import sys 
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import requests
from bs4 import BeautifulSoup


class MyApp(QWidget):
	def __init__(self):
		super().__init__()
		self.initUI()
		


	def initUI(self):
		self.titleLabel = QLabel('squirrel.Inc', self)
		self.titleLabel.move(50, 50)
		self.titleLabel.setFont(QFont('Helvetica', pointSize = 9, weight = 2))

		self.marketSumLabel = QLabel('Market cap : - won', self)
		self.marketSumLabel.move(50, 110)

		self.marketSumRankLabel = QLabel('Market capitalization rank : powernex - st', self)
		self.marketSumRankLabel.move(50, 140)

		self.currentPrice = QLabel('current Price : - won', self)
		self.currentPrice.move(50, 170)

		self.maxMinPrice = QLabel('52week max | 52week min : - won | - won', self)
		self.maxMinPrice.move(50, 200)

		self.odds = QLabel('Odds : -%', self)
		self.odds.move(50, 230)

		self.openDate = QLabel('Open date : 2023. 1. 1.', self)
		self.openDate.move(50, 260)

		self.openedDate = QLabel('Opened date : -day', self)
		self.openedDate.move(50, 290)

		self.netProfit = QLabel('Sales/Cost/Profits : -won/ -won / -won', self)
		self.netProfit.move(50, 320)

		submitButton = QPushButton('Financial Report', self)
		submitButton.move(30, 430)
		submitButton.resize(340, 50)
		submitButton.clicked.connect(self.write)

		excelButton = QPushButton('Excel Report write', self)
		excelButton.move(30, 490)
		excelButton.resize(340, 50)
		excelButton.clicked.connect(self.excel)

		quitButton = QPushButton('Program exit', self)
		quitButton.move(30, 550)
		quitButton.resize(340, 50)
		quitButton.clicked.connect(self.close)

		self.representImage = QLabel(self)
		self.representImage.setPixmap(QPixmap('/squirrel.jpg').scaled(50, 24))
		self.representImage.move(10, 10)

		self.setWindowTitle('Financial Report')
		self.setGeometry(1000, 300, 500, 640)
		self.show()


	def write(self):
		url = 'http://paullab.co.kr/stock.html'
		response = requests.get(url)
		response.encoding = 'utf-8'
		html = response.text
		soup = BeautifulSoup(html, 'html.parser')

		values = soup.select('.tables td')

		self.marketSumLabel.setText(f'Market cap : {values[0].text}')
		self.marketSumLabel.resize(400, 20)
		
		self.marketSumRankLabel.setText(f'Market capitalization rank : {values[1].text}')
		self.marketSumRankLabel.resize(400, 20)

		self.currentPrice.setText(f'current Price : {values[3].text}')
		self.currentPrice.resize(400, 20)

		s = values[4].text.strip().replace('\n', '').split('1')
		self.maxMinPrice.setText(f'52week max | 52week min : {s[0]} | {s[1]}')
		self.maxMinPrice.rexize(400, 20)

		i = values[5].text.strip()
		self.odds.setText(f'Odds : {i}')
		self.odds.resize(400, 20)

		self.netProfit.setText(f'Sales/Cost/Profits : \n{values[6].text}\n / {values[7].text}\n / {values[8].text}')
		self.netProfit.resize(400, 80)

	def excel(self):
		pass
	
	def close(self):
		return QCoreApplication.instance().quit()



app = QApplication(sys.argv)
ex = MyApp()
app.exec_()









		
		
		

