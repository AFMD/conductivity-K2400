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
        
    def connect2Keith(self, connSet):
        smu, rm = k2400.connect_SMU(connSet)
        print (smu.query('*IDN?'))
        return smu, rm
    
    def measure_fixedV(self, pars, smu):
        
        print ('Commencing data aquisition...')
        v = []
        i = []
        for n in range ((int(pars['nRepeats']))):
            if self._flag: 
                self.signalStatus.emit('Stopped.')
                return v, i
            vv, ii = smu.measI(pars)
            v.append(float(vv))
            i.append(float(ii))
            time.sleep(pars['pauseTime']) #Time between measurements
        return v, i
    
    def measure_fixedV_test(self, pars):
        print ('Commencing data aquisition...')
        v = []
        i = []
        for n in range (int(pars['nRepeats'])):
            if self._flag: 
                self.signalStatus.emit('Stopped.')
                print ('Measurement aborted')
                self.endData.emit(data)
                return
            
            ii = random.gauss((float(pars['fixedV'])), 5)
            vv = n
            print (vv, '\t', '%.4f' %ii)
            v.append(float(vv))
            i.append(float(ii))
            data = v, i
            self.newDataPoint.emit(data) # for live update
            time.sleep(float(pars['pauseTime']))
        self.signalStatus.emit('Complete.')
        data = v, i
        self.endData.emit(data)
        return data
    
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
        
        
        
    
    

    
        