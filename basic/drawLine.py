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
		qp.setPen(QPen(Qt.blue, 7))
		qp.drawLine(104, 156, 134, 216)
		qp.setPen(QPen(Qt.blue, 8))
		qp.drawLine(173, 142, 134, 216)
		qp.setPen(QPen(Qt.blue, 8))
		qp.drawLine(150, 348, 134, 216)

		qp.setPen(QPen(Qt.yellow, 7))
		qp.drawLine(233, 163, 322, 163)
		qp.setPen(QPen(Qt.yellow, 7))
		qp.drawLine(233, 163, 233, 331)
		qp.setPen(QPen(Qt.yellow, 7))
		qp.drawLine(233, 238, 322, 238)
		qp.setPen(QPen(Qt.yellow, 7))
		qp.drawLine(233, 326, 329, 326)

		qp.setPen(QPen(Qt.red, 7))
		qp.drawLine(413, 163, 502, 163)
		qp.setPen(QPen(Qt.red, 7))
		qp.drawLine(413, 163, 413, 331)
		qp.setPen(QPen(Qt.red, 7))
		qp.drawLine(413, 238, 502, 238)
		qp.setPen(QPen(Qt.red, 7))
		qp.drawLine(413, 326, 509, 326)




if __name__ == "__main__":
	app = QApplication(sys.argv)
	ex = MyApp()
	sys.exit(app.exec_())