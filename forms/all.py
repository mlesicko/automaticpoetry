import wordtools
from forms.form import Form

class AllForm(Form):
	def __init__(self):
		self.data=None

	def readTweet(self, tweet):
		clean = wordtools.clean(tweet)
		syl = wordtools.syllableCount(clean)
		if syl>0:
			self.data = tweet

	def build(self):
		if self.data != None:
			verse = self.data
			self.data = None
			return verse
		else:
			return None
