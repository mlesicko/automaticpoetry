import wordtools
import poem

class form(poem.form):
	def __init__(self):
		self.data={}
		self.data[5]=[]
		self.data[7]=[]

	def validate(self,tweet):
		clean = wordtools.clean(tweet)
		syllableCount = wordtools.syllableCount(clean)
		if syllableCount==7 or syllableCount==5:
			return [syllableCount, tweet]
		else:
			return None

	def save(self,cleaned):
		self.data[cleaned[0]].append(cleaned[1])
	
	def build(self):
		if len(self.data[5])>=2 and len(self.data[7])>=1:
			poem = self.data[5].pop(0)+"\n"
			poem +=self.data[7].pop(0)+"\n"
			poem +=self.data[5].pop(0)+"\n"
			return poem
		else:
			return None
