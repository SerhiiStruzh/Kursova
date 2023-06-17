from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtWidgets import QMainWindow, QWidget
from Water import WaterFormScreen
from Gas import GasFormWindow
from Light import LightFormScreen
from Trash import TrashFormWindow

class ServiceMenu_UI(QMainWindow):
    def __init__(self, Form):
        super().__init__()
        Form.setObjectName("Form")
        Form.resize(500, 350)
        Form.setFixedSize(QtCore.QSize(500,350))

        self.frame = QtWidgets.QFrame(parent=Form)
        self.frame.setGeometry(QtCore.QRect(0, 0, 500, 350))
        self.frame.setStyleSheet("background-color: rgb(255, 255, 241);")
        self.frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame.setObjectName("frame")

        self.AddWater = QtWidgets.QPushButton(parent=self.frame)
        self.AddWater.setGeometry(QtCore.QRect(50, 50, 128, 128))
        self.AddWater.setStyleSheet("QPushButton{\n"
"border:none;\n"
"border-radius: 25px;\n"
"}\n"
"QPushButton:hover {\n"
"  background-color: #ffffbb;\n"
"}")
        self.AddWater.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("D:/Project/Icons/water.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)

        self.AddWater.setIcon(icon)
        self.AddWater.setIconSize(QtCore.QSize(128, 128))
        self.AddWater.setObjectName("AddWater")
        self.AddGas = QtWidgets.QPushButton(parent=self.frame)
        self.AddGas.setGeometry(QtCore.QRect(320, 50, 128, 128))
        self.AddGas.setStyleSheet("QPushButton{\n"
"border:none;\n"
"border-radius: 25px;\n"
"}\n"
"QPushButton:hover {\n"
"  background-color: #ffffbb;\n"
"}border:none;")
        self.AddGas.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("D:/Project/Icons/gas.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)

        self.AddGas.setIcon(icon1)
        self.AddGas.setIconSize(QtCore.QSize(128, 128))
        self.AddGas.setObjectName("AddGas")
        self.AddTrash = QtWidgets.QPushButton(parent=self.frame)
        self.AddTrash.setGeometry(QtCore.QRect(50, 200, 128, 128))
        self.AddTrash.setStyleSheet("QPushButton{\n"
"border:none;\n"
"border-radius: 25px;\n"
"}\n"
"QPushButton:hover {\n"
"  background-color: #ffffbb;\n"
"}border:none;")
        self.AddTrash.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("D:/Project/Icons/trash.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)

        self.AddTrash.setIcon(icon2)
        self.AddTrash.setIconSize(QtCore.QSize(128, 128))
        self.AddTrash.setObjectName("AddTrash")
        self.AddLight = QtWidgets.QPushButton(parent=self.frame)
        self.AddLight.setGeometry(QtCore.QRect(320, 200, 128, 128))
        self.AddLight.setStyleSheet("QPushButton{\n"
"border:none;\n"
"border-radius: 25px;\n"
"}\n"
"QPushButton:hover {\n"
"  background-color: #ffffbb;\n"
"}border:none;")
        self.AddLight.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("D:/Project/Icons/light.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.AddLight.setIcon(icon3)
        self.AddLight.setIconSize(QtCore.QSize(128, 128))
        self.AddLight.setObjectName("AddLight")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))


class ServiceMenu(ServiceMenu_UI):
    def __init__(self, Form, CabinetMenu):
        super().__init__(Form)
        Form.show()
        self.AddWater.clicked.connect(lambda: self.AddServiceWater(CabinetMenu))
        self.AddGas.clicked.connect(lambda: self.AddServiceGas(CabinetMenu))
        self.AddLight.clicked.connect(lambda: self.AddServiceLight(CabinetMenu))
        self.AddTrash.clicked.connect(lambda: self.AddServiceTrash(CabinetMenu))

    def AddServiceTrash(self, CabinetMenu):
        global TrashFrom
        TrashFrom = QWidget()
        ThashScreen = TrashFormWindow(TrashFrom, CabinetMenu.PersonInfo, CabinetMenu)

    def AddServiceLight(self, CabinetMenu):
        global LightFrom
        LightFrom = QWidget()
        LightScreen = LightFormScreen(LightFrom, CabinetMenu.PersonInfo, CabinetMenu)

    def AddServiceGas(self, CabinetMenu):
        global GasFrom
        GasFrom = QWidget()
        GasScreen = GasFormWindow(GasFrom, CabinetMenu.PersonInfo, CabinetMenu) 

    def AddServiceWater(self, CabinetMenu):
        global WaterFrom
        WaterFrom = QWidget()
        WaterScreen = WaterFormScreen(WaterFrom, CabinetMenu.PersonInfo, CabinetMenu) 
