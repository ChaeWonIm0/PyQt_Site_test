import sys
from PyQt5.QtWidgets import *

class MyApp(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        lcd = QLCDNumber(self)
        dial = QDial(self)
        btn1 = QPushButton('GO Big', self)
        btn2 = QPushButton('GO Small', self)
        
        hbox = QHBoxLayout()
        hbox.addWidget(btn1)
        hbox.addWidget(btn2)

        vbox = QVBoxLayout()
        vbox.addWidget(lcd)
        vbox.addWidget(dial)
        vbox.addLayout(hbox)
        self.setLayout(vbox)

        dial.valueChanged.connect(lcd.display)
        btn1.clicked.connect(self.resizeBig)
        btn2.clicked.connect(self.resizeSmall)

        self.setWindowTitle('Signal and slot')
        self.setGeometry(0, 0, 600, 600)
        self.show()

    def resizeBig(self):
        self.resize(2970, 1670)
    def resizeSmall(self):
        self.resize(200, 250)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = MyApp()
    app.setStyle("WindowsVista")
    sys.exit(app.exec_())
