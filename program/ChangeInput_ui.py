# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'coil.ui'
#
# Created by: PyQt4 UI code generator 4.12
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

class Ui_ChangeInputDialog(object):
    def setupUi(self, ChangeInputDialog):
        ChangeInputDialog.setObjectName(_fromUtf8("ChangeInputDialog"))
        ChangeInputDialog.resize(150, 150)
        self.gridLayout = QtGui.QGridLayout(ChangeInputDialog)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.warning_label = QtGui.QLabel(ChangeInputDialog)
        self.warning_label.setObjectName(_fromUtf8("warning_label"))
        self.gridLayout.addWidget(self.warning_label, 0, 0, 1, 0)
        self.previous_label = QtGui.QLabel(ChangeInputDialog)
        self.previous_label.setObjectName(_fromUtf8("previous_label"))
        self.gridLayout.addWidget(self.previous_label, 1, 0, 1, 1)
        self.p_label = QtGui.QLabel(ChangeInputDialog)
        self.p_label.setObjectName(_fromUtf8("p_label"))
        self.gridLayout.addWidget(self.p_label, 1, 1, 1, 1)
        self.new_label = QtGui.QLabel(ChangeInputDialog)
        self.new_label.setObjectName(_fromUtf8("new_label"))
        self.gridLayout.addWidget(self.new_label, 2, 0, 1, 1)
        self.n_label = QtGui.QLabel(ChangeInputDialog)
        self.n_label.setObjectName(_fromUtf8("n_label"))
        self.gridLayout.addWidget(self.n_label, 2, 1, 1, 1)
        self.buttonBox = QtGui.QDialogButtonBox(ChangeInputDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.gridLayout.addWidget(self.buttonBox, 3, 0, 1, 0)
        self.retranslateUi(ChangeInputDialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), ChangeInputDialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), ChangeInputDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(ChangeInputDialog)

    def retranslateUi(self, ChangeInputDialog):
        ChangeInputDialog.setWindowTitle(_translate("ChangeInputDialog", "Changing Input", None))
        self.warning_label.setText(_translate("ChangeInputDialog", "Are you sure you want to change the input of this object?", None))
        self.previous_label.setText(_translate("ChangeInputDialog", "Actual Input:	", None))
        #self.p_label.setText(_translate("ChangeInputDialog", "", None))
        self.new_label.setText(_translate("ChangeInputDialog", "New Input: 	", None))
        #self.n_label.setText(_translate("ChangeInputDialog", "", None))
		


