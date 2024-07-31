from PyQt5.QtCore import Qt, QTime, QTimer
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QHBoxLayout, QPushButton, QLineEdit
from instr import *
from final_win import FinalWin

class Experiment():
    def __init__(self, age, test1, test2, test3):
        self.le2 = int(age)
        self.le3 = test1
        self.le4 = test2
        self.le5 = test3
    

class SecondWin(QWidget):
    def __init__(self):
        super().__init__()
        self.set_appear()
        self.initUI()
        self.connects()
        self.show()
    
    def next_click(self):
        self.hide()
        self.exp = Experiment (self.le2.text(),self.le3.text(),self.le4.text(),self.le5.text())
        self.fw = FinalWin(self.exp)


    def set_appear(self):
        self.setWindowTitle(txt_titel)
        self.resize(win_width , win_height)
        self.move(win_x , win_y)   
    
    def timer_test(self):
        global time
        time = QTime(0, 0, 15)
        self.timer = QTimer()
        self.timer.timeout.connect(self.timer1Event)
        self.timer.start(1000)
    
    def timer1Event(self):
        global time
        time = time.addSecs(-1)
        self.l6.setText(time.toString("hh:mm:ss"))  
        self.l6.setFont(QFont("Times", 36, QFont.Bold))
        self.l6.setStyleSheet("color: rgb(0,0,0)")
        if time.toString('hh:mm:ss') == "00:00:00":
            self.timer.stop()

    def timer_sits(self):
        global time
        time = QTime(0, 0, 30)
        self.timer = QTimer()
        self.timer.timeout.connect(self.timer2Event)
        self.timer.start(1500)


    def timer2Event(self):
        global time
        time = time.addSecs(-1)
        self.l6.setText(time.toString("hh:mm:ss")[6:8])  
        self.l6.setFont(QFont("Times", 36, QFont.Bold))
        self.l6.setStyleSheet("color: rgb(0,0,0)")
        if time.toString('hh:mm:ss') == "00:00:00":
            self.timer.stop()

    def timer_final(self):
        global time
        time = QTime(0, 1, 0)
        self.timer = QTimer()
        self.timer.timeout.connect(self.timer3Event)
        self.timer.start(1000)
    
    def timer3Event(self):
        global time
        time = time.addSecs(-1)
        self.l6.setText(time.toString("hh:mm:ss"))
        self.l6.setFont(QFont("Times", 36, QFont.Bold))
        if int(time.toString('hh:mm:ss')[6:8])>= 45:
            self.l6.setStyleSheet('color: rgb(0,255,0)')
        elif int(time.toString('hh:mm:ss')[6:8])>= 15:
            self.l6.setStyleSheet('color: rgb(0,255,0)')
        else :
            self.l6.setStyleSheet('color: rgb(0,0,0)')
        
        if time.toString('hh:mm:ss') == "00:00:00":
            self.timer.stop()


    def initUI(self):
        self.h_linr = QHBoxLayout()
        self.r_linr = QVBoxLayout()
        self.l_linr = QVBoxLayout()
        self.l1 =QLabel(label1)
        self.l2 =QLabel(label2)
        self.l3 =QLabel(label3)
        self.l4 =QLabel(label4)
        self.l5 =QLabel(label5)
        self.l6 =QLabel(label6)
        self.b1 = QPushButton(button1)
        self.b2 = QPushButton(button2)
        self.b3 = QPushButton(button3)
        self.b4 = QPushButton(button4)
        self.le1 = QLineEdit()
        self.le2 = QLineEdit()
        self.le3 = QLineEdit()
        self.le4 = QLineEdit()
        self.le5 = QLineEdit()

        self.l_linr.addWidget(self.l1,alignment=Qt.AlignLeft) 
        self.l_linr.addWidget(self.le1,alignment=Qt.AlignLeft)  
        self.l_linr.addWidget(self.l2,alignment=Qt.AlignLeft) 
        self.l_linr.addWidget(self.le2,alignment=Qt.AlignLeft) 
        self.l_linr.addWidget(self.l3,alignment=Qt.AlignLeft) 
        self.l_linr.addWidget(self.b1,alignment=Qt.AlignLeft) 
        self.l_linr.addWidget(self.le3,alignment=Qt.AlignLeft) 
        self.l_linr.addWidget(self.l4,alignment=Qt.AlignLeft) 
        self.l_linr.addWidget(self.b2,alignment=Qt.AlignLeft) 
        self.l_linr.addWidget(self.l5,alignment=Qt.AlignLeft) 
        self.l_linr.addWidget(self.b3,alignment=Qt.AlignLeft) 
        self.l_linr.addWidget(self.le4,alignment=Qt.AlignLeft) 
        self.l_linr.addWidget(self.le5,alignment=Qt.AlignLeft) 
        self.r_linr.addWidget(self.l6,alignment=Qt.AlignRight)
        self.l_linr.addWidget(self.b4,alignment=Qt.AlignCenter)

        self.h_linr.addLayout(self.l_linr)
        self.h_linr.addLayout(self.r_linr)
        self.setLayout(self.h_linr)


    def connects(self):
        self.b1.clicked.connect(self.timer_test)
        self.b2.clicked.connect(self.timer_sits)
        self.b3.clicked.connect(self.timer_final)
        self.b4.clicked.connect(self.next_click)