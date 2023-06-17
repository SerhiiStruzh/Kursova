from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtWidgets import QMainWindow, QWidget
from Person import Person
import DataBase

class Gas_UI(QMainWindow):
    def __init__(self, Form):
        super().__init__()
        Form.setObjectName("Form")
        Form.resize(600, 500)
        Form.setFixedSize(QtCore.QSize(600, 500))

        self.frame = QtWidgets.QFrame(parent=Form)
        self.frame.setGeometry(QtCore.QRect(-1, -1, 601, 501))
        self.frame.setStyleSheet("background-color: rgb(255, 255, 241);")
        self.frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame.setObjectName("frame")

        self.AdressLine = QtWidgets.QLineEdit(parent=self.frame)
        self.AdressLine.setGeometry(QtCore.QRect(170, 150, 231, 22))
        self.AdressLine.setObjectName("AdressLine")

        self.SizeLine = QtWidgets.QLineEdit(parent=self.frame)
        self.SizeLine.setGeometry(QtCore.QRect(170, 240, 231, 22))
        self.SizeLine.setObjectName("SizeLine")

        self.OK = QtWidgets.QPushButton(parent=self.frame)
        self.OK.setGeometry(QtCore.QRect(210, 387, 131, 51))
        self.OK.setStyleSheet("QPushButton {\n"
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
"  background-color: #0000;\n"
"}")
        self.OK.setObjectName("OK")

        self.ERROR = QtWidgets.QLabel(parent=self.frame)
        self.ERROR.setGeometry(QtCore.QRect(170, 340, 281, 21))
        self.ERROR.setText("")
        self.ERROR.setObjectName("ERROR")

        self.AdressMSG = QtWidgets.QTextEdit(parent=self.frame)
        self.AdressMSG.setGeometry(QtCore.QRect(170, 100, 291, 41))
        self.AdressMSG.setStyleSheet("border:none;")
        self.AdressMSG.setObjectName("AdressMSG")
        self.AdressMSG.setReadOnly(True)

        self.SizeMSG = QtWidgets.QTextEdit(parent=self.frame)
        self.SizeMSG.setGeometry(QtCore.QRect(170, 190, 291, 41))
        self.SizeMSG.setStyleSheet("border:none;")
        self.SizeMSG.setObjectName("SizeMSG")
        self.SizeMSG.setReadOnly(True)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.OK.setText(_translate("Form", "OK"))
        self.AdressMSG.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">Введіть адресу проживання</span></p></body></html>"))
        self.SizeMSG.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">Введіть кількість кубометрів</span></p></body></html>"))


class GasFormWindow(Gas_UI):
    def __init__(self, Form, Perso_obj, Cabinet_obj):
        super().__init__(Form)
        Form.show()
        self.OK.clicked.connect(lambda: self.OKClicked(Perso_obj, Form, Cabinet_obj))

    def OKClicked(self, Perso_obj, Form, Cabinet_obj):
        if not self.AdressLine.text() or not self.SizeLine.text():
            self.ERROR.setText("Ви не заповнили всі поля")
        else:
            try:
                if not int(self.SizeLine.text()) <= 0:
                    if DataBase.SeekDeclarationInDB(Perso_obj.get_name().encode('utf-8'), Perso_obj.get_surname().encode('utf-8'), Perso_obj.get_ID().encode('utf-8'), "gas".encode('utf-8')):
                        DataBase.AddDeclaration(Perso_obj.get_name().encode('utf-8'), Perso_obj.get_surname().encode('utf-8'), Perso_obj.get_ID().encode('utf-8'), self.AdressLine.text().encode('utf-8'), "gas".encode('utf-8'), int(self.SizeLine.text())*8)
                        Cabinet_obj.ListOfService.addItem("Сплата за газ")
                        Form.close()
                    else:
                        self.ERROR.setText("Ви вже заповнили форму на цю послугу")
                else:
                    self.ERROR.setText("Хибно введені дані")
            except:
                    self.ERROR.setText("Хибно введені дані")
