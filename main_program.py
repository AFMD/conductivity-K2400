#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__version__ = '1'

'''
Transistor tools. This creates and controls the threads and GUI.
'''

import os
import sys
import datetime
import getpass
from PyQt4.QtGui import *
from PyQt4.QtCore import *
import numpy as np
import pandas as pd

from src.inficon_engine import * # inficon engine (imports inficon drivers)
from src.measurement_engine import * # conductivity engine (import Keithley drivers)
from src.transistor_tools_GUI import * # GUI design created QtDesigner
import src.Utilities as Utilities # utilities file mainly for handling fmf format

from matplotlib.backends.backend_qt4agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt4agg import NavigationToolbar2QT as NavigationToolbar
import matplotlib.pyplot as plt
import src.matplotlibwidget


class programSetup(QObject):

    # Define unbound signal as class attribute 
    signalStatus = pyqtSignal(str)
    
    def __init__(self, parent=None):
        super(self.__class__, self).__init__(parent) # inheriting from QApplication but doesn't referene it as parent=None
        
        # Create a GUI object.self = __main__,programSetup
        self.gui = mainWindow()
        
        # Setup the worker object and the worker_thread.
        self.worker1 = IVWorker() 
        self.worker_thread1 = QThread()
        self.worker2 = inficonWorker() 
        self.worker_thread2 = QThread() 
        self.worker3 = ConductivityWorker() 
        self.worker_thread3 = QThread()     
        
        # Move worker object to worker thread and start worker_thread.
        self.worker1.moveToThread(self.worker_thread1)
        self.worker_thread1.start()
        self.worker2.moveToThread(self.worker_thread2)
        self.worker_thread2.start()
        self.worker3.moveToThread(self.worker_thread3)
        self.worker_thread3.start()           
        
        # Make any cross object connections.
        self._connectSignals()
        self.gui.show()
        
    def _connectSignals(self): 
        # Keithley connections
        #self.gui.mainWindow.button_1.clicked.connect(self.gui.getInputs) 
        #self.gui.mainWindow.button_1.clicked.connect(self.worker1.startWork) 
        #self.gui.mainWindow.button_cancel1.clicked.connect(self.forceWorkerReset1)
        self.gui.mainWindow.pushButtonSave.clicked.connect(self.gui.selectFile)
        self.gui.mainWindow.pushButton_save.clicked.connect(self.gui.getInputs)        
        self.gui.mainWindow.pushButton_load.clicked.connect(self.gui.restoreState) 
        self.worker1.endData.connect(self.gui.saveIVData)
        self.worker1.newfixedVDataPoint.connect(self.gui.plotPoint)
        self.worker1.newIVData.connect(self.gui.plotIV)           
        self.signalStatus.connect(self.gui.updateStatus)
        # Inficon connections
        self.gui.mainWindow.pushButton_QCMStart.clicked.connect(self.gui.getInputs) 
        self.gui.mainWindow.pushButton_QCMStart.clicked.connect(self.worker2.startWork)
        self.gui.mainWindow.pushButton_QCMStop.clicked.connect(self.forceWorkerReset2)
        self.worker2.endDepositionData.connect(self.gui.saveDepositionData)
        self.worker2.newDepositionDataPoint.connect(self.gui.plotDepositionPoint)
        # Transistor Conductivity Connections
        self.gui.mainWindow.pushButton_cond_start.clicked.connect(self.gui.getInputs)
        self.gui.mainWindow.pushButton_cond_start.clicked.connect(self.worker3.startWork)
        self.gui.mainWindow.pushButton_cond_stop.clicked.connect(self.forceWorkerReset3)
        self.worker3.newIVData.connect(self.gui.plotIV)
        self.worker3.endIVData.connect(self.gui.saveIVData)
        self.worker3.endCondData.connect(self.gui.saveCondData)
        
        
        #General GUI connections
        #self.worker1.signalStatus.connect(self.gui.updateStatus)
        self.worker2.signalStatus.connect(self.gui.updateStatus)
        self.worker3.signalStatus.connect(self.gui.updateStatus)
        self.worker3.progressBar.connect(self.gui.updateProgress)
        self.worker2.InficonConsole.connect(self.gui.writeInficonConsole)
        self.worker3.IVConsole.connect(self.gui.writeIVConsole)
        self.worker3.ConductivityConsole.connect(self.gui.writeConductivityConsole)
        self.parent().aboutToQuit.connect(self.forceQuit)
        


        
    def forceWorkerReset1(self):
        if self.worker_thread1.isRunning():
            self.worker1.stopWork()
            self.signalStatus.emit('Keithley thread: Idle')
    def forceWorkerReset2(self):
        if self.worker_thread2.isRunning():
            self.worker2.stopWork()
            self.signalStatus.emit('Inficon thread: Idle')
    def forceWorkerReset3(self):
        if self.worker_thread3.isRunning():
            self.worker3.stopWork()
            self.signalStatus.emit('Conductivity thread: Idle')            
            
            
    def forceQuit(self):
        '''If parent is QApplication is killed (window closed) this shutdown the threads'''
        print ('Program shutting down safely (maybe)')
        if self.worker_thread1.isRunning():
            self.worker1.stopWork()
            #time.sleep(0.3) 
            self.worker_thread1.exit()
        if self.worker_thread2.isRunning():
            self.worker2.stopWork()
            #time.sleep(0.3) 
            self.worker_thread2.exit()
        if self.worker_thread3.isRunning():
            self.worker3.stopWork()
            #time.sleep(0.3) 
            self.worker_thread3.exit()        
            
            
            
