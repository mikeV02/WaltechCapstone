# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'counter.ui'
#
# Created: Wed Mar 29 23:23:34 2017
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

class Ui_CounterDialog(object):
    def setupUi(self, CounterDialog):
        CounterDialog.setObjectName(_fromUtf8("CounterDialog"))
        CounterDialog.resize(194, 174)
        self.buttonBox = QtGui.QDialogButtonBox(CounterDialog)
        self.buttonBox.setGeometry(QtCore.QRect(30, 130, 121, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.label_3 = QtGui.QLabel(CounterDialog)
        self.label_3.setGeometry(QtCore.QRect(10, 10, 71, 20))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.lineEdit = QtGui.QLineEdit(CounterDialog)
        self.lineEdit.setGeometry(QtCore.QRect(70, 10, 101, 20))
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.label_7 = QtGui.QLabel(CounterDialog)
        self.label_7.setGeometry(QtCore.QRect(20, 70, 41, 16))
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.comboBox_2 = QtGui.QComboBox(CounterDialog)
        self.comboBox_2.setGeometry(QtCore.QRect(70, 70, 101, 22))
        self.comboBox_2.setEditable(True)
        self.comboBox_2.setObjectName(_fromUtf8("comboBox_2"))
        self.label_5 = QtGui.QLabel(CounterDialog)
        self.label_5.setGeometry(QtCore.QRect(10, 40, 51, 16))
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.spinBox = QtGui.QSpinBox(CounterDialog)
        self.spinBox.setGeometry(QtCore.QRect(70, 40, 91, 22))
        self.spinBox.setMaximum(65535)
        self.spinBox.setObjectName(_fromUtf8("spinBox"))
        self.label_9 = QtGui.QLabel(CounterDialog)
        self.label_9.setGeometry(QtCore.QRect(20, 100, 46, 13))
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.comboBox_3 = QtGui.QComboBox(CounterDialog)
        self.comboBox_3.setGeometry(QtCore.QRect(70, 100, 101, 22))
        self.comboBox_3.setObjectName(_fromUtf8("comboBox_3"))
        self.comboBox_3.addItem(_fromUtf8(""))
        self.comboBox_3.addItem(_fromUtf8(""))

        self.retranslateUi(CounterDialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), CounterDialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), CounterDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(CounterDialog)

    def retranslateUi(self, CounterDialog):
        CounterDialog.setWindowTitle(_translate("CounterDialog", "Counter Properties", None))
        self.label_3.setText(_translate("CounterDialog", "Comment:", None))
        self.label_7.setText(_translate("CounterDialog", "Name:", None))
        self.label_5.setToolTip(_translate("CounterDialog", "<html><head/><body><p>maximum: 65535</p></body></html>", None))
        self.label_5.setText(_translate("CounterDialog", "Setpoint", None))
        self.label_9.setText(_translate("CounterDialog", "Type:", None))
        self.comboBox_3.setItemText(0, _translate("CounterDialog", "Counter_Up", None))
        self.comboBox_3.setItemText(1, _translate("CounterDialog", "Counter_Down", None))
        
    def switchCombo(self):
        self.comboBox_3.setItemText(0, _translate("CounterDialog", "Counter_Down", None))
        self.comboBox_3.setItemText(1, _translate("CounterDialog", "Couter_Up", None))