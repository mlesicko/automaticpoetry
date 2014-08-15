import wordtools
import poem

class form(poem.form):
	def __init__(self):
		self.data={}
		self.msg = ""

	def validate(self,tweet):
		clean = wordtools.clean(tweet)
		syl = wordtools.syllableCount(clean)
		if syl>0:
			rhyme = wordtools.getRhyme(clean[-1])
			if rhyme!= None:
				return [rhyme,syl,clean,tweet]
		return None

	def save(self,cleaned):
		if cleaned[0] in self.data:
			self.data[cleaned[0]].append(cleaned[1:])
			self.msg = cleaned[0]
		else:
			self.data[cleaned[0]] = [cleaned[1:]]

	def build(self):
		if self.msg!="":
			msg = self.msg
			self.msg = ""
			if len(self.data[msg])>=2:
				candidate1 = self.data[msg].pop()
				candidate2 = None
				for candidate in self.data[msg]:
					if validPair(candidate1,candidate):
						candidate2=candidate
						break
				if candidate2!=None:
					self.data[msg].remove(candidate2)
					return candidate1[-1]+"\n"+candidate2[-1]
				return None
					
		else:
			return None

def validPair(candidate1,candidate2):
	if abs(candidate1[0]-candidate2[0])>4: #Not similar length
		return False
	if candidate1[1][-1] == candidate2[1][-1]: #Same word rhyme
		return False
	return True
