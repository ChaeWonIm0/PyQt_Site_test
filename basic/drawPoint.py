
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import random

class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(100, 200, 1000, 1000)
        self.setWindowTitle('Point')
        self.show()

    def paintEvent(self, e):
        qp = QPainter()
        qp.begin(self)
        self.draw_point(qp)
        qp.end()

    def draw_point(self, qp):
        pen = QPen()
        colors = ['#D83C5F', '#3CD88F', '#AA5CE3',
                  '#DF4A26', '#AE85F6', '#F7A82E',
                  '#DF4A26', '#AE85F6', '#F7A82E',
                  '#DF4A26', '#AE85F6', '#F7A82E',
                  '#406CF3', '#E9F229', '#29ACF2',
                  '#456CD3', '#89F209', '#21ACA2',]
        for i in range(200):
            pen.setWidth(random.randint(20, 40))
            pen.setColor(QColor(random.choice(colors)))
            qp.setPen(pen)
            rand_x = 100 * random.randint(1, 200)
            rand_y = 100 * random.randint(1, 200)
            print(self.width(), self.height())
            qp.drawPoint(self.width() / 25 + rand_x, self.height()/ 25 + rand_y)



if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())




