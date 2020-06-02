import wordtools
from forms.form import Form

class LimerickForm(Form):
	def __init__(self):
		self.data   = {6 : {}, 9 : {}}
		self.pairs = []
		self.triplets = []

	def validate(self,tweet):
		clean = wordtools.clean(tweet)
		syllableCount = wordtools.syllableCount(clean)
		if syllableCount==9 or syllableCount==6:
			rhyme = wordtools.getRhyme(clean[-1])
			if rhyme!=None:
				return (syllableCount, rhyme, clean, tweet)
		return None

	def save(self, record):
		(sylCount, rhyme, cleaned, tweet) = record
		if sylCount==6:
			self.save6(rhyme,cleaned[-1],tweet)
		elif sylCount==9:
			self.save9(rhyme,cleaned[-1],tweet)

	def save6(self, rhyme, last, tweet):
		if rhyme not in self.data[6]:
			self.data[6][rhyme]=[[last,tweet]]
		else:
			match = None
			for potMatch in self.data[6][rhyme]:
				if potMatch[0]!=last:
					match = potMatch
					break
			if match!=None:
				self.data[6][rhyme].remove(match)
				self.pairs.append([potMatch[1],tweet])
			else:
				self.data[6][rhyme].append([last,tweet])
		
	def save9(self, rhyme, last, tweet):
		if rhyme not in self.data[9]:
			self.data[9][rhyme]=[[last,tweet]]
		else:
			match1=None
			match2=None
			for potMatch1 in self.data[9][rhyme]: #This is awful. Should this really be n^2?
				if potMatch1[0]!=last:
					for potMatch2 in self.data[9][rhyme]:
						if potMatch2[0]!=last and potMatch2[0]!=potMatch1[0]:
							match1=potMatch1
							match2=potMatch2
							break
					if match1!=None and match2!=None:
						break
			if match1!=None and match2!=None:
				self.data[9][rhyme].remove(match1)
				self.data[9][rhyme].remove(match2)
				self.triplets.append([match1[1],match2[1],tweet])
			else:
				self.data[9][rhyme].append([last,tweet])

	def build(self):
		if len(self.triplets)>0 and len(self.pairs)>0:
			pair = self.pairs.pop()
			triplet = self.triplets.pop()
			poem = ""
			poem += triplet[0]+"\n"
			poem += triplet[1]+"\n"
			poem +=    pair[0]+"\n"
			poem +=    pair[1]+"\n"
			poem += triplet[2]+"\n"
			return poem
