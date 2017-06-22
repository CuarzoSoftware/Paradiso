#!/usr/bin/python3
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QWidget, QLabel, QSizePolicy
from PyQt5.QtCore import QTimer, QTime, QDate

class Clock(QLabel):
	def __init__(self):
		super(Clock, self).__init__()
		self.timer = QTimer()
		self.timer.timeout.connect(self.Time)
		self.timer.start(1000)

	def Time(self):
		fecha = QDate.currentDate().toString("ddd MMM d")
		sdia = fecha.split(".")[0]
		smes = fecha.split(".")[1]
		ndia = fecha.split(".")[2]
		hora = QTime.currentTime().toString("hh:mm")
		self.setText(sdia + smes + ndia + ", " + hora)