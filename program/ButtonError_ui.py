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

class Ui_ButtonErrorDialog(object):
    def setupUi(self, ButtonErrorDialog):
        ButtonErrorDialog.setObjectName(_fromUtf8("ButtonErrorDialog"))
        ButtonErrorDialog.resize(100, 100)
        self.gridLayout = QtGui.QGridLayout(ButtonErrorDialog)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.warning_label = QtGui.QLabel(ButtonErrorDialog)
        self.warning_label.setObjectName(_fromUtf8("warning_label"))
        self.gridLayout.addWidget(self.warning_label, 0, 0, 1, 0)
        self.buttonBox = QtGui.QDialogButtonBox(ButtonErrorDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.gridLayout.addWidget(self.buttonBox, 1, 0, 1, 0)
        self.retranslateUi(ButtonErrorDialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), ButtonErrorDialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), ButtonErrorDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(ButtonErrorDialog)

    def retranslateUi(self, ButtonErrorDialog):
        ButtonErrorDialog.setWindowTitle(_translate("ButtonErrorDialog", "Drag&Drop Button Error", None))
        self.warning_label.setText(_translate("ButtonErrorDialog", "Please make sure the dragged button is compatible with object.\nPlease try again.", None))

		


