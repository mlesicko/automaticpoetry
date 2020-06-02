import wordtools
from forms.form import Form

class HaikuForm(Form):
	syllables = "syllableCount"
	text = "text"

	def __init__(self):
		self.data={}
		self.data[5]=[]
		self.data[7]=[]

	def validate(self,tweet):
		clean = wordtools.clean(tweet)
		syllableCount = wordtools.syllableCount(clean)
		if syllableCount==7 or syllableCount==5:
			return {self.syllables:syllableCount, self.text:tweet}
		else:
			return None

	def save(self,cleaned):
		self.data[cleaned[self.syllables]].append(cleaned[self.text])
	
	def build(self):
		if len(self.data[5])>=2 and len(self.data[7])>=1:
			poem = self.data[5].pop(0)+"\n"
			poem +=self.data[7].pop(0)+"\n"
			poem +=self.data[5].pop(0)+"\n"
			return poem
		else:
			return None
