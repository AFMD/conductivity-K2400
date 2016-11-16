#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__version__ = '0'

'''
Main program for Transistor measurement control. This creates and controls the threads and GUI.
'''

import os
import sys
import datetime
import getpass
from PyQt4.QtGui import *
from PyQt4.QtCore import *
import numpy as np
import pandas as pd


from measurement_engine import * # conductivity measurements
from transistor_tools_GUI import * # GUI design created QtDesigner
import Utilities # utilities file mainly for handling fmf format

from matplotlib.backends.backend_qt4agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt4agg import NavigationToolbar2QT as NavigationToolbar
import matplotlib.pyplot as plt
import matplotlibwidget


class programSetup(QObject):

    # Define unbound signal as class attribute 
    signalStatus = pyqtSignal(str)
    
    def __init__(self, parent=None):
        super(self.__class__, self).__init__(parent) # inheriting from QApplication but doesn't referene it as parent=None
        
        # Create a GUI object.self = __main__,programSetup
        self.gui = mainWindow()
        
        # Setup the worker object and the worker_thread.
        self.worker1 = keithleyWorker() 
        self.worker_thread1 = QThread()
        
        self.worker2 = WorkerObject2() 
        self.worker_thread2 = QThread()        
        
        # Move worker object to worker thread and start worker_thread.
        self.worker1.moveToThread(self.worker_thread1)
        self.worker_thread1.start()
        
        self.worker2.moveToThread(self.worker_thread2)
        self.worker_thread2.start()        
        
        # Make any cross object connections.
        self._connectSignals()
        
        self.gui.show()
        
    def _connectSignals(self): 
        self.gui.mainWindow.button_1.clicked.connect(self.gui.getInputs) # get inputs before running work
        self.gui.mainWindow.button_1.clicked.connect(self.worker1.startWork) # run worker
        
        #self.gui.mainWindow.button_2.clicked.connect(self.gui.getInputs) # get inputs before running work
        #self.gui.mainWindow.button_2.clicked.connect(self.worker2.startWork) # run work
        
        self.gui.mainWindow.button_cancel1.clicked.connect(self.forceWorkerReset1)
        #self.gui.mainWindow.button_cancel2.clicked.connect(self.forceWorkerReset2)
        self.gui.mainWindow.pushButtonSave.clicked.connect(self.gui.selectFile)
        
        self.gui.mainWindow.pushButton_save.clicked.connect(self.gui.getInputs) # Save settings        
        self.gui.mainWindow.pushButton_load.clicked.connect(self.gui.restoreState) # Restore settings
        
        self.signalStatus.connect(self.gui.updateStatus)
        self.worker1.signalStatus.connect(self.gui.updateStatus)
        self.worker2.signalStatus.connect(self.gui.updateStatus)
        self.parent().aboutToQuit.connect(self.forceQuit)
        
        self.worker1.endData.connect(self.gui.saveData)
        self.worker1.newfixedVDataPoint.connect(self.gui.plotPoint)
        self.worker1.newIVData.connect(self.gui.plotIV)   
        
        

        self.worker2.endData.connect(self.gui.saveData)
        self.worker2.newDataPoint.connect(self.gui.plotPoint)
        
        
    def forceWorkerReset1(self):
        if self.worker_thread1.isRunning():
            self.worker1.stopWork()
            self.signalStatus.emit('Measurement: Idle')
            
    def forceWorkerReset2(self):
        if self.worker_thread2.isRunning():
            self.worker2.stopWork()
            self.signalStatus.emit('Thread 2: Idle')
            
            
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
            
            
            
class keithleyWorker(QObject):
    '''IV data aquisition worker'''
    
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
        self.user_parameters = pd.DataFrame.from_csv('df_measurement.csv', header=1) # Get input parameters from df_measurement
        smu, rm = IV_Engine.connect2Keith(self)
        
        if self.user_parameters.value['takeIVsweep'] == 'True':
            v, i = IV_Engine.measure_IVsweep(self, smu)
        
        if self.user_parameters.value['takefixedV'] == 'True':
            v, i = IV_Engine.measure_fixedV(self, smu)
        
        self.signalStatus.emit('Completed IV measurements')
    
    @pyqtSlot()
    def stopWork(self):
        self._flag = True
        
        
