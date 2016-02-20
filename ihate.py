import wordtools
import poem

class form(poem.form):
	def __init__(self):
		self.data=None
		self.testString="I HATE"

	def readTweet(self, tweet):
		cleaned = wordtools.clean(tweet)
		if cleaned[:len(self.testString)] == self.testString:
			self.data = tweet

	def build(self):
		if self.data != None:
			verse = self.data
			self.data = None
			return verse
		else:
			return None
