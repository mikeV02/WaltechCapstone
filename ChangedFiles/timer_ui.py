# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'timer.ui'
#
# Created: Wed Mar 29 23:33:54 2017
#      by: PyQt4 UI code generator 4.11
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

class Ui_TimerDialog(object):
    def setupUi(self, TimerDialog):
        TimerDialog.setObjectName(_fromUtf8("TimerDialog"))
        TimerDialog.resize(184, 174)
        self.buttonBox = QtGui.QDialogButtonBox(TimerDialog)
        self.buttonBox.setGeometry(QtCore.QRect(30, 130, 121, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.label_3 = QtGui.QLabel(TimerDialog)
        self.label_3.setGeometry(QtCore.QRect(10, 10, 71, 20))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.lineEdit = QtGui.QLineEdit(TimerDialog)
        self.lineEdit.setGeometry(QtCore.QRect(70, 10, 101, 20))
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.label_5 = QtGui.QLabel(TimerDialog)
        self.label_5.setGeometry(QtCore.QRect(10, 40, 61, 21))
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.label_7 = QtGui.QLabel(TimerDialog)
        self.label_7.setGeometry(QtCore.QRect(10, 70, 41, 16))
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.comboBox_2 = QtGui.QComboBox(TimerDialog)
        self.comboBox_2.setGeometry(QtCore.QRect(70, 70, 101, 22))
        self.comboBox_2.setEditable(True)
        self.comboBox_2.setObjectName(_fromUtf8("comboBox_2"))
        self.doubleSpinBox = QtGui.QDoubleSpinBox(TimerDialog)
        self.doubleSpinBox.setGeometry(QtCore.QRect(80, 40, 91, 22))
        self.doubleSpinBox.setMinimum(0.01)
        self.doubleSpinBox.setMaximum(655.34)
        self.doubleSpinBox.setSingleStep(0.01)
        self.doubleSpinBox.setObjectName(_fromUtf8("doubleSpinBox"))
        self.label_9 = QtGui.QLabel(TimerDialog)
        self.label_9.setGeometry(QtCore.QRect(10, 100, 46, 13))
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.comboBox_3 = QtGui.QComboBox(TimerDialog)
        self.comboBox_3.setGeometry(QtCore.QRect(70, 100, 101, 22))
        self.comboBox_3.setObjectName(_fromUtf8("comboBox_3"))
        self.comboBox_3.addItem(_fromUtf8(""))
        self.comboBox_3.addItem(_fromUtf8(""))

        self.retranslateUi(TimerDialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), TimerDialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), TimerDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(TimerDialog)

    def retranslateUi(self, TimerDialog):
        TimerDialog.setWindowTitle(_translate("TimerDialog", "Timer Properties", None))
        self.label_3.setText(_translate("TimerDialog", "Comment:", None))
        self.label_5.setToolTip(_translate("TimerDialog", "<html><head/><body><p>10 min. max</p></body></html>", None))
        self.label_5.setText(_translate("TimerDialog", "Sec delay:", None))
        self.label_7.setText(_translate("TimerDialog", "Name:", None))
        self.doubleSpinBox.setToolTip(_translate("TimerDialog", "<html><head/><body><p>10 miniutes max</p></body></html>", None))
        self.label_9.setText(_translate("TimerDialog", "Type:", None))
        self.comboBox_3.setItemText(0, _translate("TimerDialog", "Timer_On_Delay", None))
        self.comboBox_3.setItemText(1, _translate("TimerDialog", "Retentive_Timer_On", None))