class WorkerObject2(QObject):
    
    signalStatus = pyqtSignal(str)
    endData = pyqtSignal(object)
    newDataPoint = pyqtSignal(object)
    askParameters = pyqtSignal(object)
    
    def __init__(self, parent=None):
        super(self.__class__, self).__init__(parent)
        

    @pyqtSlot()        
    def startWork(self):
        self._flag = False
        self.signalStatus.emit('Running worker2...')
        self.user_parameters = pd.DataFrame.from_csv('df_measurement.csv')
        IV_Engine.measure_fixedV_test(self)
        
        
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
        sys.stdout = EmittingStream(textWritten=self.write) #redirect console print to UI
        self.setUpPlot()
        
        ### Widget and fmf definitions ###
        self.inputManager = pd.DataFrame.from_csv('df_template.csv', header=1) # object for metadata
        fields = list(self.inputManager.index) # create a list of the indices in the metadata file
        self.inputWidgets = [w for w in self.findChildren(QWidget) if str(w.accessibleName()) in fields] # creates list of all QWidgets in GUI        
        
        
    @pyqtSlot(str)
    def updateStatus(self, status):
        self.mainWindow.statusBar.showMessage(status)
        
    @pyqtSlot(str)
    def write(self, s):
        '''write text to text slot in UI'''
        self.mainWindow.plainTextEdit.moveCursor(QTextCursor.End)
        self.mainWindow.plainTextEdit.ensureCursorVisible()
        self.mainWindow.plainTextEdit.insertPlainText(s)
        
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
            self.inputManager.loc['setup'].value = str('IVsweep_FixedV')
        
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
            
        if self.inputManager.loc['exp_name'].value == None:
            pass # what to do if user forgets to put in exp name/sample???
            
        mainWindow.saveState(self)
        
        
    @pyqtSlot()
    def saveState(self):
        ''' Save current inputs to csv '''
        try:
            hdr =  ' --- Insitu ECHO meas template for data-frame used to store inputs and write file header - change at your own risk---,,,,'
            with open('df_measurement.csv','w') as f:
                f.write(hdr + '\n')
            self.inputManager.to_csv('df_measurement.csv', mode = 'a', na_rep = ' ') #append (hdr)
        except:
            print ('Settings NOT saved. Please check df_template status.')

    @pyqtSlot()
    def restoreState(self):
        ''' write inputManager values to user input widgets.
                input widget values saved on close to inputManager csv'''
        try:
            self.inputManager = pd.DataFrame.from_csv('df_measurement.csv', header = 1)
            for w in self.inputWidgets:
                field = w.accessibleName()
                if not (str(field) == 'exp_name' or str(field) == 'sample'):
                    if self.inputManager.loc[field].value != None:
                        Utilities.setWidgetValue(w, self.inputManager.loc[field].value)
        except:
            pass           
        
        
        
    @pyqtSlot(object)
    def saveData(self, dat):
        '''Save final data array'''
        if self.mainWindow.checkBoxSave.isChecked():
            Utilities.save_to_file(self.inputManager, dat[0], dat[1])
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
        '''Update GUI graph with new measurement point'''
        self.fixedVfig.plot(datPoint[0],datPoint[2])
        self.fixedVfig.figure.suptitle('Fixed Voltage Measurements')
        self.fixedVfig.axes.set_xlabel('Sample')
        self.fixedVfig.axes.set_ylabel('I (A)')
        self.mainWindow.pltWidget.figure.tight_layout()
        self.mainWindow.pltWidget.draw()
        
        
    @pyqtSlot(object)    
    def plotIV(self, datPoint):
        '''Update GUI graph with new measurement point'''
        self.IVfig.plot(datPoint[0],datPoint[1])
        self.IVfig.figure.suptitle('IV plot')
        self.IVfig.axes.set_xlabel('Voltage [V]')
        self.IVfig.axes.set_ylabel('I (A)')
        self.mainWindow.pltWidget.figure.tight_layout()
        self.mainWindow.pltWidget.draw()        


    def setUpPlot(self):
        '''Create matplotlib in main window'''
        embeddedGraph = self.mainWindow.pltWidget
        
        self.fixedVfig = embeddedGraph.figure.add_subplot(111)
        self.IVfig = self.mainWindow.pltWidget.figure.add_subplot(111)
        
        embeddedGraph.figure.tight_layout()
        self.mainWindow.toolbar = NavigationToolbar(embeddedGraph,self)
        self.mainWindow.plotLayout.addWidget(self.mainWindow.toolbar)
        
        
        
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
    