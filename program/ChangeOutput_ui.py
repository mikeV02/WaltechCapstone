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

class Ui_ChangeOutputDialog(object):
    def setupUi(self, ChangeOutputDialog):
        ChangeOutputDialog.setObjectName(_fromUtf8("ChangeOutputDialog"))
        ChangeOutputDialog.resize(150, 150)
        self.gridLayout = QtGui.QGridLayout(ChangeOutputDialog)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.warning_label = QtGui.QLabel(ChangeOutputDialog)
        self.warning_label.setObjectName(_fromUtf8("warning_label"))
        self.gridLayout.addWidget(self.warning_label, 0, 0, 1, 0)
        self.previous_label = QtGui.QLabel(ChangeOutputDialog)
        self.previous_label.setObjectName(_fromUtf8("previous_label"))
        self.gridLayout.addWidget(self.previous_label, 1, 0, 1, 1)
        self.p_label = QtGui.QLabel(ChangeOutputDialog)
        self.p_label.setObjectName(_fromUtf8("p_label"))
        self.gridLayout.addWidget(self.p_label, 1, 1, 1, 1)
        self.new_label = QtGui.QLabel(ChangeOutputDialog)
        self.new_label.setObjectName(_fromUtf8("new_label"))
        self.gridLayout.addWidget(self.new_label, 2, 0, 1, 1)
        self.n_label = QtGui.QLabel(ChangeOutputDialog)
        self.n_label.setObjectName(_fromUtf8("n_label"))
        self.gridLayout.addWidget(self.n_label, 2, 1, 1, 1)
        self.buttonBox = QtGui.QDialogButtonBox(ChangeOutputDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.gridLayout.addWidget(self.buttonBox, 3, 0, 1, 0)
        self.retranslateUi(ChangeOutputDialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), ChangeOutputDialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), ChangeOutputDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(ChangeOutputDialog)

    def retranslateUi(self, ChangeOutputDialog):
        ChangeOutputDialog.setWindowTitle(_translate("ChangeOutputDialog", "Changing Output", None))
        self.warning_label.setText(_translate("ChangeOutputDialog", "Are you sure you want to change the output of this object?", None))
        self.previous_label.setText(_translate("ChangeOutputDialog", "Actual Output: ", None))
        self.new_label.setText(_translate("ChangeOutputDialog", "New Output: ", None))