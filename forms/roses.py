import math
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
			verse = self.data.split()
			midpoint = math.ceil(len(verse)/2)
			self.data = None
			return ("Roses are red,\n"
				"Violets are blue,\n"
				+ " ".join(verse[:midpoint]) + "\n"
				+ " ".join(verse[midpoint:]) + "\n")
		else :
			return None
			
