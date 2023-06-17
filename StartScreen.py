from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QWidget
from SingInScreen import SingIn_UI, SingInScreen
from SingUpScreen import SingUp_UI, SingUpScreen


class Enter_UI(QMainWindow):
    def __init__(self,Form):
        super().__init__()
        Form.setObjectName("Form")
        Form.resize(400, 300)
        Form.setFixedSize(QtCore.QSize(400,300))

        self.frame = QtWidgets.QFrame(parent=Form)
        self.frame.setGeometry(QtCore.QRect(0, 0, 400, 300))
        self.frame.setStyleSheet("QFrame {\n"
"  background-color: #ffffff;\n"
"  position: relative; \n"
"}")
        self.frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame.setFixedSize(QtCore.QSize(411,301))
        self.frame.setObjectName("frame")

        #self.StudName = QtWidgets.QLabel(parent=self.frame)
        #self.StudName.setGeometry(QtCore.QRect(170, 30, 100, 30))
        #self.StudName.setText("Сергій Струж")
        #self.StudName.setObjectName("NAME")

        self.Sing_In = QtWidgets.QPushButton(parent=self.frame)
        self.Sing_In.setGeometry(QtCore.QRect(140, 80, 130, 50))
        self.Sing_In.setStyleSheet("QPushButton {\n"
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
        self.Sing_In.setObjectName("pushButton")
        self.Sing_Up = QtWidgets.QPushButton(parent=self.frame)
        self.Sing_Up.setGeometry(QtCore.QRect(140, 150, 130, 50))
        self.Sing_Up.setStyleSheet("QPushButton {\n"
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
        self.Sing_Up.setObjectName("pushButton_2")

        self.retranslateUi(Form)
        
        QtCore.QMetaObject.connectSlotsByName(Form)


    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.Sing_In.setText(_translate("Form", "Вхід"))
        self.Sing_Up.setText(_translate("Form", "Реєстрація"))


class StartScreen(Enter_UI):
    def __init__(self, Form):
        super().__init__(Form)
        Form.setWindowTitle("Cергій Струж")
        Form.show()
        self.Sing_Up.clicked.connect(lambda: self.OpenSingUp(Form))
        self.Sing_In.clicked.connect(lambda: self.OpenSingIn(Form))

    def OpenSingIn(self, Form):
        global SingInForm
        SingInForm = QWidget()
        SingInForm.setWindowTitle("Сергій Струж")
        SingInScr = SingInScreen(SingInForm)
        Form.close()

    def OpenSingUp(self, Form):
        global SingUpForm
        SingUpForm = QWidget()
        SingUpScr = SingUpScreen(SingUpForm)
        Form.close()
