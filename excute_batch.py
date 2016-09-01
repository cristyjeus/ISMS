
# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\일반사용자\Documents\GitHub\ISMS\selectUrl_gui.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
from subprocess import Popen


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

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(400, 300)
        self.lineEdit = QtGui.QLineEdit(Dialog)
        self.lineEdit.setGeometry(QtCore.QRect(20, 50, 251, 21))
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.pushButton = QtGui.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(290, 50, 75, 23))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.listWidget = QtGui.QListWidget(Dialog)
        self.listWidget.setGeometry(QtCore.QRect(20, 80, 251, 191))
        self.listWidget.setObjectName(_fromUtf8("listWidget"))

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Dialog", None))
        self.pushButton.setText(_translate("Dialog", "확인", None))

    def btnClicked(self):
        if self.listWidget.count() > 0
            self.listWidget.clear()

        p = Popen("test.bat",cwd=r"./")
        stdout, stderr = p.communicate()




if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Dialog = QtGui.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    ui.pushButton.clicked.connect(ui.btnClicked)
    Dialog.show()
    sys.exit(app.exec_())
