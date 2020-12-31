# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\python\python\дизайн\cal.2.ui'
#
# Created: Tue Dec 29 21:06:59 2020
#      by: pyside-uic 0.2.15 running on PySide 1.2.4
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_Dialog2(object):
    def setupUi(self, Dialog2):
        Dialog2.setObjectName("Dialog2")
        Dialog2.resize(274, 609)
        self.lineEdit = QtGui.QLineEdit(Dialog2)
        self.lineEdit.setGeometry(QtCore.QRect(20, 219, 241, 31))
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton_4 = QtGui.QPushButton(Dialog2)
        self.pushButton_4.setGeometry(QtCore.QRect(80, 500, 101, 31))
        self.pushButton_4.setObjectName("pushButton_4")
        self.label_7 = QtGui.QLabel(Dialog2)
        self.label_7.setGeometry(QtCore.QRect(80, 550, 521, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_7.setFont(font)
        self.label_7.setText("")
        self.label_7.setObjectName("label_7")
        self.lineEdit_4 = QtGui.QLineEdit(Dialog2)
        self.lineEdit_4.setGeometry(QtCore.QRect(20, 439, 241, 31))
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.label_4 = QtGui.QLabel(Dialog2)
        self.label_4.setGeometry(QtCore.QRect(60, 410, 231, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.lineEdit_3 = QtGui.QLineEdit(Dialog2)
        self.lineEdit_3.setGeometry(QtCore.QRect(20, 329, 241, 31))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.label = QtGui.QLabel(Dialog2)
        self.label.setGeometry(QtCore.QRect(70, 190, 181, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_3 = QtGui.QLabel(Dialog2)
        self.label_3.setGeometry(QtCore.QRect(90, 300, 141, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.pushButton_3 = QtGui.QPushButton(Dialog2)
        self.pushButton_3.setGeometry(QtCore.QRect(160, 110, 101, 31))
        self.pushButton_3.setObjectName("pushButton_3")
        self.label_5 = QtGui.QLabel(Dialog2)
        self.label_5.setGeometry(QtCore.QRect(10, 50, 251, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.pushButton_5 = QtGui.QPushButton(Dialog2)
        self.pushButton_5.setGeometry(QtCore.QRect(20, 110, 101, 31))
        self.pushButton_5.setObjectName("pushButton_5")

        self.retranslateUi(Dialog2)
        QtCore.QMetaObject.connectSlotsByName(Dialog2)

    def retranslateUi(self, Dialog2):
        Dialog2.setWindowTitle(QtGui.QApplication.translate("Dialog2", "Dialog", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_4.setText(QtGui.QApplication.translate("Dialog2", "Вычислить", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("Dialog2", "Цена за 1кг.(грн)", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("Dialog2", "Ширина рулона(м)", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("Dialog2", "вес м2(г)", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_3.setText(QtGui.QApplication.translate("Dialog2", "П. м. в  кг", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("Dialog2", "килограмы в погоные метры", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_5.setText(QtGui.QApplication.translate("Dialog2", "Кг в п. м.", None, QtGui.QApplication.UnicodeUTF8))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Dialog2 = QtGui.QDialog()
    ui = Ui_Dialog2()
    ui.setupUi(Dialog2)
    Dialog2.show()
    sys.exit(app.exec_())

