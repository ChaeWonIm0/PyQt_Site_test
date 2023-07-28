import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *


class MyApp(QWidget):
	def __init__(self):
		super().__init__()
		self.initUI()

	def initUI(self):
		lcd = QLCDNumber(self)
		dial = QDial(self)

		lcd.setStyleSheet("QLCDNumber {background-color:skyblue;}")
		dial.setStyleSheet("QDial {background-color : white;}")
		vbox = QVBoxLayout()
		vbox.addWidget(lcd)
		vbox.addWidget(dial)
	
		self.setLayout(vbox)

		dial.valueChanged.connect(lcd.display)

		self.setWindowTitle('Signal and slot')
		self.setGeometry(800, 600, 500, 500)
		self.show()

if __name__ == "__main__":
	app = QApplication(sys.argv)
	app.setStyle("GTK+")
	ex = MyApp()
	sys.exit(app.exec_())
