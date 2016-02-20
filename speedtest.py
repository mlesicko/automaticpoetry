import poem

class form(poem.form):
	def __init__(self):
		self.counter = 0

	def readTweet(self, tweet):
		if (self.counter % 100 ==0):
			print(self.counter)
		self.counter+=1

	def build(self):
		pass
