#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
Code for controlling the Keithley2400. Code taken from Ivan's TPV setup: 
https://github.com/AFMD/transients
'''

import visa
import sys

defaultstdout = sys.stdout #save default console print location

class k2400():
	'''Class to control keithley SMU'''
	def __init__(self, rm, connectionPars):
		'''Connect to the Keithley?'''
		#self.inst = Utilities.inst_connect(rm, connectionPars)
		self.inst = k2400.inst_connect(rm, connectionPars)
		
		
	def inst_connect(rm, connectionPars):
		'''function to return a pyvisa Resource given some pars
		currently only works for serial'''
	#     print(connectionPars['connectionType'], type(connectionPars['connectionType']))
		if str(connectionPars['connectionType']) == 'Serial':
			baudR = int(connectionPars['baudR'])
			termChar = connectionPars['termChar']
			address = 'ASRL/dev/tty%s%s::INSTR'%(connectionPars['serAdapt'], connectionPars['serAd'])
			#print(address)
			inst = rm.open_resource(address)
			inst.read_termination = k2400.input2unicode(termChar) #needs to be unicode, cf getwidgetValue
			inst.baud_rate = baudR
	
			return inst
	
			#ross add other options here
		else:
			raise Exception('connection type %s not suported for SMU'%connectionPars['connectionType'])
	
	def input2unicode(s):
		s = s.replace('\\r','\r')
		s = s.replace('\\n','\n')
		return s #unicode(s) does not work here?	
		
	def connect_SMU(connSet):
		'''Method to connect to keithley'''
		rm = visa.ResourceManager('@py') #use py-visa backend
		smu = k2400(rm, connSet)
		return smu, rm		

	def write(self, s):
		'''Standard pyvisa write no added debug'''
		self.inst.write(s)

	def query(self, s):
		'''Standard pyvisa query no added debug'''
		a = self.inst.query(s)
		return a

	
	def measI(self, pars):
		'''take a current measurement at fixed voltage V'''
		self.write(':SYST:BEEP:STAT OFF') #TURN OFF annoying beeb
		self.write(':TRIG:COUN 1')	#set to output 1 pulse
		self.write(':SOUR:FUNC VOLT')	#SELECT SOURCE
		self.write(':SENS:FUNC:CONC OFF') #do not measure both V and I concurrently
		self.write(':SOUR:VOLT:MODE FIXED') #fixed voltage source mode
		self.write(':SOUR:VOLT:RANG:AUTO ON') #auto range for voltage
		self.write(':SOUR:VOLT:LEV %s'%pars['fixedV']) #choose voltage for measurement
		self.write(':SENS:CURR:PROT 100E-3') # 100mA compliance - is this good???
		self.write(':SENS:FUNC "CURR"') #Choose current measurement function
		self.write(':SENS:CURR:RANG:AUTO ON') #Autorange for current measuremnet
		self.write(':FORM:ELEM VOLT,CURR') #voltage and current reading
		self.write(':OUTP ON')
		print(self.query(':READ?'))
		v, i =[float(x) for x in self.query('READ?').split(',')] #break data str into values
		self.write('OUTP OFF')
		return v, i

	
