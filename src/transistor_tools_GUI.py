# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'transistor_tools_GUI.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(733, 983)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.tabWidget = QtGui.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(10, 20, 711, 931))
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.tab = QtGui.QWidget()
        self.tab.setObjectName(_fromUtf8("tab"))
        self.groupBox = QtGui.QGroupBox(self.tab)
        self.groupBox.setGeometry(QtCore.QRect(100, 190, 509, 531))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.verticalLayoutWidget_2 = QtGui.QWidget(self.groupBox)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(20, 40, 461, 491))
        self.verticalLayoutWidget_2.setObjectName(_fromUtf8("verticalLayoutWidget_2"))
        self.verticalLayout = QtGui.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.comboBox_Measurement = QtGui.QComboBox(self.verticalLayoutWidget_2)
        self.comboBox_Measurement.setObjectName(_fromUtf8("comboBox_Measurement"))
        self.comboBox_Measurement.addItem(_fromUtf8(""))
        self.comboBox_Measurement.addItem(_fromUtf8(""))
        self.comboBox_Measurement.addItem(_fromUtf8(""))
        self.comboBox_Measurement.addItem(_fromUtf8(""))
        self.verticalLayout.addWidget(self.comboBox_Measurement)
        self.stackedWidget = QtGui.QStackedWidget(self.verticalLayoutWidget_2)
        self.stackedWidget.setFrameShape(QtGui.QFrame.StyledPanel)
        self.stackedWidget.setFrameShadow(QtGui.QFrame.Sunken)
        self.stackedWidget.setLineWidth(2)
        self.stackedWidget.setObjectName(_fromUtf8("stackedWidget"))
        self.page_IVmeas = QtGui.QWidget()
        self.page_IVmeas.setObjectName(_fromUtf8("page_IVmeas"))
        self.verticalLayoutWidget_3 = QtGui.QWidget(self.page_IVmeas)
        self.verticalLayoutWidget_3.setGeometry(QtCore.QRect(20, 230, 421, 181))
        self.verticalLayoutWidget_3.setObjectName(_fromUtf8("verticalLayoutWidget_3"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.verticalLayoutWidget_3)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.label_6 = QtGui.QLabel(self.verticalLayoutWidget_3)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.verticalLayout_2.addWidget(self.label_6)
        self.checkBox_fixedV = QtGui.QCheckBox(self.verticalLayoutWidget_3)
        self.checkBox_fixedV.setChecked(False)
        self.checkBox_fixedV.setObjectName(_fromUtf8("checkBox_fixedV"))
        self.verticalLayout_2.addWidget(self.checkBox_fixedV)
        self.gridLayout_3 = QtGui.QGridLayout()
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.label = QtGui.QLabel(self.verticalLayoutWidget_3)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout_3.addWidget(self.label, 1, 0, 1, 1)
        self.label_2 = QtGui.QLabel(self.verticalLayoutWidget_3)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout_3.addWidget(self.label_2, 2, 0, 1, 1)
        self.label_3 = QtGui.QLabel(self.verticalLayoutWidget_3)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout_3.addWidget(self.label_3, 3, 0, 1, 1)
        self.doubleSpinBox_Voltage = QtGui.QDoubleSpinBox(self.verticalLayoutWidget_3)
        self.doubleSpinBox_Voltage.setDecimals(1)
        self.doubleSpinBox_Voltage.setMaximum(100.0)
        self.doubleSpinBox_Voltage.setProperty("value", 1.0)
        self.doubleSpinBox_Voltage.setObjectName(_fromUtf8("doubleSpinBox_Voltage"))
        self.gridLayout_3.addWidget(self.doubleSpinBox_Voltage, 1, 1, 1, 1)
        self.doubleSpinBox_pauseTime = QtGui.QDoubleSpinBox(self.verticalLayoutWidget_3)
        self.doubleSpinBox_pauseTime.setDecimals(1)
        self.doubleSpinBox_pauseTime.setMaximum(1000.0)
        self.doubleSpinBox_pauseTime.setProperty("value", 0.5)
        self.doubleSpinBox_pauseTime.setObjectName(_fromUtf8("doubleSpinBox_pauseTime"))
        self.gridLayout_3.addWidget(self.doubleSpinBox_pauseTime, 3, 1, 1, 1)
        self.spinBox_nRepeats = QtGui.QSpinBox(self.verticalLayoutWidget_3)
        self.spinBox_nRepeats.setMaximum(1000)
        self.spinBox_nRepeats.setProperty("value", 20)
        self.spinBox_nRepeats.setObjectName(_fromUtf8("spinBox_nRepeats"))
        self.gridLayout_3.addWidget(self.spinBox_nRepeats, 2, 1, 1, 1)
        self.verticalLayout_2.addLayout(self.gridLayout_3)
        self.verticalLayoutWidget_4 = QtGui.QWidget(self.page_IVmeas)
        self.verticalLayoutWidget_4.setGeometry(QtCore.QRect(20, 30, 421, 151))
        self.verticalLayoutWidget_4.setObjectName(_fromUtf8("verticalLayoutWidget_4"))
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.verticalLayoutWidget_4)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.label_7 = QtGui.QLabel(self.verticalLayoutWidget_4)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.verticalLayout_3.addWidget(self.label_7)
        self.checkBox_IV = QtGui.QCheckBox(self.verticalLayoutWidget_4)
        self.checkBox_IV.setChecked(False)
        self.checkBox_IV.setObjectName(_fromUtf8("checkBox_IV"))
        self.verticalLayout_3.addWidget(self.checkBox_IV)
        self.gridLayout_4 = QtGui.QGridLayout()
        self.gridLayout_4.setObjectName(_fromUtf8("gridLayout_4"))
        self.doubleSpinBox_4 = QtGui.QDoubleSpinBox(self.verticalLayoutWidget_4)
        self.doubleSpinBox_4.setDecimals(2)
        self.doubleSpinBox_4.setMaximum(60.0)
        self.doubleSpinBox_4.setSingleStep(0.1)
        self.doubleSpinBox_4.setProperty("value", 0.1)
        self.doubleSpinBox_4.setObjectName(_fromUtf8("doubleSpinBox_4"))
        self.gridLayout_4.addWidget(self.doubleSpinBox_4, 1, 3, 1, 1)
        self.label_11 = QtGui.QLabel(self.verticalLayoutWidget_4)
        self.label_11.setObjectName(_fromUtf8("label_11"))
        self.gridLayout_4.addWidget(self.label_11, 1, 2, 1, 1)
        self.label_10 = QtGui.QLabel(self.verticalLayoutWidget_4)
        self.label_10.setObjectName(_fromUtf8("label_10"))
        self.gridLayout_4.addWidget(self.label_10, 1, 0, 1, 1)
        self.doubleSpinBox_3 = QtGui.QDoubleSpinBox(self.verticalLayoutWidget_4)
        self.doubleSpinBox_3.setMinimum(0.0)
        self.doubleSpinBox_3.setMaximum(5.0)
        self.doubleSpinBox_3.setSingleStep(0.5)
        self.doubleSpinBox_3.setProperty("value", 0.5)
        self.doubleSpinBox_3.setObjectName(_fromUtf8("doubleSpinBox_3"))
        self.gridLayout_4.addWidget(self.doubleSpinBox_3, 1, 1, 1, 1)
        self.doubleSpinBox_2 = QtGui.QDoubleSpinBox(self.verticalLayoutWidget_4)
        self.doubleSpinBox_2.setDecimals(1)
        self.doubleSpinBox_2.setMaximum(50.0)
        self.doubleSpinBox_2.setProperty("value", 10.0)
        self.doubleSpinBox_2.setObjectName(_fromUtf8("doubleSpinBox_2"))
        self.gridLayout_4.addWidget(self.doubleSpinBox_2, 0, 3, 1, 1)
        self.label_8 = QtGui.QLabel(self.verticalLayoutWidget_4)
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.gridLayout_4.addWidget(self.label_8, 0, 0, 1, 1)
        self.label_9 = QtGui.QLabel(self.verticalLayoutWidget_4)
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.gridLayout_4.addWidget(self.label_9, 0, 2, 1, 1)
        self.doubleSpinBox = QtGui.QDoubleSpinBox(self.verticalLayoutWidget_4)
        self.doubleSpinBox.setDecimals(1)
        self.doubleSpinBox.setMinimum(-50.0)
        self.doubleSpinBox.setMaximum(0.0)
        self.doubleSpinBox.setProperty("value", -10.0)
        self.doubleSpinBox.setObjectName(_fromUtf8("doubleSpinBox"))
        self.gridLayout_4.addWidget(self.doubleSpinBox, 0, 1, 1, 1)
        self.verticalLayout_3.addLayout(self.gridLayout_4)
        self.stackedWidget.addWidget(self.page_IVmeas)
        self.page_keithley = QtGui.QWidget()
        self.page_keithley.setObjectName(_fromUtf8("page_keithley"))
        self.verticalLayoutWidget_6 = QtGui.QWidget(self.page_keithley)
        self.verticalLayoutWidget_6.setGeometry(QtCore.QRect(20, 20, 421, 405))
        self.verticalLayoutWidget_6.setObjectName(_fromUtf8("verticalLayoutWidget_6"))
        self.verticalLayout_5 = QtGui.QVBoxLayout(self.verticalLayoutWidget_6)
        self.verticalLayout_5.setObjectName(_fromUtf8("verticalLayout_5"))
        self.label_22 = QtGui.QLabel(self.verticalLayoutWidget_6)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_22.setFont(font)
        self.label_22.setObjectName(_fromUtf8("label_22"))
        self.verticalLayout_5.addWidget(self.label_22)
        self.gridLayout_5 = QtGui.QGridLayout()
        self.gridLayout_5.setObjectName(_fromUtf8("gridLayout_5"))
        self.label_12 = QtGui.QLabel(self.verticalLayoutWidget_6)
        self.label_12.setObjectName(_fromUtf8("label_12"))
        self.gridLayout_5.addWidget(self.label_12, 0, 0, 1, 1)
        self.label_13 = QtGui.QLabel(self.verticalLayoutWidget_6)
        self.label_13.setObjectName(_fromUtf8("label_13"))
        self.gridLayout_5.addWidget(self.label_13, 3, 0, 1, 1)
        self.comboBox_2 = QtGui.QComboBox(self.verticalLayoutWidget_6)
        self.comboBox_2.setObjectName(_fromUtf8("comboBox_2"))
        self.comboBox_2.addItem(_fromUtf8(""))
        self.gridLayout_5.addWidget(self.comboBox_2, 1, 1, 1, 1)
        self.label_16 = QtGui.QLabel(self.verticalLayoutWidget_6)
        self.label_16.setAccessibleName(_fromUtf8(""))
        self.label_16.setObjectName(_fromUtf8("label_16"))
        self.gridLayout_5.addWidget(self.label_16, 2, 0, 1, 1)
        self.label_14 = QtGui.QLabel(self.verticalLayoutWidget_6)
        self.label_14.setObjectName(_fromUtf8("label_14"))
        self.gridLayout_5.addWidget(self.label_14, 4, 0, 1, 1)
        self.comboBox_3 = QtGui.QComboBox(self.verticalLayoutWidget_6)
        self.comboBox_3.setObjectName(_fromUtf8("comboBox_3"))
        self.comboBox_3.addItem(_fromUtf8(""))
        self.gridLayout_5.addWidget(self.comboBox_3, 3, 1, 1, 1)
        self.comboBox = QtGui.QComboBox(self.verticalLayoutWidget_6)
        self.comboBox.setObjectName(_fromUtf8("comboBox"))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.gridLayout_5.addWidget(self.comboBox, 0, 1, 1, 1)
        self.comboBox_4 = QtGui.QComboBox(self.verticalLayoutWidget_6)
        self.comboBox_4.setObjectName(_fromUtf8("comboBox_4"))
        self.comboBox_4.addItem(_fromUtf8(""))
        self.gridLayout_5.addWidget(self.comboBox_4, 4, 1, 1, 1)
        self.label_15 = QtGui.QLabel(self.verticalLayoutWidget_6)
        self.label_15.setObjectName(_fromUtf8("label_15"))
        self.gridLayout_5.addWidget(self.label_15, 1, 0, 1, 1)
        self.comboBox_5 = QtGui.QComboBox(self.verticalLayoutWidget_6)
        self.comboBox_5.setObjectName(_fromUtf8("comboBox_5"))
        self.comboBox_5.addItem(_fromUtf8(""))
        self.gridLayout_5.addWidget(self.comboBox_5, 2, 1, 1, 1)
        self.verticalLayout_5.addLayout(self.gridLayout_5)
        self.label_20 = QtGui.QLabel(self.verticalLayoutWidget_6)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_20.setFont(font)
        self.label_20.setObjectName(_fromUtf8("label_20"))
        self.verticalLayout_5.addWidget(self.label_20)
        self.gridLayout_7 = QtGui.QGridLayout()
        self.gridLayout_7.setObjectName(_fromUtf8("gridLayout_7"))
        self.label_25 = QtGui.QLabel(self.verticalLayoutWidget_6)
        self.label_25.setObjectName(_fromUtf8("label_25"))
        self.gridLayout_7.addWidget(self.label_25, 3, 0, 1, 1)
        self.label_18 = QtGui.QLabel(self.verticalLayoutWidget_6)
        self.label_18.setObjectName(_fromUtf8("label_18"))
        self.gridLayout_7.addWidget(self.label_18, 1, 0, 1, 1)
        self.comboBox_7 = QtGui.QComboBox(self.verticalLayoutWidget_6)
        self.comboBox_7.setObjectName(_fromUtf8("comboBox_7"))
        self.comboBox_7.addItem(_fromUtf8(""))
        self.comboBox_7.addItem(_fromUtf8(""))
        self.gridLayout_7.addWidget(self.comboBox_7, 1, 1, 1, 1)
        self.label_17 = QtGui.QLabel(self.verticalLayoutWidget_6)
        self.label_17.setObjectName(_fromUtf8("label_17"))
        self.gridLayout_7.addWidget(self.label_17, 0, 0, 1, 1)
        self.label_19 = QtGui.QLabel(self.verticalLayoutWidget_6)
        self.label_19.setObjectName(_fromUtf8("label_19"))
        self.gridLayout_7.addWidget(self.label_19, 2, 0, 1, 1)
        self.comboBox_6 = QtGui.QComboBox(self.verticalLayoutWidget_6)
        self.comboBox_6.setObjectName(_fromUtf8("comboBox_6"))
        self.comboBox_6.addItem(_fromUtf8(""))
        self.comboBox_6.addItem(_fromUtf8(""))
        self.gridLayout_7.addWidget(self.comboBox_6, 0, 1, 1, 1)
        self.spinBox = QtGui.QSpinBox(self.verticalLayoutWidget_6)
        self.spinBox.setMinimum(-9)
        self.spinBox.setMaximum(1)
        self.spinBox.setProperty("value", -3)
        self.spinBox.setObjectName(_fromUtf8("spinBox"))
        self.gridLayout_7.addWidget(self.spinBox, 3, 1, 1, 1)
        self.comboBox_8 = QtGui.QComboBox(self.verticalLayoutWidget_6)
        self.comboBox_8.setEditable(True)
        self.comboBox_8.setObjectName(_fromUtf8("comboBox_8"))
        self.comboBox_8.addItem(_fromUtf8(""))
        self.comboBox_8.addItem(_fromUtf8(""))
        self.comboBox_8.addItem(_fromUtf8(""))
        self.comboBox_8.addItem(_fromUtf8(""))
        self.gridLayout_7.addWidget(self.comboBox_8, 2, 1, 1, 1)
        self.verticalLayout_5.addLayout(self.gridLayout_7)
        self.stackedWidget.addWidget(self.page_keithley)
        self.page_deposition = QtGui.QWidget()
        self.page_deposition.setObjectName(_fromUtf8("page_deposition"))
        self.verticalLayoutWidget_10 = QtGui.QWidget(self.page_deposition)
        self.verticalLayoutWidget_10.setGeometry(QtCore.QRect(20, 30, 421, 161))
        self.verticalLayoutWidget_10.setObjectName(_fromUtf8("verticalLayoutWidget_10"))
        self.verticalLayout_8 = QtGui.QVBoxLayout(self.verticalLayoutWidget_10)
        self.verticalLayout_8.setObjectName(_fromUtf8("verticalLayout_8"))
        self.gridLayout_9 = QtGui.QGridLayout()
        self.gridLayout_9.setObjectName(_fromUtf8("gridLayout_9"))
        self.label_29 = QtGui.QLabel(self.verticalLayoutWidget_10)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_29.setFont(font)
        self.label_29.setObjectName(_fromUtf8("label_29"))
        self.gridLayout_9.addWidget(self.label_29, 0, 0, 1, 1)
        self.checkBoxQCM1 = QtGui.QCheckBox(self.verticalLayoutWidget_10)
        self.checkBoxQCM1.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.checkBoxQCM1.setAutoFillBackground(False)
        self.checkBoxQCM1.setChecked(True)
        self.checkBoxQCM1.setObjectName(_fromUtf8("checkBoxQCM1"))
        self.gridLayout_9.addWidget(self.checkBoxQCM1, 0, 1, 1, 1)
        self.checkBoxQCM2 = QtGui.QCheckBox(self.verticalLayoutWidget_10)
        self.checkBoxQCM2.setChecked(True)
        self.checkBoxQCM2.setObjectName(_fromUtf8("checkBoxQCM2"))
        self.gridLayout_9.addWidget(self.checkBoxQCM2, 1, 1, 1, 1)
        self.checkBoxQCM3 = QtGui.QCheckBox(self.verticalLayoutWidget_10)
        self.checkBoxQCM3.setObjectName(_fromUtf8("checkBoxQCM3"))
        self.gridLayout_9.addWidget(self.checkBoxQCM3, 2, 1, 1, 1)
        self.checkBoxQCM4 = QtGui.QCheckBox(self.verticalLayoutWidget_10)
        self.checkBoxQCM4.setObjectName(_fromUtf8("checkBoxQCM4"))
        self.gridLayout_9.addWidget(self.checkBoxQCM4, 3, 1, 1, 1)
        self.verticalLayout_8.addLayout(self.gridLayout_9)
        self.gridLayoutWidget_2 = QtGui.QWidget(self.page_deposition)
        self.gridLayoutWidget_2.setGeometry(QtCore.QRect(20, 220, 421, 80))
        self.gridLayoutWidget_2.setObjectName(_fromUtf8("gridLayoutWidget_2"))
        self.gridLayout_8 = QtGui.QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_8.setObjectName(_fromUtf8("gridLayout_8"))
        self.label_26 = QtGui.QLabel(self.gridLayoutWidget_2)
        self.label_26.setObjectName(_fromUtf8("label_26"))
        self.gridLayout_8.addWidget(self.label_26, 0, 0, 1, 1)
        self.doubleSpinBox_5 = QtGui.QDoubleSpinBox(self.gridLayoutWidget_2)
        self.doubleSpinBox_5.setDecimals(1)
        self.doubleSpinBox_5.setMaximum(60.0)
        self.doubleSpinBox_5.setProperty("value", 1.0)
        self.doubleSpinBox_5.setObjectName(_fromUtf8("doubleSpinBox_5"))
        self.gridLayout_8.addWidget(self.doubleSpinBox_5, 0, 1, 1, 1)
        self.stackedWidget.addWidget(self.page_deposition)
        self.Substrate_page = QtGui.QWidget()
        self.Substrate_page.setObjectName(_fromUtf8("Substrate_page"))
        self.label_5 = QtGui.QLabel(self.Substrate_page)
        self.label_5.setGeometry(QtCore.QRect(130, 250, 181, 31))
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.stackedWidget.addWidget(self.Substrate_page)
        self.verticalLayout.addWidget(self.stackedWidget)
        self.verticalLayoutWidget_5 = QtGui.QWidget(self.tab)
        self.verticalLayoutWidget_5.setGeometry(QtCore.QRect(70, 30, 571, 141))
        self.verticalLayoutWidget_5.setObjectName(_fromUtf8("verticalLayoutWidget_5"))
        self.verticalLayout_4 = QtGui.QVBoxLayout(self.verticalLayoutWidget_5)
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
        self.gridLayout_6 = QtGui.QGridLayout()
        self.gridLayout_6.setObjectName(_fromUtf8("gridLayout_6"))
        self.label_21 = QtGui.QLabel(self.verticalLayoutWidget_5)
        self.label_21.setObjectName(_fromUtf8("label_21"))
        self.gridLayout_6.addWidget(self.label_21, 0, 0, 1, 1)
        self.label_23 = QtGui.QLabel(self.verticalLayoutWidget_5)
        self.label_23.setObjectName(_fromUtf8("label_23"))
        self.gridLayout_6.addWidget(self.label_23, 2, 0, 1, 1)
        self.lineEdit_2 = QtGui.QLineEdit(self.verticalLayoutWidget_5)
        self.lineEdit_2.setText(_fromUtf8(""))
        self.lineEdit_2.setObjectName(_fromUtf8("lineEdit_2"))
        self.gridLayout_6.addWidget(self.lineEdit_2, 0, 1, 1, 1)
        self.lineEdit_3 = QtGui.QLineEdit(self.verticalLayoutWidget_5)
        self.lineEdit_3.setObjectName(_fromUtf8("lineEdit_3"))
        self.gridLayout_6.addWidget(self.lineEdit_3, 2, 1, 1, 1)
        self.gridLayout_2 = QtGui.QGridLayout()
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.lineEditSave = QtGui.QLineEdit(self.verticalLayoutWidget_5)
        self.lineEditSave.setText(_fromUtf8(""))
        self.lineEditSave.setReadOnly(False)
        self.lineEditSave.setObjectName(_fromUtf8("lineEditSave"))
        self.gridLayout_2.addWidget(self.lineEditSave, 0, 0, 1, 1)
        self.checkBoxSave = QtGui.QCheckBox(self.verticalLayoutWidget_5)
        self.checkBoxSave.setChecked(True)
        self.checkBoxSave.setObjectName(_fromUtf8("checkBoxSave"))
        self.gridLayout_2.addWidget(self.checkBoxSave, 0, 2, 1, 1)
        self.pushButtonSave = QtGui.QPushButton(self.verticalLayoutWidget_5)
        self.pushButtonSave.setObjectName(_fromUtf8("pushButtonSave"))
        self.gridLayout_2.addWidget(self.pushButtonSave, 0, 1, 1, 1)
        self.gridLayout_6.addLayout(self.gridLayout_2, 3, 1, 1, 1)
        self.label_24 = QtGui.QLabel(self.verticalLayoutWidget_5)
        self.label_24.setObjectName(_fromUtf8("label_24"))
        self.gridLayout_6.addWidget(self.label_24, 3, 0, 1, 1)
        self.verticalLayout_4.addLayout(self.gridLayout_6)
        self.horizontalLayoutWidget = QtGui.QWidget(self.tab)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(150, 800, 403, 41))
        self.horizontalLayoutWidget.setObjectName(_fromUtf8("horizontalLayoutWidget"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.pushButton_save = QtGui.QPushButton(self.horizontalLayoutWidget)
        self.pushButton_save.setObjectName(_fromUtf8("pushButton_save"))
        self.horizontalLayout.addWidget(self.pushButton_save)
        self.pushButton_load = QtGui.QPushButton(self.horizontalLayoutWidget)
        self.pushButton_load.setObjectName(_fromUtf8("pushButton_load"))
        self.horizontalLayout.addWidget(self.pushButton_load)
        self.verticalLayoutWidget_5.raise_()
        self.horizontalLayoutWidget.raise_()
        self.groupBox.raise_()
        self.tabWidget.addTab(self.tab, _fromUtf8(""))
        self.tab_2 = QtGui.QWidget()
        self.tab_2.setObjectName(_fromUtf8("tab_2"))
        self.verticalLayoutWidget = QtGui.QWidget(self.tab_2)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 10, 691, 521))
        self.verticalLayoutWidget.setObjectName(_fromUtf8("verticalLayoutWidget"))
        self.plotLayout = QtGui.QVBoxLayout(self.verticalLayoutWidget)
        self.plotLayout.setObjectName(_fromUtf8("plotLayout"))
        self.pltWidget = MatplotlibWidget(self.verticalLayoutWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pltWidget.sizePolicy().hasHeightForWidth())
        self.pltWidget.setSizePolicy(sizePolicy)
        self.pltWidget.setObjectName(_fromUtf8("pltWidget"))
        self.plotLayout.addWidget(self.pltWidget)
        self.groupBox_2 = QtGui.QGroupBox(self.tab_2)
        self.groupBox_2.setGeometry(QtCore.QRect(10, 550, 691, 191))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.groupBox_2.setFont(font)
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.plainTextEdit = QtGui.QPlainTextEdit(self.groupBox_2)
        self.plainTextEdit.setGeometry(QtCore.QRect(0, 30, 681, 211))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        self.plainTextEdit.setFont(font)
        self.plainTextEdit.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.plainTextEdit.setFrameShape(QtGui.QFrame.NoFrame)
        self.plainTextEdit.setObjectName(_fromUtf8("plainTextEdit"))
        self.gridLayoutWidget = QtGui.QWidget(self.tab_2)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(180, 810, 321, 71))
        self.gridLayoutWidget.setObjectName(_fromUtf8("gridLayoutWidget"))
        self.gridLayout = QtGui.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.button_cancel1 = QtGui.QPushButton(self.gridLayoutWidget)
        self.button_cancel1.setObjectName(_fromUtf8("button_cancel1"))
        self.gridLayout.addWidget(self.button_cancel1, 0, 1, 1, 1)
        self.button_1 = QtGui.QPushButton(self.gridLayoutWidget)
        self.button_1.setObjectName(_fromUtf8("button_1"))
        self.gridLayout.addWidget(self.button_1, 0, 0, 1, 1)
        self.tabWidget.addTab(self.tab_2, _fromUtf8(""))
        self.tab_3 = QtGui.QWidget()
        self.tab_3.setObjectName(_fromUtf8("tab_3"))
        self.verticalLayoutWidget_7 = QtGui.QWidget(self.tab_3)
        self.verticalLayoutWidget_7.setGeometry(QtCore.QRect(10, 10, 691, 521))
        self.verticalLayoutWidget_7.setObjectName(_fromUtf8("verticalLayoutWidget_7"))
        self.plotLayout_2 = QtGui.QVBoxLayout(self.verticalLayoutWidget_7)
        self.plotLayout_2.setObjectName(_fromUtf8("plotLayout_2"))
        self.pltWidget_2 = MatplotlibWidget(self.verticalLayoutWidget_7)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pltWidget_2.sizePolicy().hasHeightForWidth())
        self.pltWidget_2.setSizePolicy(sizePolicy)
        self.pltWidget_2.setObjectName(_fromUtf8("pltWidget_2"))
        self.plotLayout_2.addWidget(self.pltWidget_2)
        self.verticalLayoutWidget_9 = QtGui.QWidget(self.tab_3)
        self.verticalLayoutWidget_9.setGeometry(QtCore.QRect(10, 610, 691, 171))
        self.verticalLayoutWidget_9.setObjectName(_fromUtf8("verticalLayoutWidget_9"))
        self.verticalLayout_7 = QtGui.QVBoxLayout(self.verticalLayoutWidget_9)
        self.verticalLayout_7.setObjectName(_fromUtf8("verticalLayout_7"))
        self.label_28 = QtGui.QLabel(self.verticalLayoutWidget_9)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_28.setFont(font)
        self.label_28.setObjectName(_fromUtf8("label_28"))
        self.verticalLayout_7.addWidget(self.label_28)
        self.plainTextEdit_2 = QtGui.QPlainTextEdit(self.verticalLayoutWidget_9)
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        self.plainTextEdit_2.setFont(font)
        self.plainTextEdit_2.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.plainTextEdit_2.setFrameShape(QtGui.QFrame.NoFrame)
        self.plainTextEdit_2.setObjectName(_fromUtf8("plainTextEdit_2"))
        self.verticalLayout_7.addWidget(self.plainTextEdit_2)
        self.verticalLayoutWidget_8 = QtGui.QWidget(self.tab_3)
        self.verticalLayoutWidget_8.setGeometry(QtCore.QRect(10, 540, 691, 61))
        self.verticalLayoutWidget_8.setObjectName(_fromUtf8("verticalLayoutWidget_8"))
        self.verticalLayout_6 = QtGui.QVBoxLayout(self.verticalLayoutWidget_8)
        self.verticalLayout_6.setObjectName(_fromUtf8("verticalLayout_6"))
        self.label_4 = QtGui.QLabel(self.verticalLayoutWidget_8)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.verticalLayout_6.addWidget(self.label_4)
        self.comboBoxQCM_Display = QtGui.QComboBox(self.verticalLayoutWidget_8)
        self.comboBoxQCM_Display.setObjectName(_fromUtf8("comboBoxQCM_Display"))
        self.comboBoxQCM_Display.addItem(_fromUtf8(""))
        self.comboBoxQCM_Display.addItem(_fromUtf8(""))
        self.verticalLayout_6.addWidget(self.comboBoxQCM_Display)
        self.horizontalLayoutWidget_2 = QtGui.QWidget(self.tab_3)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(190, 810, 321, 71))
        self.horizontalLayoutWidget_2.setObjectName(_fromUtf8("horizontalLayoutWidget_2"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.pushButton_QCMStart = QtGui.QPushButton(self.horizontalLayoutWidget_2)
        self.pushButton_QCMStart.setObjectName(_fromUtf8("pushButton_QCMStart"))
        self.horizontalLayout_2.addWidget(self.pushButton_QCMStart)
        self.pushButton_QCMStop = QtGui.QPushButton(self.horizontalLayoutWidget_2)
        self.pushButton_QCMStop.setObjectName(_fromUtf8("pushButton_QCMStop"))
        self.horizontalLayout_2.addWidget(self.pushButton_QCMStop)
        self.tabWidget.addTab(self.tab_3, _fromUtf8(""))
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusBar = QtGui.QStatusBar(MainWindow)
        self.statusBar.setObjectName(_fromUtf8("statusBar"))
        MainWindow.setStatusBar(self.statusBar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        self.comboBox_Measurement.setCurrentIndex(0)
        self.stackedWidget.setCurrentIndex(0)
        self.comboBox_8.setCurrentIndex(2)
        QtCore.QObject.connect(self.comboBox_Measurement, QtCore.SIGNAL(_fromUtf8("currentIndexChanged(int)")), self.stackedWidget.setCurrentIndex)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "transistor tools", None))
        self.groupBox.setTitle(_translate("MainWindow", "Measurement Controls", None))
        self.comboBox_Measurement.setItemText(0, _translate("MainWindow", "IV Measurement", None))
        self.comboBox_Measurement.setItemText(1, _translate("MainWindow", "Keithley Setup", None))
        self.comboBox_Measurement.setItemText(2, _translate("MainWindow", "Deposition Control", None))
        self.comboBox_Measurement.setItemText(3, _translate("MainWindow", "Substrate Heating Control", None))
        self.label_6.setText(_translate("MainWindow", "Fixed Voltage Measurement", None))
        self.checkBox_fixedV.setAccessibleName(_translate("MainWindow", "takefixedV", None))
        self.checkBox_fixedV.setText(_translate("MainWindow", "Take fixed voltage measurements?", None))
        self.label.setText(_translate("MainWindow", "Voltage", None))
        self.label_2.setText(_translate("MainWindow", "Number of measurements", None))
        self.label_3.setText(_translate("MainWindow", "Pause Time", None))
        self.doubleSpinBox_Voltage.setAccessibleName(_translate("MainWindow", "fixedV", None))
        self.doubleSpinBox_Voltage.setSuffix(_translate("MainWindow", " V", None))
        self.doubleSpinBox_pauseTime.setAccessibleName(_translate("MainWindow", "pauseTime", None))
        self.doubleSpinBox_pauseTime.setSuffix(_translate("MainWindow", " s", None))
        self.spinBox_nRepeats.setAccessibleName(_translate("MainWindow", "nRepeats", None))
        self.label_7.setText(_translate("MainWindow", "IV Sweep", None))
        self.checkBox_IV.setAccessibleName(_translate("MainWindow", "takeIVsweep", None))
        self.checkBox_IV.setText(_translate("MainWindow", "Take an IV sweep?", None))
        self.doubleSpinBox_4.setAccessibleName(_translate("MainWindow", "holdTime", None))
        self.doubleSpinBox_4.setSuffix(_translate("MainWindow", " s", None))
        self.label_11.setText(_translate("MainWindow", "Step Time", None))
        self.label_10.setAccessibleName(_translate("MainWindow", "Vstep", None))
        self.label_10.setText(_translate("MainWindow", "Voltage Step", None))
        self.doubleSpinBox_3.setAccessibleName(_translate("MainWindow", "stepSize", None))
        self.doubleSpinBox_2.setAccessibleName(_translate("MainWindow", "finalV", None))
        self.doubleSpinBox_2.setSuffix(_translate("MainWindow", " V", None))
        self.label_8.setText(_translate("MainWindow", "Initial Voltage", None))
        self.label_9.setText(_translate("MainWindow", "Final Voltage", None))
        self.doubleSpinBox.setAccessibleName(_translate("MainWindow", "initialV", None))
        self.doubleSpinBox.setSuffix(_translate("MainWindow", " V", None))
        self.label_22.setText(_translate("MainWindow", "Connection", None))
        self.label_12.setText(_translate("MainWindow", "Connection type", None))
        self.label_13.setText(_translate("MainWindow", "Baud Rate", None))
        self.comboBox_2.setAccessibleName(_translate("MainWindow", "serAdapt", None))
        self.comboBox_2.setItemText(0, _translate("MainWindow", "USB", None))
        self.label_16.setText(_translate("MainWindow", "Serial Ad", None))
        self.label_14.setText(_translate("MainWindow", "Term Character", None))
        self.comboBox_3.setAccessibleName(_translate("MainWindow", "baudR", None))
        self.comboBox_3.setItemText(0, _translate("MainWindow", "57600", None))
        self.comboBox.setAccessibleName(_translate("MainWindow", "connectionType", None))
        self.comboBox.setItemText(0, _translate("MainWindow", "Serial", None))
        self.comboBox.setItemText(1, _translate("MainWindow", "GPIB", None))
        self.comboBox.setItemText(2, _translate("MainWindow", "Other", None))
        self.comboBox_4.setAccessibleName(_translate("MainWindow", "termChar", None))
        self.comboBox_4.setItemText(0, _translate("MainWindow", "\\r", None))
        self.label_15.setText(_translate("MainWindow", "Serial Adapter", None))
        self.comboBox_5.setAccessibleName(_translate("MainWindow", "serAd", None))
        self.comboBox_5.setItemText(0, _translate("MainWindow", "0", None))
        self.label_20.setText(_translate("MainWindow", "Keithley Parameters", None))
        self.label_25.setText(_translate("MainWindow", "Compliance", None))
        self.label_18.setText(_translate("MainWindow", "Four-wire", None))
        self.comboBox_7.setAccessibleName(_translate("MainWindow", "4wire", None))
        self.comboBox_7.setItemText(0, _translate("MainWindow", "Off", None))
        self.comboBox_7.setItemText(1, _translate("MainWindow", "On", None))
        self.label_17.setText(_translate("MainWindow", "Terminals", None))
        self.label_19.setText(_translate("MainWindow", "Integration Time", None))
        self.comboBox_6.setAccessibleName(_translate("MainWindow", "route", None))
        self.comboBox_6.setItemText(0, _translate("MainWindow", "Front", None))
        self.comboBox_6.setItemText(1, _translate("MainWindow", "Rear", None))
        self.spinBox.setAccessibleName(_translate("MainWindow", "compliance", None))
        self.spinBox.setSuffix(_translate("MainWindow", " A", None))
        self.spinBox.setPrefix(_translate("MainWindow", "1 x 10^", None))
        self.comboBox_8.setAccessibleName(_translate("MainWindow", "integrationTime", None))
        self.comboBox_8.setItemText(0, _translate("MainWindow", "0.01", None))
        self.comboBox_8.setItemText(1, _translate("MainWindow", "0.1", None))
        self.comboBox_8.setItemText(2, _translate("MainWindow", "1", None))
        self.comboBox_8.setItemText(3, _translate("MainWindow", "10", None))
        self.label_29.setText(_translate("MainWindow", "QCM Channels to monitor:", None))
        self.checkBoxQCM1.setAccessibleName(_translate("MainWindow", "QCM1", None))
        self.checkBoxQCM1.setText(_translate("MainWindow", "Channel 1", None))
        self.checkBoxQCM2.setAccessibleName(_translate("MainWindow", "QCM2", None))
        self.checkBoxQCM2.setText(_translate("MainWindow", "Channel 2", None))
        self.checkBoxQCM3.setAccessibleName(_translate("MainWindow", "QCM3", None))
        self.checkBoxQCM3.setText(_translate("MainWindow", "Channel 3", None))
        self.checkBoxQCM4.setAccessibleName(_translate("MainWindow", "QCM4", None))
        self.checkBoxQCM4.setText(_translate("MainWindow", "Channel 4", None))
        self.label_26.setText(_translate("MainWindow", "Sample time", None))
        self.doubleSpinBox_5.setAccessibleName(_translate("MainWindow", "QCM_sampleTime", None))
        self.label_5.setText(_translate("MainWindow", "Feature coming soon...", None))
        self.label_21.setText(_translate("MainWindow", "Experiment Name", None))
        self.label_23.setText(_translate("MainWindow", "Sample", None))
        self.lineEdit_2.setAccessibleName(_translate("MainWindow", "exp_name", None))
        self.lineEdit_2.setPlaceholderText(_translate("MainWindow", "< Type of Measurement >", None))
        self.lineEdit_3.setAccessibleName(_translate("MainWindow", "sample", None))
        self.lineEdit_3.setPlaceholderText(_translate("MainWindow", "< Sample name >", None))
        self.lineEditSave.setAccessibleName(_translate("MainWindow", "sav_loc", None))
        self.lineEditSave.setPlaceholderText(_translate("MainWindow", "<save directory>", None))
        self.checkBoxSave.setAccessibleName(_translate("MainWindow", "saveData", None))
        self.checkBoxSave.setText(_translate("MainWindow", "Save data", None))
        self.pushButtonSave.setText(_translate("MainWindow", "Browse", None))
        self.label_24.setText(_translate("MainWindow", "Save Location", None))
        self.pushButton_save.setAccessibleName(_translate("MainWindow", "saveSettings", None))
        self.pushButton_save.setText(_translate("MainWindow", "Save Settings", None))
        self.pushButton_load.setAccessibleName(_translate("MainWindow", "loadSettings", None))
        self.pushButton_load.setText(_translate("MainWindow", "Load Settings", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Setup", None))
        self.groupBox_2.setTitle(_translate("MainWindow", "Console:", None))
        self.button_cancel1.setText(_translate("MainWindow", "ABORT", None))
        self.button_1.setText(_translate("MainWindow", "START", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Electrical Measurements", None))
        self.label_28.setText(_translate("MainWindow", "Console:", None))
        self.label_4.setText(_translate("MainWindow", "Display:", None))
        self.comboBoxQCM_Display.setAccessibleName(_translate("MainWindow", "QCM_display", None))
        self.comboBoxQCM_Display.setItemText(0, _translate("MainWindow", "Thickness", None))
        self.comboBoxQCM_Display.setItemText(1, _translate("MainWindow", "Rates", None))
        self.pushButton_QCMStart.setText(_translate("MainWindow", "Record", None))
        self.pushButton_QCMStop.setText(_translate("MainWindow", "Stop and Save", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("MainWindow", "Deposition Monitor", None))

from src.matplotlibwidget import MatplotlibWidget