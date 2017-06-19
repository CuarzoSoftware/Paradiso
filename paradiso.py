import sys
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QLabel, QGridLayout, QWidget, QApplication
from PyQt5.QtCore import QSize    

# Variables globales

ancho, alto = 800,600 # Ancho y Alto mínimos

class Paradiso(QMainWindow):
	def __init__(self):
		QMainWindow.__init__(self)
		self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
		self.resize(QSize(ancho, 32))
		self.setWindowTitle("Heaven")
		
if __name__ == "__main__":
	app = QApplication(sys.argv)
	rec = app.desktop().screenGeometry()
	ancho = rec.width()
	alto = rec.height()
	mainWin = Paradiso()
	mainWin.show()
	sys.exit( app.exec_() )