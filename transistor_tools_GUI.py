# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'transistor_tools_GUII.ui'
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
        MainWindow.resize(639, 921)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.tabWidget = QtGui.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(10, 10, 621, 851))
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.tab = QtGui.QWidget()
        self.tab.setObjectName(_fromUtf8("tab"))
        self.gridLayoutWidget_2 = QtGui.QWidget(self.tab)
        self.gridLayoutWidget_2.setGeometry(QtCore.QRect(20, 40, 561, 61))
        self.gridLayoutWidget_2.setObjectName(_fromUtf8("gridLayoutWidget_2"))
        self.gridLayout_2 = QtGui.QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.lineEditSave = QtGui.QLineEdit(self.gridLayoutWidget_2)
        self.lineEditSave.setObjectName(_fromUtf8("lineEditSave"))
        self.gridLayout_2.addWidget(self.lineEditSave, 0, 0, 1, 1)
        self.checkBoxSave = QtGui.QCheckBox(self.gridLayoutWidget_2)
        self.checkBoxSave.setObjectName(_fromUtf8("checkBoxSave"))
        self.gridLayout_2.addWidget(self.checkBoxSave, 0, 2, 1, 1)
        self.pushButtonSave = QtGui.QPushButton(self.gridLayoutWidget_2)
        self.pushButtonSave.setObjectName(_fromUtf8("pushButtonSave"))
        self.gridLayout_2.addWidget(self.pushButtonSave, 0, 1, 1, 1)
        self.groupBox = QtGui.QGroupBox(self.tab)
        self.groupBox.setGeometry(QtCore.QRect(60, 140, 509, 581))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.verticalLayoutWidget_2 = QtGui.QWidget(self.groupBox)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(20, 30, 461, 551))
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
        self.checkBox = QtGui.QCheckBox(self.verticalLayoutWidget_3)
        self.checkBox.setChecked(True)
        self.checkBox.setObjectName(_fromUtf8("checkBox"))
        self.verticalLayout_2.addWidget(self.checkBox)
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
        self.checkBox_2 = QtGui.QCheckBox(self.verticalLayoutWidget_4)
        self.checkBox_2.setChecked(True)
        self.checkBox_2.setObjectName(_fromUtf8("checkBox_2"))
        self.verticalLayout_3.addWidget(self.checkBox_2)
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
        self.gridLayoutWidget_3 = QtGui.QWidget(self.page_keithley)
        self.gridLayoutWidget_3.setGeometry(QtCore.QRect(20, 20, 421, 234))
        self.gridLayoutWidget_3.setObjectName(_fromUtf8("gridLayoutWidget_3"))
        self.gridLayout_5 = QtGui.QGridLayout(self.gridLayoutWidget_3)
        self.gridLayout_5.setObjectName(_fromUtf8("gridLayout_5"))
        self.label_13 = QtGui.QLabel(self.gridLayoutWidget_3)
        self.label_13.setObjectName(_fromUtf8("label_13"))
        self.gridLayout_5.addWidget(self.label_13, 3, 0, 1, 1)
        self.label_12 = QtGui.QLabel(self.gridLayoutWidget_3)
        self.label_12.setObjectName(_fromUtf8("label_12"))
        self.gridLayout_5.addWidget(self.label_12, 0, 0, 1, 1)
        self.comboBox_2 = QtGui.QComboBox(self.gridLayoutWidget_3)
        self.comboBox_2.setObjectName(_fromUtf8("comboBox_2"))
        self.comboBox_2.addItem(_fromUtf8(""))
        self.gridLayout_5.addWidget(self.comboBox_2, 1, 1, 1, 1)
        self.label_16 = QtGui.QLabel(self.gridLayoutWidget_3)
        self.label_16.setObjectName(_fromUtf8("label_16"))
        self.gridLayout_5.addWidget(self.label_16, 2, 0, 1, 1)
        self.comboBox_5 = QtGui.QComboBox(self.gridLayoutWidget_3)
        self.comboBox_5.setObjectName(_fromUtf8("comboBox_5"))
        self.comboBox_5.addItem(_fromUtf8(""))
        self.gridLayout_5.addWidget(self.comboBox_5, 2, 1, 1, 1)
        self.label_17 = QtGui.QLabel(self.gridLayoutWidget_3)
        self.label_17.setObjectName(_fromUtf8("label_17"))
        self.gridLayout_5.addWidget(self.label_17, 5, 0, 1, 1)
        self.label_14 = QtGui.QLabel(self.gridLayoutWidget_3)
        self.label_14.setObjectName(_fromUtf8("label_14"))
        self.gridLayout_5.addWidget(self.label_14, 4, 0, 1, 1)
        self.comboBox_3 = QtGui.QComboBox(self.gridLayoutWidget_3)
        self.comboBox_3.setObjectName(_fromUtf8("comboBox_3"))
        self.comboBox_3.addItem(_fromUtf8(""))
        self.gridLayout_5.addWidget(self.comboBox_3, 3, 1, 1, 1)
        self.comboBox = QtGui.QComboBox(self.gridLayoutWidget_3)
        self.comboBox.setObjectName(_fromUtf8("comboBox"))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.gridLayout_5.addWidget(self.comboBox, 0, 1, 1, 1)
        self.comboBox_4 = QtGui.QComboBox(self.gridLayoutWidget_3)
        self.comboBox_4.setObjectName(_fromUtf8("comboBox_4"))
        self.comboBox_4.addItem(_fromUtf8(""))
        self.gridLayout_5.addWidget(self.comboBox_4, 4, 1, 1, 1)
        self.label_15 = QtGui.QLabel(self.gridLayoutWidget_3)
        self.label_15.setObjectName(_fromUtf8("label_15"))
        self.gridLayout_5.addWidget(self.label_15, 1, 0, 1, 1)
        self.label_18 = QtGui.QLabel(self.gridLayoutWidget_3)
        self.label_18.setObjectName(_fromUtf8("label_18"))
        self.gridLayout_5.addWidget(self.label_18, 6, 0, 1, 1)
        self.comboBox_6 = QtGui.QComboBox(self.gridLayoutWidget_3)
        self.comboBox_6.setObjectName(_fromUtf8("comboBox_6"))
        self.comboBox_6.addItem(_fromUtf8(""))
        self.comboBox_6.addItem(_fromUtf8(""))
        self.gridLayout_5.addWidget(self.comboBox_6, 5, 1, 1, 1)
        self.comboBox_7 = QtGui.QComboBox(self.gridLayoutWidget_3)
        self.comboBox_7.setObjectName(_fromUtf8("comboBox_7"))
        self.comboBox_7.addItem(_fromUtf8(""))
        self.comboBox_7.addItem(_fromUtf8(""))
        self.gridLayout_5.addWidget(self.comboBox_7, 6, 1, 1, 1)
        self.stackedWidget.addWidget(self.page_keithley)
        self.page_deposition = QtGui.QWidget()
        self.page_deposition.setObjectName(_fromUtf8("page_deposition"))
        self.label_4 = QtGui.QLabel(self.page_deposition)
        self.label_4.setGeometry(QtCore.QRect(130, 240, 191, 41))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.stackedWidget.addWidget(self.page_deposition)
        self.Substrate_page = QtGui.QWidget()
        self.Substrate_page.setObjectName(_fromUtf8("Substrate_page"))
        self.label_5 = QtGui.QLabel(self.Substrate_page)
        self.label_5.setGeometry(QtCore.QRect(130, 250, 181, 31))
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.stackedWidget.addWidget(self.Substrate_page)
        self.verticalLayout.addWidget(self.stackedWidget)
        self.horizontalLayoutWidget = QtGui.QWidget(self.tab)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(100, 750, 403, 41))
        self.horizontalLayoutWidget.setObjectName(_fromUtf8("horizontalLayoutWidget"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.pushButton_save = QtGui.QPushButton(self.horizontalLayoutWidget)
        self.pushButton_save.setObjectName(_fromUtf8("pushButton_save"))
        self.horizontalLayout.addWidget(self.pushButton_save)
        self.pushButton_load = QtGui.QPushButton(self.horizontalLayoutWidget)
        self.pushButton_load.setObjectName(_fromUtf8("pushButton_load"))
        self.horizontalLayout.addWidget(self.pushButton_load)
        self.tabWidget.addTab(self.tab, _fromUtf8(""))
        self.tab_2 = QtGui.QWidget()
        self.tab_2.setObjectName(_fromUtf8("tab_2"))
        self.verticalLayoutWidget = QtGui.QWidget(self.tab_2)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(30, 30, 561, 371))
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
        self.groupBox_2.setGeometry(QtCore.QRect(50, 420, 521, 231))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.groupBox_2.setFont(font)
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.plainTextEdit = QtGui.QPlainTextEdit(self.groupBox_2)
        self.plainTextEdit.setGeometry(QtCore.QRect(0, 30, 491, 201))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        self.plainTextEdit.setFont(font)
        self.plainTextEdit.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.plainTextEdit.setFrameShape(QtGui.QFrame.NoFrame)
        self.plainTextEdit.setObjectName(_fromUtf8("plainTextEdit"))
        self.gridLayoutWidget = QtGui.QWidget(self.tab_2)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(150, 670, 292, 121))
        self.gridLayoutWidget.setObjectName(_fromUtf8("gridLayoutWidget"))
        self.gridLayout = QtGui.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.button_2 = QtGui.QPushButton(self.gridLayoutWidget)
        self.button_2.setObjectName(_fromUtf8("button_2"))
        self.gridLayout.addWidget(self.button_2, 1, 0, 1, 1)
        self.button_cancel2 = QtGui.QPushButton(self.gridLayoutWidget)
        self.button_cancel2.setObjectName(_fromUtf8("button_cancel2"))
        self.gridLayout.addWidget(self.button_cancel2, 1, 1, 1, 1)
        self.button_cancel1 = QtGui.QPushButton(self.gridLayoutWidget)
        self.button_cancel1.setObjectName(_fromUtf8("button_cancel1"))
        self.gridLayout.addWidget(self.button_cancel1, 0, 1, 1, 1)
        self.button_1 = QtGui.QPushButton(self.gridLayoutWidget)
        self.button_1.setObjectName(_fromUtf8("button_1"))
        self.gridLayout.addWidget(self.button_1, 0, 0, 1, 1)
        self.tabWidget.addTab(self.tab_2, _fromUtf8(""))
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusBar = QtGui.QStatusBar(MainWindow)
        self.statusBar.setObjectName(_fromUtf8("statusBar"))
        MainWindow.setStatusBar(self.statusBar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        self.comboBox_Measurement.setCurrentIndex(0)
        self.stackedWidget.setCurrentIndex(0)
        QtCore.QObject.connect(self.comboBox_Measurement, QtCore.SIGNAL(_fromUtf8("currentIndexChanged(int)")), self.stackedWidget.setCurrentIndex)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "Transistor Tools", None))
        self.lineEditSave.setAccessibleName(_translate("MainWindow", "sav_loc", None))
        self.lineEditSave.setPlaceholderText(_translate("MainWindow", "<save directory>", None))
        self.checkBoxSave.setText(_translate("MainWindow", "Save data", None))
        self.pushButtonSave.setText(_translate("MainWindow", "Browse", None))
        self.groupBox.setTitle(_translate("MainWindow", "Measurement Controls", None))
        self.comboBox_Measurement.setItemText(0, _translate("MainWindow", "IV Measurement", None))
        self.comboBox_Measurement.setItemText(1, _translate("MainWindow", "Keithley Setup", None))
        self.comboBox_Measurement.setItemText(2, _translate("MainWindow", "Deposition Control", None))
        self.comboBox_Measurement.setItemText(3, _translate("MainWindow", "Substrate Heating Control", None))
        self.label_6.setText(_translate("MainWindow", "Fixed Voltage Measurement", None))
        self.checkBox.setAccessibleName(_translate("MainWindow", "takefixedV", None))
        self.checkBox.setText(_translate("MainWindow", "Take fixed voltage measurements?", None))
        self.label.setText(_translate("MainWindow", "Voltage", None))
        self.label_2.setText(_translate("MainWindow", "Number of measurements", None))
        self.label_3.setText(_translate("MainWindow", "Pause Time", None))
        self.doubleSpinBox_Voltage.setAccessibleName(_translate("MainWindow", "fixedV", None))
        self.doubleSpinBox_Voltage.setSuffix(_translate("MainWindow", " V", None))
        self.doubleSpinBox_pauseTime.setAccessibleName(_translate("MainWindow", "pauseTime", None))
        self.doubleSpinBox_pauseTime.setSuffix(_translate("MainWindow", " s", None))
        self.spinBox_nRepeats.setAccessibleName(_translate("MainWindow", "nRepeats", None))
        self.label_7.setText(_translate("MainWindow", "IV Sweep", None))
        self.checkBox_2.setAccessibleName(_translate("MainWindow", "takeIVsweep", None))
        self.checkBox_2.setText(_translate("MainWindow", "Take an IV sweep?", None))
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
        self.label_13.setText(_translate("MainWindow", "Baud Rate", None))
        self.label_12.setText(_translate("MainWindow", "Connection type", None))
        self.comboBox_2.setAccessibleName(_translate("MainWindow", "serAdapt", None))
        self.comboBox_2.setItemText(0, _translate("MainWindow", "USB", None))
        self.label_16.setAccessibleName(_translate("MainWindow", "serAd", None))
        self.label_16.setText(_translate("MainWindow", "Serial Ad", None))
        self.comboBox_5.setAccessibleName(_translate("MainWindow", "serAd", None))
        self.comboBox_5.setItemText(0, _translate("MainWindow", "0", None))
        self.label_17.setText(_translate("MainWindow", "Route", None))
        self.label_14.setText(_translate("MainWindow", "Term Character", None))
        self.comboBox_3.setAccessibleName(_translate("MainWindow", "baudR", None))
        self.comboBox_3.setItemText(0, _translate("MainWindow", "57600", None))
        self.comboBox.setAccessibleName(_translate("MainWindow", "connectionType", None))
        self.comboBox.setItemText(0, _translate("MainWindow", "Serial", None))
        self.comboBox.setItemText(1, _translate("MainWindow", "Other", None))
        self.comboBox_4.setAccessibleName(_translate("MainWindow", "termChar", None))
        self.comboBox_4.setItemText(0, _translate("MainWindow", "\\r", None))
        self.label_15.setText(_translate("MainWindow", "Serial Adapter", None))
        self.label_18.setText(_translate("MainWindow", "How many wires?", None))
        self.comboBox_6.setAccessibleName(_translate("MainWindow", "route", None))
        self.comboBox_6.setItemText(0, _translate("MainWindow", "Front", None))
        self.comboBox_6.setItemText(1, _translate("MainWindow", "Rear", None))
        self.comboBox_7.setAccessibleName(_translate("MainWindow", "4wire", None))
        self.comboBox_7.setItemText(0, _translate("MainWindow", "Off", None))
        self.comboBox_7.setItemText(1, _translate("MainWindow", "On", None))
        self.label_4.setText(_translate("MainWindow", "Feature coming soon...", None))
        self.label_5.setText(_translate("MainWindow", "Feature coming soon...", None))
        self.pushButton_save.setAccessibleName(_translate("MainWindow", "saveSettings", None))
        self.pushButton_save.setText(_translate("MainWindow", "Save Settings", None))
        self.pushButton_load.setAccessibleName(_translate("MainWindow", "loadSettings", None))
        self.pushButton_load.setText(_translate("MainWindow", "Load Settings", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Setup", None))
        self.groupBox_2.setTitle(_translate("MainWindow", "Console", None))
        self.button_2.setText(_translate("MainWindow", "Start_2", None))
        self.button_cancel2.setText(_translate("MainWindow", "Stop_2", None))
        self.button_cancel1.setText(_translate("MainWindow", "ABORT", None))
        self.button_1.setText(_translate("MainWindow", "START", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Run", None))

from matplotlibwidget import MatplotlibWidget