class IVWorker(QObject):
    '''IV data aquisition worker'''
    
    IVConsole = pyqtSignal(str)
    signalStatus = pyqtSignal(str)
    endData = pyqtSignal(object)
    newfixedVDataPoint = pyqtSignal(object)
    newIVData = pyqtSignal(object)
    askParameters = pyqtSignal(object)    
    
    def __init__(self, parent=None):
        super(self.__class__, self).__init__(parent)
        
    @pyqtSlot()        
    def startWork(self):
        
        self._flag = False
        self.user_parameters = pd.DataFrame.from_csv('src/df_measurement.csv', header=1) # Get input parameters from df_measurement
        smu, rm = IV_Engine.connect2Keith(self)
        
        if self.user_parameters.value['takeIVsweep'] == 'True':
            v, i = IV_Engine.measure_IVsweep(self, smu)
        
        if self.user_parameters.value['takefixedV'] == 'True':
            v, i = IV_Engine.measure_fixedV(self, smu)
        
        self.signalStatus.emit('Completed IV measurements')
    
    @pyqtSlot()
    def stopWork(self):
        self._flag = True
        
        
class ConductivityWorker(QObject):
    '''Conductivity aquisition worker'''
    
    ConductivityConsole = pyqtSignal(str)
    IVConsole = pyqtSignal(str)
    progressBar = pyqtSignal(float)
    signalStatus = pyqtSignal(str)
    endIVData = pyqtSignal(object)
    endCondData = pyqtSignal(object)
    askParameters = pyqtSignal(object)   
    newIVData = pyqtSignal(object)
    
    def __init__(self, parent=None):
        super(self.__class__, self).__init__(parent)
        
    @pyqtSlot()        
    def startWork(self):
        
        self._flag = False
        self.signalStatus.emit('Conductivity thread running')
        self.progressBar.emit(0)
        self.user_parameters = pd.DataFrame.from_csv('src/df_measurement.csv', header=1) # Get input parameters from df_measurement
        smu, rm = Conductivity_Engine.connect2Keith(self)
        Conductivity_Engine.measure(self, smu)
        self.signalStatus.emit('Completed')
    
    @pyqtSlot()
    def stopWork(self):
        self._flag = True
        
