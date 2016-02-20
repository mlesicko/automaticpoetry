import wordtools
import poem

class form(poem.form):
	rhyme = "rhyme"
	syllables = "syllables"
	clean = "clean"
	text = "text"

	def __init__(self):
		self.data={}
		self.toCheck = ""

	def validate(self,tweet):
		clean = wordtools.clean(tweet)
		syl = wordtools.syllableCount(clean)
		if syl>0:
			rhyme = wordtools.getRhyme(clean[-1])
			if rhyme!= None:
				return {self.rhyme:rhyme,self.syllables:syl,self.clean:clean,self.text:tweet}
		return None

	def save(self,cleaned):
		if cleaned[self.rhyme] in self.data:
			self.data[cleaned[self.rhyme]].append(cleaned)
			self.toCheck = cleaned[self.rhyme]
		else:
			self.data[cleaned[self.rhyme]] = [cleaned]

	def build(self):
		if self.toCheck!="":
			toCheck = self.toCheck
			self.toCheck = ""
			if len(self.data[toCheck])>=2:
				candidate1 = self.data[toCheck].pop()
				candidate2 = None
				for candidate in self.data[toCheck]:
					if self.validPair(candidate1,candidate):
						candidate2=candidate
						break
				if candidate2!=None:
					self.data[toCheck].remove(candidate2)
					return candidate1[self.text]+"\n"+candidate2[self.text]
				else:
					self.data[toCheck].append(candidate1)
					return None
					
		else:
			return None

	def validPair(self,candidate1,candidate2):
		if abs(candidate1[self.syllables]-candidate2[self.syllables])>4: #Not similar length
			return False
		if candidate1[self.clean][-1] == candidate2[self.clean][-1]: #Same word rhyme
			return False
		return True
