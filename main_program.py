#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__version__ = '0'

'''
Main program for Transistor measurement control. This creates and controls the threads and GUI.
'''

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
        self.gui.mainWindow.button_1.clicked.connect(self.worker1.startWork)
        
        self.gui.mainWindow.button_2.clicked.connect(self.gui.getInputs) # get inputs before running work
        self.gui.mainWindow.button_2.clicked.connect(self.worker2.startWork) # run work
        
        self.gui.mainWindow.button_cancel1.clicked.connect(self.forceWorkerReset1)
        self.gui.mainWindow.button_cancel2.clicked.connect(self.forceWorkerReset2)
        self.gui.mainWindow.pushButtonSave.clicked.connect(self.gui.selectFile)
        self.signalStatus.connect(self.gui.updateStatus)
        self.worker1.signalStatus.connect(self.gui.updateStatus)
        self.worker2.signalStatus.connect(self.gui.updateStatus)
        self.parent().aboutToQuit.connect(self.forceQuit)
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
            time.sleep(1) 
            self.worker_thread1.exit()
        if self.worker_thread2.isRunning():
            self.worker2.stopWork()
            time.sleep(1) 
            self.worker_thread2.exit()
            
            
            
class keithleyWorker(QObject):
    '''Conductivity data aquisition worker'''
    
    signalStatus = pyqtSignal(str)
    
    def __init__(self, parent=None):
        super(self.__class__, self).__init__(parent)
        
    @pyqtSlot()        
    def startWork(self):
        self._flag = False
       
        self.signalStatus.emit('Running measurement...')
        
        connSet = {'baudR':57600, 'termChar':u'\r', 'serAdapt':'USB','serAd':0, 'connectionType':'Serial', 'debug':1}
        smu, rm = IV_Engine.connect2Keith(self, connSet)
        
        pars = {'fixedV':0, 'nRepeats':20, 'pauseTime':1} #Set measurement parameters
        v,i = IV_Engine.measure_fixedV(self, pars, smu)
    
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
        
        self.conductivityParams = pd.DataFrame.from_csv('df_measurement.csv')
        IV_Engine.measure_fixedV_test(self, self.conductivityParams.value)
        
        
    @pyqtSlot()
    def stopWork(self):
        self._flag = True
    

class mainWindow(QMainWindow):
    '''Main applicaiton window'''

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
                #print (str(w.accessibleName()), '\t', self.inputManager.loc[str(w.accessibleName())].value)
        
        self.inputManager.loc['date'].value = str(datetime.datetime.now())
        self.inputManager.loc['user'].value = str(getpass.getuser())
        self.inputManager.loc['vers'].value = __version__
        
        self.inputManager.to_csv('df_measurement.csv')
        
        
    @pyqtSlot(object)
    def saveData(self, dat):
        '''Save final data array'''
        if self.mainWindow.checkBoxSave.isChecked():
            data2save = np.column_stack((dat[0],dat[1]))
            format = ['%.6e']*data2save.shape[1] # number of columns
            
            try:
                directory = self.mainWindow.lineEditSave.text()
                filename = 'testing.txt'
                savepath = str(directory+filename)
                np.savetxt(savepath, data2save, delimiter='\t')
                print ('Data saved:', savepath)
            except:
                pass # need to add user proof options
            
        else: 
            print ('Data not saved')
            
            
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
        self.figData.plot(datPoint[0],datPoint[1])
        self.mainWindow.pltWidget.draw()


    def setUpPlot(self):
        '''Create matplotlib in main window'''
        embeddedGraph = self.mainWindow.pltWidget
        embeddedGraph.axes.set_xlabel('V (V)')
        embeddedGraph.axes.set_ylabel('I (Amps)')
        
        self.figData = embeddedGraph.figure.add_subplot(111)
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
    