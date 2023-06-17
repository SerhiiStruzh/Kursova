from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtWidgets import QMainWindow, QWidget, QMenu
from Person import Person
from UserInfo import UserInfo
import DataBase
from MenuServicesScreen import ServiceMenu
from PaymentAllert import AllertWindow

class Cabinet_UI(QMainWindow):
    def __init__(self,Form):
        super().__init__()
        Form.setObjectName("Form")
        Form.resize(1000, 700)
        Form.setFixedSize(QtCore.QSize(1000,700))

        self.frame = QtWidgets.QFrame(parent=Form)
        self.frame.setGeometry(QtCore.QRect(0, 0, 1000, 701))
        self.frame.setStyleSheet("background-color: rgb(255, 255, 241);")
        self.frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame.setObjectName("frame")

        self.ListOfService = QtWidgets.QListWidget(parent=self.frame)
        self.ListOfService.setGeometry(QtCore.QRect(10, 160, 980, 451))
        self.ListOfService.setStyleSheet("QListWidget {"
    "background-color: #f2f2f2;"
    "border: 1px solid #cccccc;"
    "padding: 5px;"
    "}"

    "QListWidget::item {"
    "background-color: #ffffff;"
    "border-bottom: 1px solid #cccccc;"
    "padding: 5px;"
    "}"

    "QListWidget::item:selected {"
    "background-color: #a0c4ff;"
    "color: #ffffff;"
    "}")
        self.ListOfService.setObjectName("ListOfService")

        self.AddService = QtWidgets.QPushButton(parent=self.frame)
        self.AddService.setGeometry(QtCore.QRect(450, 90, 150, 50))
        self.AddService.setStyleSheet("QPushButton {\n"
" display: inline-block;\n"
" padding: 10px 20px;\n"
" font-size: 16px;\n"
" font-weight: bold;\n"
" text-align: center;\n"
" text-decoration: none;\n"
" color: #6b70ff;\n"
" background-color:#000000;\n"
" border: none;\n"
" border-radius: 25px;\n"
" cursor: pointer;\n"
"}\n"
"QPushButton:hover {\n"
"     color: #8185f7;\n"
"  background-color: #000000;\n"
"}")
        self.AddService.setObjectName("AddService")

        self.PayService = QtWidgets.QPushButton(parent=self.frame)
        self.PayService.setGeometry(QtCore.QRect(450, 630, 150, 50))
        self.PayService.setStyleSheet("QPushButton {\n"
" display: inline-block;\n"
" padding: 10px 20px;\n"
" font-size: 16px;\n"
" font-weight: bold;\n"
" text-align: center;\n"
" text-decoration: none;\n"
" color: #6b70ff;\n"
" background-color:#000000;\n"
" border: none;\n"
" border-radius: 25px;\n"
" cursor: pointer;\n"
"}\n"
"QPushButton:hover {\n"
"     color: #8185f7;\n"
"  background-color: #000000;\n"
"}")
        self.PayService.setIconSize(QtCore.QSize(50, 50))
        self.PayService.setObjectName("PayService")

        self.label = QtWidgets.QLabel(parent=self.frame)
        self.label.setGeometry(QtCore.QRect(370, 90, 50, 50))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("D:/Project/Icons/Plus.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")

        self.label_2 = QtWidgets.QLabel(parent=self.frame)
        self.label_2.setGeometry(QtCore.QRect(370, 630, 50, 50))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("D:/Project/Icons/money.png"))
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")

        self.pushButton = QtWidgets.QPushButton(parent=self.frame)
        self.pushButton.setGeometry(QtCore.QRect(890, 10, 93, 61))
        self.pushButton.setStyleSheet("border:none;")
        self.pushButton.setText("")

        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("D:/Project/Icons/user.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)

        self.pushButton.setIcon(icon)
        self.pushButton.setIconSize(QtCore.QSize(50, 50))
        self.pushButton.setObjectName("pushButton")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.AddService.setText(_translate("Form", "Добавити"))
        self.PayService.setText(_translate("Form", "Сплатити"))


class CabinetScreen(Cabinet_UI):
    def __init__(self, Form, PersonInfo):
        super().__init__(Form)
        self.PersonInfo = PersonInfo
        Form.show()
        self.AddExistedDeclar()
        self.pushButton.clicked.connect(lambda: self.ProfileOpen())
        self.AddService.clicked.connect(lambda: self.AddingServiceInfo())
        self.PayService.clicked.connect(lambda: self.PayForDeclaration())

    def PayForDeclaration(self):
        global PaymetForm
        PaymentForm = QWidget()
        price = DataBase.CountSummDeclaration(self.PersonInfo.get_name().encode("utf-8"), self.PersonInfo.get_surname().encode("utf-8"), self.PersonInfo.get_ID().encode("utf-8"))
        PaymentScreen = AllertWindow(PaymentForm, price)
        self.ListOfService.clear()
        DataBase.RemoveDeclaration(self.PersonInfo.get_name().encode("utf-8"), self.PersonInfo.get_surname().encode("utf-8"), self.PersonInfo.get_ID().encode("utf-8"))

    def AddExistedDeclar(self):
        services = ["water", "trash", "gas", "light"]
        for service in services:
            if not DataBase.SeekDeclarationInDB(self.PersonInfo.get_name().encode('utf-8'), self.PersonInfo.get_surname().encode('utf-8'), self.PersonInfo.get_ID().encode('utf-8'), service.encode('utf-8')):
                if service == "water":
                    self.ListOfService.addItem("Сплата за воду")
                if service == "trash":
                    self.ListOfService.addItem("Сплата за вивіз сміття")
                if service == "gas":
                    self.ListOfService.addItem("Сплата за газ")
                if service == "light":
                    self.ListOfService.addItem("Сплата за світло")

    def ProfileOpen(self):
        global UserInfoForm
        UserInfoForm = QWidget()
        UserInfoScreen = UserInfo(UserInfoForm, self.PersonInfo)

    def AddingServiceInfo(self):
        global ServiceMenuForm
        ServiceMenuForm = QWidget()
        ServiceMenuScreen = ServiceMenu(ServiceMenuForm, self)