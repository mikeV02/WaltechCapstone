# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'wrongVersion.ui'
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

class Ui_wrongVersionDialog(object):
    def setupUi(self, wrongVersionDialog):
        wrongVersionDialog.setObjectName(_fromUtf8("wrongVersionDialog"))
        wrongVersionDialog.resize(312, 84)
        self.gridLayout = QtGui.QGridLayout(wrongVersionDialog)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.label = QtGui.QLabel(wrongVersionDialog)
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
        self.buttonBox = QtGui.QDialogButtonBox(wrongVersionDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.gridLayout.addWidget(self.buttonBox, 1, 0, 1, 1)

        self.retranslateUi(wrongVersionDialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), wrongVersionDialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), wrongVersionDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(wrongVersionDialog)

    def retranslateUi(self, wrongVersionDialog):
        wrongVersionDialog.setWindowTitle(_translate("wrongVersionDialog", "Wrong version", None))
        self.label.setText(_translate("wrongVersionDialog", "Sorry, cannot open older file version.", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    wrongVersionDialog = QtGui.QDialog()
    ui = Ui_wrongVersionDialog()
    ui.setupUi(wrongVersionDialog)
    wrongVersionDialog.show()
    sys.exit(app.exec_())

