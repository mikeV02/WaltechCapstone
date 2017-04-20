# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'math.ui'
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

class Ui_MathDialog(object):
    def setupUi(self, MathDialog):
        MathDialog.setObjectName(_fromUtf8("MathDialog"))
        MathDialog.resize(226, 181)
        MathDialog.setMinimumSize(QtCore.QSize(226, 181))
        MathDialog.setMaximumSize(QtCore.QSize(227, 181))
        self.gridLayout = QtGui.QGridLayout(MathDialog)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.label_5 = QtGui.QLabel(MathDialog)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.gridLayout.addWidget(self.label_5, 0, 0, 1, 2)
        self.label_8 = QtGui.QLabel(MathDialog)
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.gridLayout.addWidget(self.label_8, 0, 2, 1, 2)
        self.label_7 = QtGui.QLabel(MathDialog)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.gridLayout.addWidget(self.label_7, 0, 4, 1, 1)
        self.comboBox_A = QtGui.QComboBox(MathDialog)
        self.comboBox_A.setObjectName(_fromUtf8("comboBox_A"))
        self.gridLayout.addWidget(self.comboBox_A, 1, 0, 1, 3)
        self.comboBox_B = QtGui.QComboBox(MathDialog)
        self.comboBox_B.setEditable(False)
        self.comboBox_B.setObjectName(_fromUtf8("comboBox_B"))
        self.gridLayout.addWidget(self.comboBox_B, 1, 3, 1, 2)
        self.label_6 = QtGui.QLabel(MathDialog)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.gridLayout.addWidget(self.label_6, 2, 0, 1, 2)
        self.label_9 = QtGui.QLabel(MathDialog)
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.gridLayout.addWidget(self.label_9, 2, 4, 1, 1)
        self.spinBox_A = QtGui.QSpinBox(MathDialog)
        self.spinBox_A.setMinimum(-32767)
        self.spinBox_A.setMaximum(32767)
        self.spinBox_A.setObjectName(_fromUtf8("spinBox_A"))
        self.gridLayout.addWidget(self.spinBox_A, 3, 0, 1, 3)
        self.spinBox_B = QtGui.QSpinBox(MathDialog)
        self.spinBox_B.setMinimum(-32767)
        self.spinBox_B.setMaximum(32767)
        self.spinBox_B.setProperty("value", 0)
        self.spinBox_B.setObjectName(_fromUtf8("spinBox_B"))
        self.gridLayout.addWidget(self.spinBox_B, 3, 3, 1, 2)
        self.label_10 = QtGui.QLabel(MathDialog)
        self.label_10.setObjectName(_fromUtf8("label_10"))
        self.gridLayout.addWidget(self.label_10, 4, 0, 1, 1)
        self.comboBox_2 = QtGui.QComboBox(MathDialog)
        self.comboBox_2.setEditable(True)
        self.comboBox_2.setObjectName(_fromUtf8("comboBox_2"))
        self.gridLayout.addWidget(self.comboBox_2, 4, 1, 1, 4)
        self.buttonBox = QtGui.QDialogButtonBox(MathDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.gridLayout.addWidget(self.buttonBox, 5, 1, 1, 4)

        self.retranslateUi(MathDialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), MathDialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), MathDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(MathDialog)

    def retranslateUi(self, MathDialog):
        MathDialog.setWindowTitle(_translate("MathDialog", "Math Operator", None))
        self.label_5.setText(_translate("MathDialog", "Source", None))
        self.label_8.setText(_translate("MathDialog", "(+,-,x,÷)", None))
        self.label_7.setText(_translate("MathDialog", "Source", None))
        self.label_6.setText(_translate("MathDialog", "Constant", None))
        self.label_9.setText(_translate("MathDialog", "Constant", None))
        self.label_10.setText(_translate("MathDialog", "=", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MathDialog = QtGui.QDialog()
    ui = Ui_MathDialog()
    ui.setupUi(MathDialog)
    MathDialog.show()
    sys.exit(app.exec_())

