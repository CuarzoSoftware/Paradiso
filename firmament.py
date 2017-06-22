#!/usr/bin/python3
import sys
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QLabel, QWidget, QApplication, QPushButton, QGridLayout,QGroupBox,QHBoxLayout
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

		self.layout = QGridLayout()
		self.layout.setContentsMargins(0,0,0,0)
		self.layout.setSpacing(0)

		self.cuarzoBtn = QPushButton()
		self.batteryStatus = QPushButton()
		self.wifiStatus = QPushButton()
		self.volumeControl = QPushButton()
		self.shutdownControl = QPushButton()

		self.cuarzoBtn.setIcon(QIcon("src/img/cuarzo_16x16.png"))
		self.batteryStatus.setIcon(QIcon("src/img/battery-full.png"))
		self.wifiStatus.setIcon(QIcon("src/img/network-wireless-signal-good.png"))
		self.volumeControl.setIcon(QIcon("src/img/audio-volume-high.png"))
		self.shutdownControl.setIcon(QIcon("src/img/system-devices-panel.png"))

		self.cuarzoBtn.setIconSize(QSize(16,16))
		self.batteryStatus.setIconSize(QSize(22,22))
		self.wifiStatus.setIconSize(QSize(22,22))
		self.volumeControl.setIconSize(QSize(22,22))
		self.shutdownControl.setIconSize(QSize(22,22))

		self.cuarzoBtn.setStyleSheet("background-color: rgba(255, 255, 255, 0);")
		self.batteryStatus.setStyleSheet("background-color: rgba(255, 255, 255, 0);")		
		self.wifiStatus.setStyleSheet("background-color: rgba(255, 255, 255, 0);")
		self.volumeControl.setStyleSheet("background-color: rgba(255, 255, 255, 0);")
		self.shutdownControl.setStyleSheet("background-color: rgba(255, 255, 255, 0);")

		self.btnGroup = QWidget()
		self.topicons = QHBoxLayout()
		self.topicons.setContentsMargins(0,0,0,0)
		self.topicons.setSpacing(0)
		self.topicons.addWidget(self.wifiStatus)
		self.topicons.addWidget(self.volumeControl)
		self.topicons.addWidget(self.batteryStatus)
		self.topicons.addWidget(self.shutdownControl)
		self.btnGroup.setLayout(self.topicons)

		self.layout.addWidget(self.cuarzoBtn,0,0,QtCore.Qt.AlignLeft)
		self.layout.addWidget(clock,0,1,QtCore.Qt.AlignCenter)
		self.layout.addWidget(self.btnGroup,0,2, QtCore.Qt.AlignRight)

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