import wordtools
import poem

class form(poem.form):
	def __init__(self):
		self.data=[{},[]]

	def validate(self,tweet):
		cleaned = wordtools.clean(tweet)
		if wordtools.validate(cleaned):
			return [cleaned,tweet]

	def save(self,cleaned):
		if len(cleaned[0])<=10:
			self.saveTweet(cleaned[1])
		for word in cleaned[0]:
			if len(word)>=4:
				self.data[1].append(word)

	def saveTweet(self,tweet):
		if tweet[0] in self.data[0]:
			self.data[0][tweet[0]].append(tweet)
		else:
			self.data[0][tweet[0]]=[tweet]

	def build(self):
		for i in range(len(self.data[1])):
			poem = []
			for c in self.data[1][i]:
				if c in self.data[0] and len(self.data[0][c])>0:
					poem.append(self.data[0][c].pop(0))
				else:
					break
			if len(poem)<len(self.data[1][i]):
				for line in poem:
					self.saveTweet(line)
			else:
				self.data[1].pop(i)
				return "\n".join(poem)+"\n"
		return None
