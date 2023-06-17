from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtWidgets import QMainWindow, QWidget
from Person import Person

class UserInfo_UI(QMainWindow):
    def __init__(self,Form):
        super().__init__()
        Form.setObjectName("Form")
        Form.resize(900, 600)
        Form.setFixedSize(QtCore.QSize(900,600))

        self.frame = QtWidgets.QFrame(parent=Form)
        self.frame.setGeometry(QtCore.QRect(0, 0, 900, 600))
        self.frame.setStyleSheet("background-color: rgb(255, 255, 241);")
        self.frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame.setObjectName("frame")

        self.NameAllert = QtWidgets.QTextEdit(parent=self.frame)
        self.NameAllert.setGeometry(QtCore.QRect(60, 300, 131, 31))
        self.NameAllert.setStyleSheet("border: none;")
        self.NameAllert.setObjectName("NameAllert")
        self.NameAllert.setReadOnly(True)

        self.SurnameAllert = QtWidgets.QTextEdit(parent=self.frame)
        self.SurnameAllert.setGeometry(QtCore.QRect(360, 300, 131, 31))
        self.SurnameAllert.setStyleSheet("border: none;")
        self.SurnameAllert.setObjectName("SurnameAllert")
        self.SurnameAllert.setReadOnly(True)

        self.IDAllert = QtWidgets.QTextEdit(parent=self.frame)
        self.IDAllert.setGeometry(QtCore.QRect(660, 300, 181, 31))
        self.IDAllert.setStyleSheet("border: none;")
        self.IDAllert.setObjectName("IDAllert")
        self.IDAllert.setReadOnly(True)

        self.Name = QtWidgets.QLabel(parent=self.frame)
        self.Name.setGeometry(QtCore.QRect(60, 350, 151, 21))
        self.Name.setText("")
        self.Name.setObjectName("Name")

        self.Surname = QtWidgets.QLabel(parent=self.frame)
        self.Surname.setGeometry(QtCore.QRect(360, 350, 151, 21))
        self.Surname.setText("")
        self.Surname.setObjectName("Surname")

        self.ID = QtWidgets.QLabel(parent=self.frame)
        self.ID.setGeometry(QtCore.QRect(660, 350, 171, 21))
        self.ID.setText("")
        self.ID.setObjectName("ID")

        self.ICON = QtWidgets.QLabel(parent=self.frame)
        self.ICON.setGeometry(QtCore.QRect(390, 70, 100, 100))
        self.ICON.setText("")
        self.ICON.setPixmap(QtGui.QPixmap("D:/vsproject/CourseProject/Icons/user.png"))
        self.ICON.setScaledContents(True)
        self.ICON.setObjectName("ICON")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.NameAllert.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">Ім\'я</span></p></body></html>"))
        self.SurnameAllert.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">Прізвище</span></p></body></html>"))
        self.IDAllert.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">Номер паспорта</span></p></body></html>"))


class UserInfo(UserInfo_UI):
    def __init__(self,Form, PersonInfo):
        super().__init__(Form)
        self.Name.setText(PersonInfo.get_name())
        self.Surname.setText(PersonInfo.get_surname())
        self.ID.setText(PersonInfo.get_ID())
        Form.show()
