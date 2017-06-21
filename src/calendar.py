#!/usr/bin/python3
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import (
	QWidget,
	QLabel
)

from PyQt5.QtCore import (
	QTimer,
	QTime
)

class Clock(QLabel):
	def __init__(self):
		super(Clock, self).__init__()
		self.timer = QTimer()
		self.timer.timeout.connect(self.Time)
		self.timer.start(1000)

	def Time(self):
		time = QTime.currentTime().toString()
		self.setText(time)