class inficonWorker(QObject):
    
    signalStatus = pyqtSignal(str)
    InficonConsole = pyqtSignal(str)
    endDepositionData = pyqtSignal(object)
    newDepositionDataPoint = pyqtSignal(object)
    #askParameters = pyqtSignal(object)
    
    def __init__(self, parent=None):
        super(self.__class__, self).__init__(parent)
        
    @pyqtSlot()        
    def startWork(self):
        self._flag = False
        self.signalStatus.emit('Inficon thread running...')
        self.user_parameters = pd.DataFrame.from_csv('src/df_measurement.csv', header=1) # Get input parameters from df_measurement
        thickness = inficon_engine.monitor_QCM(self)
        self.InficonConsole.emit('Thickness monitoring complete.')
        
    @pyqtSlot()
    def stopWork(self):
        self._flag = True
    

class mainWindow(QMainWindow):
    '''Main applicaiton window'''
    
    signalStatus = pyqtSignal(str)

    def __init__(self, parent = None):
        
        ### QTDESIGNER MADE GUI ###
        super(mainWindow, self).__init__(parent)
        self.mainWindow = Ui_MainWindow()
        self.mainWindow.setupUi(self)
        #self.mainWindow.OFET_label.setPixmap(QtGui.QPixmap(_fromUtf8("OFET_layout.jpg")))
        self.mainWindow.OFET_label.setPixmap(QtGui.QPixmap("src/OFET_layout.jpg"))
        #sys.stdout = EmittingStream(textWritten=self.write) #redirect console print to UI
        
        ### Widget and fmf definitions ###
        self.inputManager = pd.DataFrame.from_csv('src/df_template.csv', header=1) # object for metadata
        fields = list(self.inputManager.index) # create a list of the indices in the metadata file
        self.inputWidgets = [w for w in self.findChildren(QWidget) if str(w.accessibleName()) in fields] # creates list of all QWidgets in GUI
        mainWindow.setUpPlot(self)
        
        
    @pyqtSlot(str)
    def updateStatus(self, status):
        self.mainWindow.statusBar.showMessage(status)
        
    @pyqtSlot(str)
    def updateProgress(self, value):
        self.mainWindow.progressBar.setValue(value)
        
    @pyqtSlot(str)
    def writeIVConsole(self, s):
        '''write text to text slot in UI'''
        self.mainWindow.plainTextEdit.moveCursor(QTextCursor.End)
        self.mainWindow.plainTextEdit.ensureCursorVisible()
        self.mainWindow.plainTextEdit.insertPlainText(s)
        self.mainWindow.plainTextEdit.insertPlainText('\n')
        
    @pyqtSlot(str)
    def writeInficonConsole(self, s):
        '''write text to Inficon text slot in UI'''
        self.mainWindow.plainTextEdit_2.moveCursor(QTextCursor.End)
        self.mainWindow.plainTextEdit_2.ensureCursorVisible()
        self.mainWindow.plainTextEdit_2.insertPlainText(s) 
        self.mainWindow.plainTextEdit_2.insertPlainText('\n')
        
    @pyqtSlot(str)
    def writeConductivityConsole(self, s):
        '''write text to Inficon text slot in UI'''
        self.mainWindow.plainTextEdit_3.moveCursor(QTextCursor.End)
        self.mainWindow.plainTextEdit_3.ensureCursorVisible()
        self.mainWindow.plainTextEdit_3.insertPlainText(s) 
        self.mainWindow.plainTextEdit_3.insertPlainText('\n')
        
        
    @pyqtSlot(object)
    def getInputs(self):
        '''get measurement parameters from GUI and store in dataframe.'''

        for w in self.inputWidgets:
            try:
                self.inputManager.loc[str(w.accessibleName())].value = Utilities.getWidgetValue(w)
            except:
                print ('Input parameter error: ', w.objectName())
            else:
                pass
        
        self.inputManager.loc['date'].value = str(datetime.datetime.now())
        self.inputManager.loc['user'].value = str(getpass.getuser())
        self.inputManager.loc['vers'].value = __version__
        
        if self.mainWindow.checkBox_IV.isChecked() == True and self.mainWindow.checkBox_fixedV.isChecked() == True:
            self.inputManager.loc['setup'].value = str('Conductivity')
        
        if self.mainWindow.checkBox_IV.isChecked() == True and self.mainWindow.checkBox_fixedV.isChecked() == False:
            self.inputManager.loc['setup'].value = str('IVsweep')
            self.inputManager.loc['fixedV'].value = None
            self.inputManager.loc['nRepeats'].value = None
            self.inputManager.loc['pauseTime'].value = None
            
            
        if self.mainWindow.checkBox_IV.isChecked() == False and self.mainWindow.checkBox_fixedV.isChecked() == True:
            self.inputManager.loc['setup'].value = str('FixedV')
            self.inputManager.loc['initialV'].value = None
            self.inputManager.loc['finalV'].value = None
            self.inputManager.loc['stepSize'].value = None           
            self.inputManager.loc['holdTime'].value = None            
            self.inputManager.loc['x_descript'].value = str('Sample')            
            self.inputManager.loc['x_descript'].units = None     
            
        if self.mainWindow.checkBox_IV.isChecked() == False and self.mainWindow.checkBox_fixedV.isChecked() == False:
            self.inputManager.loc['setup'].value = str('DepositionMonitoring')
            self.inputManager.loc['fixedV'].value = None
            self.inputManager.loc['nRepeats'].value = None
            self.inputManager.loc['pauseTime'].value = None
            self.inputManager.loc['initialV'].value = None
            self.inputManager.loc['finalV'].value = None
            self.inputManager.loc['stepSize'].value = None           
            self.inputManager.loc['holdTime'].value = None            
            self.inputManager.loc['x_descript'].value = str('Time')  
            self.inputManager.loc['x_descript'].units = str('s')
            self.inputManager.loc['y_descript'].value = str('QCM1 thickness, QCM1 rate, QCM2 thickness, QCM2 rate, etc.')                
            self.inputManager.loc['y_descript'].units = str('') 
            
        # For transistor picture  
        if self.mainWindow.OFET_20_1.isChecked() == True:
            self.inputManager.loc['OFET_width'].value = int(20)
            self.inputManager.loc['OFET_no'].value = int(1)
        if self.mainWindow.OFET_20_2.isChecked() == True:
            self.inputManager.loc['OFET_width'].value = int(20)
            self.inputManager.loc['OFET_no'].value = int(2)
        if self.mainWindow.OFET_20_3.isChecked() == True:
            self.inputManager.loc['OFET_width'].value = int(20)
            self.inputManager.loc['OFET_no'].value = int(3)  
        if self.mainWindow.OFET_20_4.isChecked() == True:
            self.inputManager.loc['OFET_width'].value = int(20)
            self.inputManager.loc['OFET_no'].value = int(4)
        if self.mainWindow.OFET_10_1.isChecked() == True:
            self.inputManager.loc['OFET_width'].value = int(10)
            self.inputManager.loc['OFET_no'].value = int(1)
        if self.mainWindow.OFET_10_2.isChecked() == True:
            self.inputManager.loc['OFET_width'].value = int(10)
            self.inputManager.loc['OFET_no'].value = int(2)
        if self.mainWindow.OFET_10_3.isChecked() == True:
            self.inputManager.loc['OFET_width'].value = int(10)
            self.inputManager.loc['OFET_no'].value = int(3)  
        if self.mainWindow.OFET_10_4.isChecked() == True:
            self.inputManager.loc['OFET_width'].value = int(10)
            self.inputManager.loc['OFET_no'].value = int(4)      
        if self.mainWindow.OFET_5_1.isChecked() == True:
            self.inputManager.loc['OFET_width'].value = int(5)
            self.inputManager.loc['OFET_no'].value = int(1)
        if self.mainWindow.OFET_5_2.isChecked() == True:
            self.inputManager.loc['OFET_width'].value = int(5)
            self.inputManager.loc['OFET_no'].value = int(2)
        if self.mainWindow.OFET_5_3.isChecked() == True:
            self.inputManager.loc['OFET_width'].value = int(5)
            self.inputManager.loc['OFET_no'].value = int(3)  
        if self.mainWindow.OFET_5_4.isChecked() == True:
            self.inputManager.loc['OFET_width'].value = int(5)
            self.inputManager.loc['OFET_no'].value = int(4)         
        if self.mainWindow.OFET_2p5_1.isChecked() == True:
            self.inputManager.loc['OFET_width'].value = float(2.5)
            self.inputManager.loc['OFET_no'].value = int(1)
        if self.mainWindow.OFET_2p5_2.isChecked() == True:
            self.inputManager.loc['OFET_width'].value = float(2.5)
            self.inputManager.loc['OFET_no'].value = int(2)
        if self.mainWindow.OFET_2p5_3.isChecked() == True:
            self.inputManager.loc['OFET_width'].value = float(2.5)
            self.inputManager.loc['OFET_no'].value = int(3)  
        if self.mainWindow.OFET_2p5_4.isChecked() == True:
            self.inputManager.loc['OFET_width'].value = float(2.5)
            self.inputManager.loc['OFET_no'].value = int(4)             
        
        
        if self.inputManager.loc['exp_name'].value == None:
            pass # what to do if user forgets to put in exp name/sample???
            
        mainWindow.saveState(self)
        
        
    @pyqtSlot()
    def saveState(self):
        ''' Save current inputs to csv '''
        try:
            hdr =  ' --- Insitu ECHO meas template for data-frame used to store inputs and write file header - change at your own risk---,,,,'
            with open('src/df_measurement.csv','w') as f:
                f.write(hdr + '\n')
            self.inputManager.to_csv('src/df_measurement.csv', mode = 'a', na_rep = ' ') #append (hdr)
        except:
            print ('Settings NOT saved. Please check df_template status.')

    @pyqtSlot()
    def restoreState(self):
        ''' write inputManager values to user input widgets.
                input widget values saved on close to inputManager csv'''
        try:
            self.inputManager = pd.DataFrame.from_csv('src/df_measurement.csv', header = 1)
            for w in self.inputWidgets:
                field = w.accessibleName()
                if not (str(field) == 'exp_name' or str(field) == 'sample'):
                    if self.inputManager.loc[field].value != None:
                        Utilities.setWidgetValue(w, self.inputManager.loc[field].value)
        except:
            pass           
        
        
        
    @pyqtSlot(object)
    def saveIVData(self, dat):
        '''Save final data array'''
        if self.mainWindow.checkBoxSave.isChecked():
            self.inputManager.loc['setup'].value = str('IV_sweep')
            Utilities.save_to_file(self.inputManager, dat[0], dat[1])
        else:
            print ('### Data has not been saved. ###')
            
    @pyqtSlot(object)
    def saveCondData(self, dat):
        '''Save final data array'''
        if self.mainWindow.checkBoxSave.isChecked():
            self.inputManager.loc['setup'].value = str('Conductivity')
            Utilities.conductivity_save_to_file(self.inputManager, dat[0], dat[1], dat[2], dat[3])
        else:
            print ('### Data has not been saved. ###')    
            
    @pyqtSlot(object)
    def saveDepositionData(self, dat):
        '''Save final data array'''
        if self.mainWindow.checkBoxSave.isChecked():
            Utilities.deposition_save_to_file(self.inputManager, dat[0], dat[1], dat[2], dat[3], dat[4], dat[5], dat[6], dat[7], dat[8])
        else:
            print ('### Data has not been saved. ###')    

            
    @pyqtSlot()
    def selectFile(self):
        '''Directory browser on gui.
        Only allow user to choose directory. avoids idiocy'''
        try:
            current = self.mainWindow.lineEditSave.text()
            self.mainWindow.lineEditSave.setText(QFileDialog(directory = current).getExistingDirectory()+'/')
        except Exception:
            self.mainWindow.lineEditSave.setText(QFileDialog().getExistingDirectory()+'/')
            
            
        
    @pyqtSlot(object)    
    def plotPoint(self, datPoint):
        '''Update GUI graph with new IV measurement point'''
        self.fixedVfig.plot(datPoint[0],datPoint[2])
        self.fixedVfig.figure.suptitle('Fixed Voltage Measurements')
        self.fixedVfig.axes.set_xlabel('Sample')
        self.fixedVfig.axes.set_ylabel('I (A)')
        self.mainWindow.pltWidget.figure.tight_layout()
        self.mainWindow.pltWidget.draw()
        
    @pyqtSlot(object)    
    def plotDepositionPoint(self, datPoint):
        '''Update GUI graph with new deposition measurement point'''
        if (self.mainWindow.comboBoxQCM_Display.currentText() == 'Thickness'):
            self.depositionfig.plot(datPoint[0],datPoint[1], 'rs', datPoint[0],datPoint[3], 'bs', datPoint[0],datPoint[5], 'gs', datPoint[0],datPoint[7], 'ys',)
            self.depositionfig.figure.suptitle('Thickness Monitor')
            self.depositionfig.axes.set_xlabel('Time (s)')
            self.depositionfig.axes.set_ylabel('Thickness (Angstroms)')
            self.mainWindow.pltWidget_2.figure.tight_layout()
            self.mainWindow.pltWidget_2.draw()
        if (self.mainWindow.comboBoxQCM_Display.currentText() == 'Rates'):
            self.depositionfig.plot(datPoint[0],datPoint[2], 'r--', datPoint[0],datPoint[4], 'b--', datPoint[0],datPoint[6], 'g--', datPoint[0],datPoint[8], 'y--',)
            self.depositionfig.figure.suptitle('Rate Monitor')
            self.depositionfig.axes.set_xlabel('Time (s)')
            self.depositionfig.axes.set_ylabel('Rate (Angstroms/sec)')
            self.mainWindow.pltWidget_2.figure.tight_layout()
            self.mainWindow.pltWidget_2.draw()        
        
        
        
    @pyqtSlot(object)    
    def plotIV(self, datPoint):
        '''Update GUI graph with new measurement point'''
        #embeddedGraph = self.mainWindow.pltWidget
        #self.IVfig = self.mainWindow.pltWidget.figure.add_subplot(111)
        #embeddedGraph.figure.tight_layout()
        #self.mainWindow.toolbar = NavigationToolbar(embeddedGraph,self)
        #self.mainWindow.plotLayout.addWidget(self.mainWindow.toolbar)
        
        self.IVfig.plot(datPoint[0],datPoint[1])
        self.IVfig.figure.suptitle('IV plot')
        self.IVfig.axes.set_xlabel('Voltage [V]')
        self.IVfig.axes.set_ylabel('I (A)')
        self.mainWindow.pltWidget.figure.tight_layout()
        self.mainWindow.pltWidget.draw()        


    def setUpPlot(self):
        '''Create matplotlib in main window'''
        # Conductivity plot
        embeddedGraph = self.mainWindow.pltWidget
        #self.fixedVfig = embeddedGraph.figure.add_subplot(111)
        self.IVfig = self.mainWindow.pltWidget.figure.add_subplot(111)
        embeddedGraph.figure.tight_layout()
        self.mainWindow.toolbar = NavigationToolbar(embeddedGraph,self)
        self.mainWindow.plotLayout.addWidget(self.mainWindow.toolbar)
        # Deposition Plot
        embeddedGraph2 = self.mainWindow.pltWidget_2
        self.depositionfig = embeddedGraph2.figure.add_subplot(111)
        embeddedGraph2.figure.tight_layout()
        self.mainWindow.toolbar2 = NavigationToolbar(embeddedGraph2,self)
        self.mainWindow.plotLayout_2.addWidget(self.mainWindow.toolbar2)        
        
        
class EmittingStream(QObject):
    '''object for print to gui'''
    
    textWritten = pyqtSignal(str)
    
    def write(self, text):
        self.textWritten.emit(str(text))
        
    def flush(self):
        '''system.stdout must be replaced with file-like object,
        therefore we include the flush method'''
        pass
        
    
        
def main():
    qt_app = QApplication([]) # create an instance of class QApplication
    win = programSetup(qt_app) # create an instance of programSetup inheriting from QApplication
    qt_app.exec_() # start event loop of the QApplication

if __name__=='__main__':
    main()
    