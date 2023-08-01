import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *


class Communicate(QObject):
	closeApp = pyqtSignal()

class ExampleGUI(QMainWindow):
	def __init__(self):
		super().__init__()
		self.initUI()

	def initUI(self):
		self.c = Communicate()
		self.c.closeApp.connect(self.close)

		self.setWindowTitle('Emitting Signal')
		self.setGeometry(600, 800, 1000, 1000)
		self.show()

	def mousePressEvent(self, e):
		self.c.closeApp.emit()

if __name__ == "__main__":
	app = QApplication(sys.argv)
	ex = ExampleGUI()
	sys.exit(app.exec_())