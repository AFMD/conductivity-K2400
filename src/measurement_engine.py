#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
Methods and classes used for IV measurements. Run in separate thread from GUI.
'''

import time
import random
import numpy as np

from src.k2400_control import * # conductivity engine controls keithley

class Conductivity_Engine():
    '''Routine for fixed-voltage measurements and IV sweep'''
    def __init__(self, parent=None):
        pass

    def connect2Keith(self):
        smu, rm = k2400.connect_SMU(self.user_parameters)
        return smu, rm	

    def measure(self, smu):
        
        width = self.user_parameters.value['OFET_width']
        thickness = self.user_parameters.value['OFET_thickness']
        number = self.user_parameters.value['OFET_no']
        name = str('OFET'+'_'+width+'_'+number)
        self.ConductivityConsole.emit('Measuring: '+name)
        
        # IV Sweep for Ohmic injection check
        self.IVConsole.emit('Commencing IV Sweep...')
        v = []
        i = []
        
        if self._flag: 
            self.signalStatus.emit('Stopped.')
            self.IVConsole.emit('Measurement aborted')
            return

        v, i = smu.measIVsweep(self.user_parameters.value)
        data = v, i
             
        self.IVConsole.emit('Voltage [V] \t Current [A]')
        for n in range(len(v)):
            self.IVConsole.emit('%.2f \t %.4g' % (data[0][n] ,data[1][n]))
        
        self.newIVData.emit(data) # for graph update
        self.endIVData.emit(data)
        self.progressBar.emit(20)
        
        if self._flag: 
            self.signalStatus.emit('Stopped.')
            self.IVConsole.emit('Measurement aborted')
            return
        
        # Conductivity Measurement
        self.ConductivityConsole.emit('Sample \t Current [A] \t Conductivity [S/cm]')
        sample = []
        current = []
        voltage =[]
        conductivity = []
        for n in range((int(self.user_parameters.value['nRepeats']))):
            if self._flag: 
                self.signalStatus.emit('Stopped.')
                self.ConductivityConsole.emit('Measurement aborted')            
            vv, ii = smu.measConductivity(self.user_parameters.value) # the actual measurement - default 20 secs
            current.append(float(ii))
            voltage.append(float(vv))
            sample.append(int(n))
            # conductivity calculation
            oo = (ii/vv)*((float(width)*(1e-6))/(0.5e-3*(float(thickness)*1e-9))) # finger length * film thickness!!
            conductivity.append(float(oo))
            self.ConductivityConsole.emit('%s \t %.4g \t %.2e' % ((n+1), ii, oo*1e-2))
            self.progressBar.emit(20+(n+1)*(80/(int(self.user_parameters.value['nRepeats']))))
            if self._flag: 
                self.signalStatus.emit('Stopped.')
                data2 = sample, voltage, current, conductivity    
                self.endCondData.emit(data2)                
                self.ConductivityConsole.emit('Measurement aborted')
                return
         
        data2 = sample, voltage, current, conductivity    
        self.endCondData.emit(data2)
        return
        
class IV_Engine():
    
    '''Routine for fixed-voltage measurements and IV sweep'''
    def __init__(self, parent=None):
        #self._flag1 = False
        #sys.stdout = EmittingStream(textWritten=self.write) #redirect console print to UI
        pass
        
    def connect2Keith(self):
        smu, rm = k2400.connect_SMU(self.user_parameters)
        #print (smu.query('*IDN?'))
        return smu, rm
    
    def measure_fixedV(self, smu):
    
        self.KeithleyConsole.emit('Commencing fixed voltage measurements...')
        self.signalStatus.emit('Running fixed voltage measurement...')
        self.KeithleyConsole.emit('Sample', '\t', 'Voltage [V]', '\t', 'Current [A]')
        v = []
        i = []
        t = []
        for n in range ((int(self.user_parameters.value['nRepeats']))):
            if self._flag: 
                self.signalStatus.emit('Stopped.')
                self.KeithleyConsole.emit('Measurement aborted')
                return v, i
            vv, ii = smu.measV(self.user_parameters.value)
            self.KeithleyConsole.emit(n, '\t', vv, '\t', '%.4g' %ii)
            v.append(float(vv))
            i.append(float(ii))
            t.append(int(n))
            data = t, v, i
            self.newfixedVDataPoint.emit(data) # for live update
            time.sleep(float(self.user_parameters.value['pauseTime'])) #Time between measurements
        data = t, i
        self.endData.emit(data)
        return v, i
    
    def measure_IVsweep(self, smu):
        
        
        self.KeithleyConsole.emit('Commencing IV Sweep...')
        
        v = []
        i = []
        if self._flag: 
            self.signalStatus.emit('Stopped.')
            self.KeithleyConsole.emit('Measurement aborted')
            return v, i
        v, i = smu.measIVsweep(self.user_parameters.value)
        data = v, i
        
        self.KeithleyConsole.emit('Voltage [V]', '\t', 'Current [A]')
        for n in range(len(v)):
            self.KeithleyConsole.emit(data[0][n], '\t', '%.4g' %data[1][n])
        
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
        
        
        
    
    

    
        