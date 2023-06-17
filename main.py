from PyQt6 import QtWidgets
from PyQt6.QtWidgets import QApplication, QWidget
from StartScreen import StartScreen

app = QApplication([])
FormStartScreen = QWidget()
StartScr = StartScreen(FormStartScreen)
app.exec()
