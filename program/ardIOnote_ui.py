# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ardIOnote.ui'
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

class Ui_ardIOnoteDialog(object):
    def setupUi(self, ardIOnoteDialog):
        ardIOnoteDialog.setObjectName(_fromUtf8("ardIOnoteDialog"))
        ardIOnoteDialog.resize(289, 167)
        ardIOnoteDialog.setMinimumSize(QtCore.QSize(289, 167))
        ardIOnoteDialog.setMaximumSize(QtCore.QSize(289, 167))
        self.gridLayout = QtGui.QGridLayout(ardIOnoteDialog)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.label = QtGui.QLabel(ardIOnoteDialog)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(170, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(106, 104, 100))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        self.label.setPalette(palette)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.buttonBox = QtGui.QDialogButtonBox(ardIOnoteDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.gridLayout.addWidget(self.buttonBox, 1, 0, 1, 1)

        self.retranslateUi(ardIOnoteDialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), ardIOnoteDialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), ardIOnoteDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(ardIOnoteDialog)

    def retranslateUi(self, ardIOnoteDialog):
        ardIOnoteDialog.setWindowTitle(_translate("ardIOnoteDialog", "Changing Hardware Error.", None))
        self.label.setText(_translate("ardIOnoteDialog", "There are IO, PWM ,or ADC\n"
"numbers higher than\n"
"this hardwar supports.\n"
"\n"
"Please remove those elements \n"
"before choosing this hardware. ", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    ardIOnoteDialog = QtGui.QDialog()
    ui = Ui_ardIOnoteDialog()
    ui.setupUi(ardIOnoteDialog)
    ardIOnoteDialog.show()
    sys.exit(app.exec_())

