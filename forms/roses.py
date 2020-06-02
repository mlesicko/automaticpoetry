import wordtools
from forms.form import Form

class RosesForm(Form):
	def __init__(self):
		self.data = None
		self.testRhyme = wordtools.getRhyme("BLUE")

	def readTweet(self, tweet):
		cleaned = wordtools.clean(tweet)
		syllableCount = wordtools.syllableCount(cleaned)
		if syllableCount > 0 and syllableCount < 20:
			rhyme = wordtools.getRhyme(cleaned[-1])
			if rhyme == self.testRhyme:
				self.data = tweet

	def build(self):
		if self.data != None:
			verse = self.data
			self.data = None
			return "Roses are red,\nViolets are blue,\n" + verse + "\n"
		else :
			return None
			
