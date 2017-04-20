# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'cont.ui'
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

class Ui_ContDialog(object):
    def setupUi(self, ContDialog):
        ContDialog.setObjectName(_fromUtf8("ContDialog"))
        ContDialog.resize(300, 201)
        ContDialog.setMinimumSize(QtCore.QSize(300, 201))
        ContDialog.setMaximumSize(QtCore.QSize(300, 201))
        self.gridLayout = QtGui.QGridLayout(ContDialog)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.label_3 = QtGui.QLabel(ContDialog)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout.addWidget(self.label_3, 0, 0, 1, 1)
        self.lineEdit = QtGui.QLineEdit(ContDialog)
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.gridLayout.addWidget(self.lineEdit, 0, 1, 1, 1)
        self.label_5 = QtGui.QLabel(ContDialog)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.gridLayout.addWidget(self.label_5, 1, 0, 1, 1)
        self.comboBox = QtGui.QComboBox(ContDialog)
        self.comboBox.setObjectName(_fromUtf8("comboBox"))
        self.gridLayout.addWidget(self.comboBox, 1, 1, 1, 1)
        self.label_7 = QtGui.QLabel(ContDialog)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.gridLayout.addWidget(self.label_7, 2, 0, 1, 1)
        self.comboBox_2 = QtGui.QComboBox(ContDialog)
        self.comboBox_2.setEditable(True)
        self.comboBox_2.setObjectName(_fromUtf8("comboBox_2"))
        self.gridLayout.addWidget(self.comboBox_2, 2, 1, 1, 1)
        self.comboBox_3 = QtGui.QComboBox(ContDialog)
        self.comboBox_3.setObjectName(_fromUtf8("comboBox_3"))
        self.gridLayout.addWidget(self.comboBox_3, 3, 1, 1, 1)
        self.label = QtGui.QLabel(ContDialog)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 3, 0, 1, 1)
        self.buttonBox = QtGui.QDialogButtonBox(ContDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.gridLayout.addWidget(self.buttonBox, 4, 0, 1, 2)

        self.retranslateUi(ContDialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), ContDialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), ContDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(ContDialog)

    def retranslateUi(self, ContDialog):
        ContDialog.setWindowTitle(_translate("ContDialog", "Contact Properties", None))
        self.label_3.setText(_translate("ContDialog", "Comment:", None))
        self.label_5.setText(_translate("ContDialog", "Input", None))
        self.label_7.setText(_translate("ContDialog", "Name:", None))
        self.label.setText(_translate("ContDialog", "Done Bit:", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    ContDialog = QtGui.QDialog()
    ui = Ui_ContDialog()
    ui.setupUi(ContDialog)
    ContDialog.show()
    sys.exit(app.exec_())

