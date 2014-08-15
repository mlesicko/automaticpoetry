import wordtools
import poem

class form(poem.form):
	def __init__(self):
		self.data= [{},[]]


	def readTweet(self, tweet):
		cleaned = wordtools.clean(tweet)
		if not wordtools.validate(cleaned) or not len(cleaned)>0:
			return
		if cleaned[0] in self.data[0]:
			self.data[0][cleaned[0]].append(tweet)
		else:
			self.data[0][cleaned[0]]=[tweet]
		if len(self.data[0][cleaned[0]])==4:
			self.data[1] = self.data[0][cleaned[0]]
			self.data[0][cleaned[0]]=[]

	def build(self):
		if len(self.data[1])>0:
			verse = self.data[1]
			self.data[1]=[]
			return "\n".join(verse)+"\n"
		else:
			return None
