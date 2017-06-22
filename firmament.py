#!/usr/bin/python3
import sys
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QLabel, QHBoxLayout, QWidget, QApplication, QPushButton
from PyQt5.QtCore import QSize, QTimer, QTime
from PyQt5.QtGui import QIcon
from src.calendar import Clock

# Variables globales
ancho, alto = 800,600 # Ancho y Alto mínimos

class Firmament(QWidget):
	def __init__(self):
		QWidget.__init__(self)
		self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
		self.setStyleSheet("background-color: rgb(255, 255, 255);");
		self.setWindowOpacity(0.7)
		self.setMaximumHeight(30)
		self.resize(QSize(ancho, 30))

		self.layout = QHBoxLayout()
		self.layout.setContentsMargins(0,0,0,0)
		self.layout.setSpacing(0)

		cuarzoBtn = QPushButton()
		cuarzoBtn.setIcon(QIcon("img/cuarzo16x16.png"));
		cuarzoBtn.setIconSize(QSize(16,16));
		cuarzoBtn.setStyleSheet("background-color: rgba(255, 255, 255, 0);")

		self.layout.addWidget(cuarzoBtn,0,QtCore.Qt.AlignLeft)
		self.layout.addWidget(clock,1,QtCore.Qt.AlignCenter)

		self.setLayout(self.layout)
		
if __name__ == "__main__":
	app = QApplication(sys.argv)
	app.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling, True) # Retina
	rec = app.desktop().screenGeometry() # Obtener tamaño de pantalla del usuario
	ancho = rec.width()
	alto = rec.height()
	clock = Clock()	
	mainWin = Firmament()
	mainWin.show()
	sys.exit( app.exec_() )