import wordtools
import poem

class form(poem.form):
	def __init__(self):
		self.line = ""
		self.ALLITERATIVE_FACTOR=.4

	def validate(self,tweet):
		clean = wordtools.clean(tweet)
		if not wordtools.validate(clean):
			return None
		initials = {}
		for i in range(len(clean)):
			initial = wordtools.getInitialSound(clean[i])
			if initial in initials:
				initials[initial][0]+=1
			else:
				initials[initial]=[1,False,False]
			if i < len(clean)/2:
				initials[initial][1]=True
			else:
				initials[initial][2]=True
		if len(initials)==0:
			return None
		if self.existsUsableSound(initials,len(clean)*self.ALLITERATIVE_FACTOR):
			return tweet
		else:
			return None
			
	def existsUsableSound(self,a,minCount):
		return  len(list(s for s in a if a[s][0]>=max(3,minCount) and a[s][1] and a[s][2]))>0

	def save(self,tweet):
		self.line = tweet

	def build(self):
		if self.line == "":
			return None
		line = self.line
		self.line = ""
		return line
