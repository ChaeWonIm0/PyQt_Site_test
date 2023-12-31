import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5 import uic

import random
class MyApp(QWidget):

    def __init__(self):
        super().__init__()

        self.random_x = 1
        self.random_y = 1
        
        self.loadImage()
     

        self.initUI()

    def initUI(self):

        x = 0
        y = 0

        self.text = 'x: {0}, y:{1}'.format(x, y)
        self.label = QLabel(self.text, self)
        self.label.move(10, 0)

        self.setMouseTracking(True)

        self.score = 0
        self.scoretext = 'score : {0}'.format(self.score)
        self.scorelabel = QLabel(str(self.scoretext), self)
        self.scorelabel.move(250, 0)

        
        self.setWindowTitle('Catch the squirral')
        self.setGeometry(0, 0, 2780, 1670)
        self.timer = QBasicTimer()
        self.onActivated()
        
        self.show()

    def loadImage(self):   
        #squirrel summit
        self.monster_img = QLabel(self)
        self.monster_img.setPixmap(QPixmap('C:\github\squirrel.png').scaled(110,50))
        self.monster_img.move(self.random_x, self.random_y)

    def paintEvent(self, e):
        qp = QPainter()
        qp.begin(self)
        self.drawRect(qp)
        qp.end()

    def drawRect(self ,qp):
        qp.setBrush(QColor(255, 0, 0, 1290))
        qp.drawRect(self.random_x, self.random_y, 100, 40)
        
    
    def timerEvent(self, argEvent):
        del argEvent
        self.random_x  = random.randint(0, 500)
        self.random_y  = random.randint(0, 500)
        self.monster_img.move(self.random_x, self.random_y)
        self.repaint()

    def onActivated(self):
        self.timer.stop()
        self.resolution = 1
        self.setWindowTitle('event handler')
        self.setGeometry(600, 500, 1000, 1000)
        self.timer.start(300, self)

    def mouseMoveEvent(self, e):
        x = e.x()
        y = e.y()

        text = 'x: {0}, y: {1}'.format(x, y)
        self.label.setText(text)
        self.label.setStyleSheet("color : black;"
                                 "font-size: 30px;")
        if x <= self.random_x + 120 and x >= self.random_x and y <= self.random_y + 60 and y >= self.random_y:
            self.score += 10
            self.scoretext = f'score : {self.score}'
            self.scorelabel.setText(self.scoretext)
            self.scorelabel.adjustSize()
            
        else:
            pass
        
        self.scorelabel.setText(self.scoretext)
        self.scorelabel.setStyleSheet("color : black;"
                                 "font-size: 30px;")
        self.label.adjustSize()
        self.scorelabel.adjustSize()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = MyApp()
    app.setStyle("WindowsVista")
    sys.exit(app.exec_())
