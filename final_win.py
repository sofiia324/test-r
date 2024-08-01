from PyQt5.QtCore import Qt, QTime, QTimer
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QHBoxLayout, QPushButton, QLineEdit
from instr import *

class FinalWin(QWidget):
    def __init__(self, exp):
        super().__init__()
        self.exp = exp
        self.set_appear()
        self.initUI()
        self.show()
        
        

    def set_appear(self):
        self.setWindowTitle(txt_titel)
        self.resize(win_width , win_height)
        self.move(win_x , win_y)

    def results(self):
        self.index = (4*(int(self.exp.le2)+int(self.exp.le3)+int(self.exp.le4))-200)/10
        if self.exp.le2 >= 15:
            if self.index >= 15:
                return txt_res1
            elif self.index<15 and self.index>=11:
                return txt_res2
            elif self.index<11 and self.index>=6:
                return txt_res3
            elif self.index<6 and self.index>=0.5:
                return txt_res4
            elif self.index<0.4 :
                return txt_res5

        if self.exp.le2 == 11 and self.exp.le2 == 12:
            if self.index >= 18:
                return txt_res1
            elif self.index<18 and self.index>=14:
                return txt_res2
            elif self.index<14 and self.index>=9:
                return txt_res3
            elif self.index<9 and self.index>=3.5:
                return txt_res4
            elif self.index<35 :
                return txt_res5
            
        if self.exp.le2 == 13 and self.exp.le2 == 14:
            if self.index >= 16.5:
                return txt_res1
            elif self.index<16.5 and self.index==12.5:
                return txt_res2
            elif self.index<12.5 and self.index>=7.5:
                return txt_res3
            elif self.index<7.5 and self.index>=2:
                return txt_res4
            elif self.index<2 :
                return txt_res5
            
        if self.exp.le2 == 9 and self.exp.le2 == 10:
            if self.index >= 19.5:
                return txt_res1
            elif self.index<19.5 and self.index>=15.5:
                return txt_res2
            elif self.index<15.5 and self.index>=10.5:
                return txt_res3
            elif self.index<10.5 and self.index>=5:
                return txt_res4
            elif self.index<5 :
                return txt_res5
            
        if self.exp.le2 == 7 and self.exp.le2 == 8:
            if self.index >= 21:
                return txt_res1
            elif self.index<21 and self.index>=17:
                return txt_res2
            elif self.index<17 and self.index>=12:
                return txt_res3
            elif self.index<12 and self.index>=6.5:
                return txt_res4
            elif self.index<6.5 :
                return txt_res5

    def initUI(self):
        self.work_text = QLabel(txt_workheart + self.results())
        self.index_text = QLabel(txt_index + str(self.index))
        self.layout =  QVBoxLayout()
        self.layout.addWidget(self.work_text, alignment=Qt.AlignCenter)
        self.layout.addWidget(self.index_text, alignment=Qt.AlignCenter)
        self.setLayout(self.layout)