# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'counter.ui'
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

class Ui_CounterDialog(object):
    def setupUi(self, CounterDialog):
        CounterDialog.setObjectName(_fromUtf8("CounterDialog"))
        CounterDialog.resize(250, 186)
        CounterDialog.setMinimumSize(QtCore.QSize(250, 186))
        CounterDialog.setMaximumSize(QtCore.QSize(250, 186))
        self.gridLayout = QtGui.QGridLayout(CounterDialog)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.comboBox_3 = QtGui.QComboBox(CounterDialog)
        self.comboBox_3.setObjectName(_fromUtf8("comboBox_3"))
        self.comboBox_3.addItem(_fromUtf8(""))
        self.comboBox_3.addItem(_fromUtf8(""))
        self.gridLayout.addWidget(self.comboBox_3, 3, 1, 1, 1)
        self.label_5 = QtGui.QLabel(CounterDialog)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.gridLayout.addWidget(self.label_5, 1, 0, 1, 1)
        self.spinBox = QtGui.QSpinBox(CounterDialog)
        self.spinBox.setMaximum(65535)
        self.spinBox.setObjectName(_fromUtf8("spinBox"))
        self.gridLayout.addWidget(self.spinBox, 1, 1, 1, 1)
        self.label_7 = QtGui.QLabel(CounterDialog)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.gridLayout.addWidget(self.label_7, 2, 0, 1, 1)
        self.comboBox_2 = QtGui.QComboBox(CounterDialog)
        self.comboBox_2.setEditable(False)
        self.comboBox_2.setObjectName(_fromUtf8("comboBox_2"))
        self.gridLayout.addWidget(self.comboBox_2, 2, 1, 1, 1)
        self.label_9 = QtGui.QLabel(CounterDialog)
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.gridLayout.addWidget(self.label_9, 3, 0, 1, 1)
        self.label_3 = QtGui.QLabel(CounterDialog)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout.addWidget(self.label_3, 0, 0, 1, 1)
        self.lineEdit = QtGui.QLineEdit(CounterDialog)
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.gridLayout.addWidget(self.lineEdit, 0, 1, 1, 1)
        self.buttonBox = QtGui.QDialogButtonBox(CounterDialog)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.buttonBox.sizePolicy().hasHeightForWidth())
        self.buttonBox.setSizePolicy(sizePolicy)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.gridLayout.addWidget(self.buttonBox, 4, 0, 1, 2)

        self.retranslateUi(CounterDialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), CounterDialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), CounterDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(CounterDialog)

    def retranslateUi(self, CounterDialog):
        CounterDialog.setWindowTitle(_translate("CounterDialog", "Counter Properties", None))
        self.comboBox_3.setItemText(0, _translate("CounterDialog", "Counter_Up", None))
        self.comboBox_3.setItemText(1, _translate("CounterDialog", "Counter_Down", None))
        self.label_5.setToolTip(_translate("CounterDialog", "<html><head/><body><p>maximum: 65535</p></body></html>", None))
        self.label_5.setText(_translate("CounterDialog", "Setpoint", None))
        self.label_7.setText(_translate("CounterDialog", "Name:", None))
        self.label_9.setText(_translate("CounterDialog", "Type:", None))
        self.label_3.setText(_translate("CounterDialog", "Comment:", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    CounterDialog = QtGui.QDialog()
    ui = Ui_CounterDialog()
    ui.setupUi(CounterDialog)
    CounterDialog.show()
    sys.exit(app.exec_())

