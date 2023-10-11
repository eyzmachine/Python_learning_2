import time

class Loggable:
	def log(self, msg):
		print(str(time.ctime()) + ": " + str(msg))

class LoggableList(Loggable, list):
	def append(self, obj):
		super().append(obj)
		self.log(obj)

q = LoggableList()
q.append("q")