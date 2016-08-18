# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\일반사용자\Documents\GitHub\ISMS\selectUrl_gui.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
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

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(400, 300)
        self.lineEdit = QtGui.QLineEdit(Dialog)
        self.lineEdit.setGeometry(QtCore.QRect(20, 50, 251, 21))
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.label = QtGui.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(30, 20, 161, 16))
        self.label.setObjectName(_fromUtf8("label"))
        self.pushButton = QtGui.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(290, 50, 75, 23))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.listWidget = QtGui.QTextBrowser(Dialog)
        self.listWidget.setGeometry(QtCore.QRect(20, 80, 251, 191))
        self.listWidget.setObjectName(_fromUtf8("listWidget"))

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Dialog", None))
        self.label.setText(_translate("Dialog", "url 입력 파싱 테스트", None))
        self.pushButton.setText(_translate("Dialog", "확인", None))

    def btnClicked(self):
        self.listWidget.clear()
        url = 'http://'+self.lineEdit.text()
        print(url)
        try:
            # For Python 3.0 and later
            from urllib.request import urlopen
        except ImportError:
            # Fall back to Python 2's urllib2
            from urllib2 import urlopen

        from bs4 import BeautifulSoup
        html = urlopen(url)
        soup = BeautifulSoup(html,"html.parser")
        titles = soup.find_all("a")
        for title in titles:
            self.listWidget.append('link:{0:20s}\n'.format(title['href']))



if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Dialog = QtGui.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    ui.pushButton.clicked.connect(ui.btnClicked)
    Dialog.show()
    sys.exit(app.exec_())
