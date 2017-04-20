# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'edge.ui'
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

class Ui_EdgeDialog(object):
    def setupUi(self, EdgeDialog):
        EdgeDialog.setObjectName(_fromUtf8("EdgeDialog"))
        EdgeDialog.resize(249, 88)
        EdgeDialog.setMinimumSize(QtCore.QSize(249, 88))
        EdgeDialog.setMaximumSize(QtCore.QSize(249, 88))
        self.gridLayout = QtGui.QGridLayout(EdgeDialog)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.label_3 = QtGui.QLabel(EdgeDialog)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout.addWidget(self.label_3, 0, 0, 1, 1)
        self.lineEdit = QtGui.QLineEdit(EdgeDialog)
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.gridLayout.addWidget(self.lineEdit, 0, 1, 1, 1)
        self.buttonBox = QtGui.QDialogButtonBox(EdgeDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.gridLayout.addWidget(self.buttonBox, 1, 0, 1, 2)

        self.retranslateUi(EdgeDialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), EdgeDialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), EdgeDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(EdgeDialog)

    def retranslateUi(self, EdgeDialog):
        EdgeDialog.setWindowTitle(_translate("EdgeDialog", "Edge Trigger Properties", None))
        self.label_3.setText(_translate("EdgeDialog", "Comment:", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    EdgeDialog = QtGui.QDialog()
    ui = Ui_EdgeDialog()
    ui.setupUi(EdgeDialog)
    EdgeDialog.show()
    sys.exit(app.exec_())

