# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'PWM.ui'
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

class Ui_PWMDialog(object):
    def setupUi(self, PWMDialog):
        PWMDialog.setObjectName(_fromUtf8("PWMDialog"))
        PWMDialog.resize(217, 140)
        PWMDialog.setMinimumSize(QtCore.QSize(217, 140))
        PWMDialog.setMaximumSize(QtCore.QSize(217, 140))
        self.gridLayout = QtGui.QGridLayout(PWMDialog)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.label_4 = QtGui.QLabel(PWMDialog)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.gridLayout.addWidget(self.label_4, 0, 0, 1, 1)
        self.lineEdit = QtGui.QLineEdit(PWMDialog)
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.gridLayout.addWidget(self.lineEdit, 0, 1, 1, 1)
        self.label_6 = QtGui.QLabel(PWMDialog)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.gridLayout.addWidget(self.label_6, 1, 0, 1, 1)
        self.doubleSpinBox = QtGui.QDoubleSpinBox(PWMDialog)
        self.doubleSpinBox.setDecimals(1)
        self.doubleSpinBox.setSingleStep(0.2)
        self.doubleSpinBox.setProperty("value", 50.0)
        self.doubleSpinBox.setObjectName(_fromUtf8("doubleSpinBox"))
        self.gridLayout.addWidget(self.doubleSpinBox, 1, 1, 1, 1)
        self.label_9 = QtGui.QLabel(PWMDialog)
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.gridLayout.addWidget(self.label_9, 1, 2, 1, 1)
        self.label_5 = QtGui.QLabel(PWMDialog)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.gridLayout.addWidget(self.label_5, 2, 0, 1, 1)
        self.comboBox = QtGui.QComboBox(PWMDialog)
        self.comboBox.setObjectName(_fromUtf8("comboBox"))
        self.gridLayout.addWidget(self.comboBox, 2, 1, 1, 1)
        self.buttonBox = QtGui.QDialogButtonBox(PWMDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.gridLayout.addWidget(self.buttonBox, 3, 0, 1, 2)

        self.retranslateUi(PWMDialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), PWMDialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), PWMDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(PWMDialog)

    def retranslateUi(self, PWMDialog):
        PWMDialog.setWindowTitle(_translate("PWMDialog", "PWM", None))
        self.label_4.setText(_translate("PWMDialog", "Comment:", None))
        self.label_6.setText(_translate("PWMDialog", "Duty Cycle", None))
        self.label_9.setText(_translate("PWMDialog", "%", None))
        self.label_5.setText(_translate("PWMDialog", "Output", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    PWMDialog = QtGui.QDialog()
    ui = Ui_PWMDialog()
    ui.setupUi(PWMDialog)
    PWMDialog.show()
    sys.exit(app.exec_())

