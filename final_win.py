from PyQt5.QtCore import Qt, QTime, QTimer
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QHBoxLayout, QPushButton, QLineEdit
from instr import *

class FinalWin(QWidget):
    def __init__(self, exp):
        super().__init__()
        self.set_appear()
        self.initUI()
        self.show()
        self.exp = exp
        

    def set_appear(self):
        self.setWindowTitle(txt_titel)
        self.resize(win_width , win_height)
        self.move(win_x , win_y)

    def initUI(self):
        self.hello_text = QLabel(txt_index)
        self.instruction = QLabel(txt_workheart)
        self.layout =  QVBoxLayout()
        self.layout.addWidget(self.hello_text,alignment=Qt.AlignCenter)
        self.layout.addWidget(self.instruction,alignment=Qt.AlignCenter)
        self.setLayout(self.layout)