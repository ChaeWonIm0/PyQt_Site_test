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
		self.setGeometry(600, 800, 1000, 1000)
		self.setWindowTitle('line')
		self.show()
		
	def paintEvent(self, e):
		qp = QPainter()
		qp.begin(self)
		self.draw_line(qp)
		qp.end()

	def draw_line(self, qp):
		qp.setPen(QPen(Qt.blue, 8))
		qp.drawLine(30, 230, 200, 50)

		qp.setPen(QPen(Qt.green, 8))
		qp.drawLine(100, 230, 270, 50)

		qp.setPen(QPen(Qt.red, 8))
		qp.drawLine(170, 230, 340, 50)




if __name__ == "__main__":
	app = QApplication(sys.argv)
	ex = MyApp()
	sys.exit(app.exec_())