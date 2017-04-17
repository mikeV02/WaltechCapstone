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

class Ui_CoilDialog(object):
    def setupUi(self, CoilDialog):
        CoilDialog.setObjectName(_fromUtf8("CoilDialog"))
        CoilDialog.resize(269, 250)
        self.gridLayout = QtGui.QGridLayout(CoilDialog)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.label_3 = QtGui.QLabel(CoilDialog)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout.addWidget(self.label_3, 0, 0, 1, 1)
        self.label_7 = QtGui.QLabel(CoilDialog)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.gridLayout.addWidget(self.label_7, 3, 0, 1, 1)
        self.comboBox_2 = QtGui.QComboBox(CoilDialog)
        self.comboBox_2.setEditable(True)
        self.comboBox_2.setObjectName(_fromUtf8("comboBox_2"))
        self.gridLayout.addWidget(self.comboBox_2, 3, 1, 1, 1)
        self.lineEdit = QtGui.QLineEdit(CoilDialog)
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.gridLayout.addWidget(self.lineEdit, 0, 1, 1, 1)
        self.comboBox = QtGui.QComboBox(CoilDialog)
        self.comboBox.setObjectName(_fromUtf8("comboBox"))
        self.gridLayout.addWidget(self.comboBox, 1, 1, 1, 1)
        self.label_5 = QtGui.QLabel(CoilDialog)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.gridLayout.addWidget(self.label_5, 1, 0, 1, 1)
        self.label = QtGui.QLabel(CoilDialog)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 4, 0, 1, 1)
        self.buttonBox = QtGui.QDialogButtonBox(CoilDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.gridLayout.addWidget(self.buttonBox, 5, 1, 1, 1)
        self.comboBox_3 = QtGui.QComboBox(CoilDialog)
        self.comboBox_3.setObjectName(_fromUtf8("comboBox_3"))
        self.gridLayout.addWidget(self.comboBox_3, 4, 1, 1, 1)

        self.retranslateUi(CoilDialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), CoilDialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), CoilDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(CoilDialog)

    def retranslateUi(self, CoilDialog):
        CoilDialog.setWindowTitle(_translate("CoilDialog", "Coil Properties", None))
        self.label_3.setText(_translate("CoilDialog", "Comment:", None))
        self.label_7.setText(_translate("CoilDialog", "Name:", None))
        self.label_5.setText(_translate("CoilDialog", "Output", None))
        self.label.setText(_translate("CoilDialog", "Done Bit", None))

