# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ADC.ui'
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

class Ui_ADCDialog(object):
    def setupUi(self, ADCDialog):
        ADCDialog.setObjectName(_fromUtf8("ADCDialog"))
        ADCDialog.resize(227, 140)
        ADCDialog.setMinimumSize(QtCore.QSize(227, 140))
        ADCDialog.setMaximumSize(QtCore.QSize(227, 140))
        self.gridLayout = QtGui.QGridLayout(ADCDialog)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.label_3 = QtGui.QLabel(ADCDialog)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout.addWidget(self.label_3, 0, 0, 1, 1)
        self.lineEdit = QtGui.QLineEdit(ADCDialog)
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.gridLayout.addWidget(self.lineEdit, 0, 1, 1, 1)
        self.label_5 = QtGui.QLabel(ADCDialog)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.gridLayout.addWidget(self.label_5, 1, 0, 1, 1)
        self.comboBox = QtGui.QComboBox(ADCDialog)
        self.comboBox.setObjectName(_fromUtf8("comboBox"))
        self.gridLayout.addWidget(self.comboBox, 1, 1, 1, 1)
        self.label_7 = QtGui.QLabel(ADCDialog)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.gridLayout.addWidget(self.label_7, 2, 0, 1, 1)
        self.comboBox_2 = QtGui.QComboBox(ADCDialog)
        self.comboBox_2.setEditable(True)
        self.comboBox_2.setObjectName(_fromUtf8("comboBox_2"))
        self.gridLayout.addWidget(self.comboBox_2, 2, 1, 1, 1)
        self.buttonBox = QtGui.QDialogButtonBox(ADCDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.gridLayout.addWidget(self.buttonBox, 3, 0, 1, 2)

        self.retranslateUi(ADCDialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), ADCDialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), ADCDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(ADCDialog)

    def retranslateUi(self, ADCDialog):
        ADCDialog.setWindowTitle(_translate("ADCDialog", "ADC", None))
        self.label_3.setText(_translate("ADCDialog", "Comment:", None))
        self.label_5.setText(_translate("ADCDialog", "Input:", None))
        self.label_7.setText(_translate("ADCDialog", "Name:", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    ADCDialog = QtGui.QDialog()
    ui = Ui_ADCDialog()
    ui.setupUi(ADCDialog)
    ADCDialog.show()
    sys.exit(app.exec_())

