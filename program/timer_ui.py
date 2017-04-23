# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'timer.ui'
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

class Ui_TimerDialog(object):
    def setupUi(self, TimerDialog):
        TimerDialog.setObjectName(_fromUtf8("TimerDialog"))
        TimerDialog.resize(256, 174)
        self.gridLayout = QtGui.QGridLayout(TimerDialog)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.label_3 = QtGui.QLabel(TimerDialog)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout.addWidget(self.label_3, 0, 0, 1, 1)
        self.lineEdit = QtGui.QLineEdit(TimerDialog)
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.gridLayout.addWidget(self.lineEdit, 0, 1, 1, 1)
        self.label_5 = QtGui.QLabel(TimerDialog)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.gridLayout.addWidget(self.label_5, 1, 0, 1, 1)
        self.doubleSpinBox = QtGui.QDoubleSpinBox(TimerDialog)
        self.doubleSpinBox.setMinimum(0.01)
        self.doubleSpinBox.setMaximum(655.34)
        self.doubleSpinBox.setSingleStep(0.01)
        self.doubleSpinBox.setObjectName(_fromUtf8("doubleSpinBox"))
        self.gridLayout.addWidget(self.doubleSpinBox, 1, 1, 1, 1)
        self.label_7 = QtGui.QLabel(TimerDialog)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.gridLayout.addWidget(self.label_7, 2, 0, 1, 1)
        self.comboBox_2 = QtGui.QComboBox(TimerDialog)
        self.comboBox_2.setEditable(False)
        self.comboBox_2.setObjectName(_fromUtf8("comboBox_2"))
        self.gridLayout.addWidget(self.comboBox_2, 2, 1, 1, 1)
        self.label_9 = QtGui.QLabel(TimerDialog)
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.gridLayout.addWidget(self.label_9, 3, 0, 1, 1)
        self.comboBox_3 = QtGui.QComboBox(TimerDialog)
        self.comboBox_3.setObjectName(_fromUtf8("comboBox_3"))
        self.comboBox_3.addItem(_fromUtf8(""))
        self.comboBox_3.addItem(_fromUtf8(""))
        self.gridLayout.addWidget(self.comboBox_3, 3, 1, 1, 1)
        self.buttonBox = QtGui.QDialogButtonBox(TimerDialog)
        self.buttonBox.setMinimumSize(QtCore.QSize(238, 27))
        self.buttonBox.setMaximumSize(QtCore.QSize(238, 27))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.gridLayout.addWidget(self.buttonBox, 4, 0, 1, 2)

        self.retranslateUi(TimerDialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), TimerDialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), TimerDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(TimerDialog)

    def retranslateUi(self, TimerDialog):
        TimerDialog.setWindowTitle(_translate("TimerDialog", "Timer Properties", None))
        self.label_3.setText(_translate("TimerDialog", "Comment:", None))
        self.label_5.setToolTip(_translate("TimerDialog", "<html><head/><body><p>10 min. max</p></body></html>", None))
        self.label_5.setText(_translate("TimerDialog", "Sec delay:", None))
        self.doubleSpinBox.setToolTip(_translate("TimerDialog", "<html><head/><body><p>10 miniutes max</p></body></html>", None))
        self.label_7.setText(_translate("TimerDialog", "Name:", None))
        self.label_9.setText(_translate("TimerDialog", "Type:", None))
        self.comboBox_3.setItemText(0, _translate("TimerDialog", "Timer_On_Delay", None))
        self.comboBox_3.setItemText(1, _translate("TimerDialog", "Retentive_Timer_On", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    TimerDialog = QtGui.QDialog()
    ui = Ui_TimerDialog()
    ui.setupUi(TimerDialog)
    TimerDialog.show()
    sys.exit(app.exec_())

