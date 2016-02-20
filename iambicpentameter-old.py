import wordtools
import poem

class form(poem.form):
	def __init__(self):
		self.line = ""

	def validate(self,tweet):
		cleaned = wordtools.clean(tweet)
		meter = wordtools.getMeter(cleaned)
		if meter!=None and self.isIambicPentameter(meter):
			return tweet
		else:
			return None

	def save(self,tweet):
		self.line = tweet

	def build(self):
		if self.line != "":
			line = self.line
			self.line = ""
			return line

	def isIambicPentameter(self,meter):
		if len(meter)!=10 and len(meter)!=11:
			return False
		if len("".join(c for c in meter if c==1))!=5:
			return False
		if "11" in meter:
			return False
		return True
