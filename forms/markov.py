import wordtools
import random
from forms.form import Form

class MarkovForm(Form):

	def __init__(self):
		self.data={}
		self.data[""]={}
		self.limiter=0

	def validate(self,tweet):
		cleaned = wordtools.clean(tweet)
		if wordtools.validate(cleaned) and len(cleaned)>=2:
			return cleaned
		else:
			return None

	def save(self,a):
		a.insert(0,"")
		a.append("")
		for i in range(0,len(a)-1):
			if not a[i] in self.data:
				self.data[a[i]]={}
			if a[i+1] in self.data[a[i]]:
				self.data[a[i]][a[i+1]]+=1
			else:
				self.data[a[i]][a[i+1]]=1

	def build(self):
		self.limiter+=1
		if self.limiter < 1000 or not self.limiter%300==0:
			return None
		s = ""
		lastWord = ""
		while True:
			total = 0
			for word in self.data[lastWord]:
				total+=self.data[lastWord][word]
			choice = random.randint(0,total-1)
			total = 0
			for word in self.data[lastWord]:
				total+=self.data[lastWord][word]
				if total>choice:
					lastWord=word
					s+=word+" "
					break
			if lastWord=="":
				break
		return s.lower()
