from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtWidgets import QMainWindow, QWidget


class Allert_UI(QMainWindow):
    def __init__(self, Form, price):
        super().__init__()
        Form.setObjectName("Form")
        Form.resize(600, 240)
        Form.setFixedSize(QtCore.QSize(600, 240))


        self.frame = QtWidgets.QFrame(parent=Form)
        self.frame.setGeometry(QtCore.QRect(0, 0, 600, 240))
        self.frame.setStyleSheet("background-color: rgb(255, 255, 241);")
        self.frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame.setObjectName("frame")

        self.textEdit = QtWidgets.QTextEdit(parent=self.frame)
        self.textEdit.setGeometry(QtCore.QRect(50, 70, 311, 30))
        self.textEdit.setStyleSheet("border:none;")
        self.textEdit.setObjectName("textEdit")

        self.label = QtWidgets.QLabel(parent=self.frame)
        self.label.setGeometry(QtCore.QRect(400, 68, 101, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setText("")
        self.label.setObjectName("label")
        self.label.setText(str(price))

        self.pushButton = QtWidgets.QPushButton(parent=self.frame)
        self.pushButton.setGeometry(QtCore.QRect(240, 140, 131, 51))
        self.pushButton.setStyleSheet("QPushButton {\n"
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
        self.pushButton.setObjectName("pushButton")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.textEdit.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">Ви успішно сплатили послуги на суму:</span></p></body></html>"))
        self.pushButton.setText(_translate("Form", "OK"))


class AllertWindow(Allert_UI):
    def __init__(self, Form, price):
        super().__init__(Form, price)
        Form.show()
        self.pushButton.clicked.connect(lambda: self.OKClicked(Form))
    
    def OKClicked(self, Form):
        Form.close()
