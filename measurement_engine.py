#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
Methods and classes used for conductivity measurements. Run in separate thread from GUI.
'''

import time
import random
import numpy as np

from k2400_control import * # conductivity engine controls keithley

class IV_Engine():
    '''Routine for fixed-voltage measurements and IV sweep'''
    def __init__(self, parent=None):
        self._flag1 = False
        sys.stdout = EmittingStream(textWritten=self.write) #redirect console print to UI
        
    def connect2Keith(self):
        smu, rm = k2400.connect_SMU(self.user_parameters)
        #print (smu.query('*IDN?'))
        return smu, rm
    
    def measure_fixedV(self, smu):
        
        print ('Commencing fixed voltage measurements...')
        self.signalStatus.emit('Running fixed voltage measurement...')
        print ('Sample', '\t', 'Voltage [V]', '\t', 'Current [A]')
        v = []
        i = []
        t = []
        for n in range ((int(self.user_parameters.value['nRepeats']))):
            if self._flag: 
                self.signalStatus.emit('Stopped.')
                print ('Measurement aborted')
                return v, i
            vv, ii = smu.measV(self.user_parameters.value)
            print (n, '\t', vv, '\t', '%.4g' %ii)
            v.append(float(vv))
            i.append(float(ii))
            t.append(int(n))
            data = t, v, i
            self.newfixedVDataPoint.emit(data) # for live update
            time.sleep(float(self.user_parameters.value['pauseTime'])) #Time between measurements
        data = t, i
        self.endData.emit(data)
        return v, i
    
    def measure_fixedV_test(self):
        
        print ('Commencing data aquisition...')
        v = []
        i = []
        for n in range (int(self.user_parameters.value['nRepeats'])):
            if self._flag: 
                self.signalStatus.emit('Stopped.')
                print ('Measurement aborted')
                self.endData.emit(data)
                return
            
            ii = random.gauss((float(self.user_parameters.value['fixedV'])), 5)
            vv = n
            print (vv, '\t', '%.4f' %ii)
            v.append(float(vv))
            i.append(float(ii))
            data = v, i
            self.newDataPoint.emit(data) # for live update
            time.sleep(float(self.user_parameters.value['pauseTime']))
        data = v, i
        self.endData.emit(data)
        return data
    
    def measure_IVsweep(self, smu):
        
        print ('Commencing IV Sweep...')
        
        v = []
        i = []
        if self._flag: 
            self.signalStatus.emit('Stopped.')
            print ('Measurement aborted')
            return v, i
        v, i = smu.measIVsweep(self.user_parameters.value)
        data = v, i
        
        print ('Voltage [V]', '\t', 'Current [A]')
        for n in range(len(v)):
            print (data[0][n], '\t', '%.4g' %data[1][n])
        
        self.newIVData.emit(data) # for graph update
        self.endData.emit(data)
        return v, i        

        
class livePlot:
    '''Class for plotting the conductivity data live'''
    
    def __init__(self, parent=None, width =5, height=4, dpi=100):
        fig = Figure(figsize = (width,height), dpi=dpi)
        self.axes = fig.add_subplot(111)
        self.axes.hold(False)
        self.initial_fig()
        
    
    def animatePlot(graph_data):
        ax1.clear()
        ax1.plot(data)
        
        
        
    
    

    
        