from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtWidgets import QMainWindow, QWidget
import DataBase
from Validation import CorrectCheckText, CorrectCheckNumber
from Person import Person
from ServiceCabinet import Cabinet_UI, CabinetScreen


class SingIn_UI(QMainWindow):
    def __init__(self,Form):
        super().__init__()
        Form.setObjectName("Form")
        Form.resize(700, 500)
        Form.setFixedSize(QtCore.QSize(700,500))

        self.frame = QtWidgets.QFrame(parent=Form)
        self.frame.setGeometry(QtCore.QRect(-30, 0, 741, 501))
        self.frame.setStyleSheet("background-color: #fffff1;\n"
"position: relative; \n"
"")
        self.frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame.setObjectName("frame")

        self.NameSurname = QtWidgets.QLineEdit(parent=self.frame)
        self.NameSurname.setGeometry(QtCore.QRect(410, 90, 191, 21))
        self.NameSurname.setStyleSheet("background-color:rgba(0,0,0,0);\n"
"border: none;\n"
"border-bottom: 2px solid rgba(105,118,132,255);\n"
"color:rgba(0,0,0,1);\n"
"")
        self.NameSurname.setPlaceholderText("")
        self.NameSurname.setObjectName("NameSurname")

        self.Password = QtWidgets.QLineEdit(parent=self.frame)
        self.Password.setGeometry(QtCore.QRect(410, 270, 191, 21))
        self.Password.setStyleSheet("background-color:rgba(0,0,0,0);\n"
"border: none;\n"
"border-bottom: 2px solid rgba(105,118,132,255);\n"
"color:rgba(0,0,0,1);\n"
"")
        self.Password.setPlaceholderText("")
        self.Password.setObjectName("Password")

        self.AllertNameSurname = QtWidgets.QTextEdit(parent=self.frame)
        self.AllertNameSurname.setGeometry(QtCore.QRect(410, 40, 181, 41))
        self.AllertNameSurname.setStyleSheet("border:none")
        self.AllertNameSurname.setObjectName("AllertNameSurname")
        self.AllertNameSurname.setReadOnly(True)

        self.AllertPassword = QtWidgets.QTextEdit(parent=self.frame)
        self.AllertPassword.setGeometry(QtCore.QRect(410, 220, 181, 41))
        self.AllertPassword.setStyleSheet("border:none")
        self.AllertPassword.setObjectName("AllertPassword")
        self.AllertPassword.setReadOnly(True)

        self.Enter = QtWidgets.QPushButton(parent=self.frame)
        self.Enter.setGeometry(QtCore.QRect(280, 380, 161, 51))
        self.Enter.setStyleSheet("QPushButton {\n"
"  display: inline-block;\n"
"  padding: 10px 20px;\n"
"  font-size: 16px;\n"
"  font-weight: bold;\n"
"  text-align: center;\n"
"  text-decoration: none;\n"
"  color: #6b70ff;\n"
"  background-color: #000000;\n"
"  border: none;\n"
"  border-radius: 25px;\n"
"  cursor: pointer;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"     color: #8185f7;\n"
"  background-color: #000000;\n"
"}")
        self.Enter.setObjectName("Enter")

        self.PersonLogo = QtWidgets.QLabel(parent=self.frame)
        self.PersonLogo.setGeometry(QtCore.QRect(110, 90, 161, 161))
        self.PersonLogo.setText("")
        self.PersonLogo.setPixmap(QtGui.QPixmap("D:/Project/Icons/person.png"))
        self.PersonLogo.setScaledContents(True)
        self.PersonLogo.setObjectName("PersonLogo")

        self.AllertID = QtWidgets.QTextEdit(parent=self.frame)
        self.AllertID.setGeometry(QtCore.QRect(410, 130, 181, 41))
        self.AllertID.setStyleSheet("border:none")
        self.AllertID.setObjectName("AllertID")
        self.AllertID.setReadOnly(True)

        self.ID = QtWidgets.QLineEdit(parent=self.frame)
        self.ID.setGeometry(QtCore.QRect(410, 180, 191, 21))
        self.ID.setStyleSheet("background-color:rgba(0,0,0,0);\n"
"border: none;\n"
"border-bottom: 2px solid rgba(105,118,132,255);\n"
"color:rgba(0,0,0,1);\n"
"")
        self.ID.setPlaceholderText("")
        self.ID.setObjectName("ID")

        self.ERROR_ALLERT = QtWidgets.QLabel(parent=self.frame)
        self.ERROR_ALLERT.setGeometry(QtCore.QRect(410, 330, 301, 16))
        self.ERROR_ALLERT.setText("")
        self.ERROR_ALLERT.setObjectName("ERROR_ALLERT")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.AllertNameSurname.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11pt;\">Ім\'я та Прізвище</span></p></body></html>"))
        self.AllertPassword.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11pt;\">Пароль</span></p></body></html>"))
        self.Enter.setText(_translate("Form", "Увійти"))
        self.AllertID.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11pt;\">Номер паспорта</span></p></body></html>"))

class SingInScreen(SingIn_UI):
    def __init__(self, Form):
        super().__init__(Form)
        Form.show()
        self.Enter.clicked.connect(lambda: self.EnterClicked(Form))

    def EnterClicked(self, Form):
        if len(self.NameSurname.text().split()) == 2 and self.ID.text():
            if CorrectCheckText(self.NameSurname.text().split()[0].title()) and CorrectCheckText(self.NameSurname.text().split()[1].title()) and CorrectCheckNumber(self.ID.text()) and len(self.ID.text()) == 9:
                if not DataBase.SearchUserInDB(self.NameSurname.text().split()[0].title().encode('utf-8'), self.NameSurname.text().title().split()[1].encode('utf-8'),self.ID.text().encode('utf-8') ,self.Password.text().encode('utf-8')):
                    self.ERROR_ALLERT.setText("Користувач не зареєстрований")
                else:
                    PersonInfo = Person(self.NameSurname.text().split()[0].title(), self.NameSurname.text().split()[1].title(), self.ID.text())
                    global PersonCabinetForm
                    PersonCabinetForm = QWidget()
                    PersonCabinetScr = CabinetScreen(PersonCabinetForm, PersonInfo)
                    Form.close()
            else:
                self.ERROR_ALLERT.setText("Хибно введені дані")
        else:
            self.ERROR_ALLERT.setText("Ви не заповнили усіх полів")
