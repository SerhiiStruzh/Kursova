from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtWidgets import QMainWindow, QWidget
import DataBase
from Validation import CorrectCheckNumber, CorrectCheckText
from ServiceCabinet import Cabinet_UI, CabinetScreen
from Person import Person

class SingUp_UI(QMainWindow):
    def __init__(self, Form):
        super().__init__()
        Form.setObjectName("SingUpScreen")
        Form.resize(700, 500)
        Form.setFixedSize(QtCore.QSize(700,500))

        self.frame = QtWidgets.QFrame(parent=Form)
        self.frame.setGeometry(QtCore.QRect(0, 0, 700, 500))
        self.frame.setStyleSheet("background-color: #fffff1;")
        self.frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame.setObjectName("frame")

        self.label = QtWidgets.QLabel(parent=self.frame)
        self.label.setGeometry(QtCore.QRect(80, 100, 160, 160))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("D:/Project/Icons/Register.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")

        self.Name = QtWidgets.QLineEdit(parent=self.frame)
        self.Name.setGeometry(QtCore.QRect(450, 80, 150, 25))
        self.Name.setStyleSheet("background-color:rgba(0,0,0,0);\n"
"border: none;\n"
"border-bottom: 2px solid rgba(105,118,132,255);\n"
"color:rgba(0,0,0,1);")
        self.Name.setObjectName("Name")

        self.Surname = QtWidgets.QLineEdit(parent=self.frame)
        self.Surname.setGeometry(QtCore.QRect(450, 180, 150, 25))
        self.Surname.setStyleSheet("background-color:rgba(0,0,0,0);\n"
"border: none;\n"
"border-bottom: 2px solid rgba(105,118,132,255);\n"
"color:rgba(0,0,0,1);")
        self.Surname.setObjectName("Surname")

        self.IdNumber = QtWidgets.QLineEdit(parent=self.frame)
        self.IdNumber.setGeometry(QtCore.QRect(450, 280, 150, 25))
        self.IdNumber.setStyleSheet("background-color:rgba(0,0,0,0);\n"
"border: none;\n"
"border-bottom: 2px solid rgba(105,118,132,255);\n"
"color:rgba(0,0,0,1);")
        self.IdNumber.setObjectName("IdNumber")

        self.Password = QtWidgets.QLineEdit(parent=self.frame)
        self.Password.setGeometry(QtCore.QRect(450, 380, 150, 25))
        self.Password.setStyleSheet("background-color:rgba(0,0,0,0);\n"
"border: none;\n"
"border-bottom: 2px solid rgba(105,118,132,255);\n"
"color:rgba(0,0,0,1);")
        self.Password.setObjectName("Password")

        self.AllertName = QtWidgets.QTextEdit(parent=self.frame)
        self.AllertName.setGeometry(QtCore.QRect(450, 40, 81, 31))
        self.AllertName.setStyleSheet("border:none")
        self.AllertName.setObjectName("AllertName")
        self.AllertName.setReadOnly(True)

        self.AllertSurname = QtWidgets.QTextEdit(parent=self.frame)
        self.AllertSurname.setGeometry(QtCore.QRect(450, 140, 111, 31))
        self.AllertSurname.setStyleSheet("border:none")
        self.AllertSurname.setObjectName("AllertSurname")
        self.AllertSurname.setReadOnly(True)

        self.AllertIdNumber = QtWidgets.QTextEdit(parent=self.frame)
        self.AllertIdNumber.setGeometry(QtCore.QRect(450, 240, 161, 31))
        self.AllertIdNumber.setStyleSheet("border:none")
        self.AllertIdNumber.setObjectName("AllertIdNumber")
        self.AllertIdNumber.setReadOnly(True)

        self.AllertPassword = QtWidgets.QTextEdit(parent=self.frame)
        self.AllertPassword.setGeometry(QtCore.QRect(450, 340, 81, 31))
        self.AllertPassword.setStyleSheet("border:none")
        self.AllertPassword.setObjectName("AllertPassword")
        self.AllertPassword.setReadOnly(True)

        self.Enter = QtWidgets.QPushButton(parent=self.frame)
        self.Enter.setGeometry(QtCore.QRect(70, 360, 191, 51))
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

        self.ERROR_ALLERT = QtWidgets.QLabel(parent=self.frame)
        self.ERROR_ALLERT.setGeometry(QtCore.QRect(80, 450, 251, 16))
        self.ERROR_ALLERT.setText("")
        self.ERROR_ALLERT.setObjectName("ERROR_ALLERT")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, SingUpScreen):
        _translate = QtCore.QCoreApplication.translate
        SingUpScreen.setWindowTitle(_translate("SingUpScreen", "Form"))
        self.AllertName.setHtml(_translate("SingUpScreen", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">Ім\'я</span></p></body></html>"))
        self.AllertSurname.setHtml(_translate("SingUpScreen", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">Прізвище</span></p></body></html>"))
        self.AllertIdNumber.setHtml(_translate("SingUpScreen", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">Номер паспорта</span></p></body></html>"))
        self.AllertPassword.setHtml(_translate("SingUpScreen", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">Пароль</span></p></body></html>"))
        self.Enter.setText(_translate("SingUpScreen", "Зареєструватися"))

class SingUpScreen(SingUp_UI):
    def __init__(self, Form):
        super().__init__(Form)
        Form.show()
        self.Enter.clicked.connect(lambda: self.RegisterClicked(Form))

    def RegisterClicked(self, Form):
        if self.Name.text() and self.Surname.text() and self.IdNumber.text():
            if CorrectCheckText(self.Name.text().title()) and CorrectCheckText(self.Surname.text()) and CorrectCheckNumber(self.IdNumber.text()) and len(self.IdNumber.text()) == 9:
                if DataBase.SearchUserInDB(self.Name.text().title().encode('utf-8'), self.Surname.text().title().encode('utf-8'), self.IdNumber.text().encode('utf-8'), self.Password.text().encode('utf-8')):
                    self.ERROR_ALLERT.setText("Користувач уже зареєстрований")
                else:
                    DataBase.AddUserInDB(self.Name.text().title().encode('utf-8'), self.Surname.text().title().encode('utf-8'), self.IdNumber.text().encode('utf-8'), self.Password.text().encode('utf-8'))
                    PersonInfo = Person(self.Name.text().title(), self.Surname.text().title(), self.IdNumber.text())
                    global PersonCabinetForm
                    PersonCabinetForm = QWidget()
                    PersonCabinetScr = CabinetScreen(PersonCabinetForm, PersonInfo)
                    Form.close()
            else:
                self.ERROR_ALLERT.setText("Хибно введені дані")
        else:
            self.ERROR_ALLERT.setText("Ви не заповнили усіх полів")