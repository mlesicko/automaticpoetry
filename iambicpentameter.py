import wordtools
import poem

class form(poem.form):
	rhyme = "rhyme"
	clean = "clean"
	text = "text"

	def __init__(self):
		self.data = {}
		self.toCheck = ""

	def validate(self,tweet):
		cleaned = wordtools.clean(tweet)
		meter = wordtools.getMeter(cleaned)
		if meter!=None and self.isIambicPentameter(meter):
			rhyme = wordtools.getRhyme(cleaned[-1])
			if rhyme!=None:
				return {self.rhyme:rhyme,self.clean:cleaned,self.text:tweet}
		else:
			return None

	def save(self,cleaned):
		if cleaned[self.rhyme] in self.data:
			self.data[cleaned[self.rhyme]].append(cleaned)
			self.toCheck = cleaned[self.rhyme]
		else:
			self.data[cleaned[self.rhyme]] = [cleaned]

	def build(self):
		if self.toCheck != "":
			toCheck = self.toCheck
			self.toCheck = ""
			if len(self.data[toCheck])>=2:
				candidate1 = self.data[toCheck].pop()
				candidate2 = None
				for candidate in self.data[toCheck]:
					if self.validPair(candidate1,candidate):
						candidate2 = candidate
						break
				if candidate2!=None:
					self.data[toCheck].remove(candidate2)
					return candidate1[self.text]+"\n"+candidate2[self.text]
				else:
					self.data[toCheck].append(candidate1)
					return None

	def isIambicPentameter(self,meter):
		"""Based on a description of iambic pentameter given by
			Noam Chomsky. The only rule is that traditionally
			weak positions may not be stressed if the neighboring
			strong positions are also unstressed.
			This also supports 'feminine' endings, where there
			is an eleventh syllable, which must be unstressed."""
		if len(meter)!=10 and len(meter)!=11:
			return False
		if len(meter)==11 and meter[10]=="1":
			return False
		for i in range(0,len(meter),2):
			if meter[i] == "1":
				if (i-1 < 0 or meter[i-1]=="0") and (i+1 >= len(meter) or meter[i+1]=="0"):
					return False
		return True
					
	def validPair(self,candidate1,candidate2):
		return candidate1[self.clean][-1] != candidate2[self.clean][-1]
