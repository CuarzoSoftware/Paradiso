#!/usr/bin/python3
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
		self.setStyleSheet("background-color: rgba(255, 255, 255,1);");
		self.setWindowOpacity(0.8)
		self.resize(QSize(ancho, 32))
		
if __name__ == "__main__":
	app = QApplication(sys.argv)
	app.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling, True) # Retina
	rec = app.desktop().screenGeometry() # Obtener tamaño de pantalla del usuario
	ancho = rec.width()
	alto = rec.height()
	mainWin = Paradiso()
	mainWin.show()
	sys.exit( app.exec_() )