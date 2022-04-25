from PyQt6.QtWidgets import QApplication, QWidget
import sys
from PyQt6.QtCore import Qt
from PyQt6 import uic

class UI(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('form.ui', self)
        self.pushButton.clicked.connect(self.prt)

    def prt(self):
        print('hthfgdfx')

app = QApplication(sys.argv)
window = UI()
window.show()
app.exec()
