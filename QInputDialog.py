
import sys
from PyQt5.QtWidgets import *

class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.btn = QPushButton('Dialog', self)
        self.btn.move(10, 30)
        self.btn.clicked.connect(self.showDialog)

        self.le = QLineEdit(self)
        self.le.move(200, 35)

        self.setWindowTitle('input dialog')
        self.setGeometry(600, 600, 600, 600)
        self.show()

    def showDialog(self):
        text, ok = QInputDialog.getText(self, 'input dialog', 'Enter your name :')
        if ok:
            self.le.setText(str(text))
        print(str(text))

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())