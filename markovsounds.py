import wordtools
import random
import poem

class form(poem.form):

	def __init__(self):
		self.data={}
		self.data[""]={}
		self.limiter=0
		self.tweetcatalog = {}

	def validate(self,tweet):
		cleaned = wordtools.clean(tweet)
		if wordtools.validate(cleaned):
			sounds = []
			for word in cleaned:
				sounds +=wordtools.getPronunciationNoStress(word)+[" "]
			if len(sounds)>4:
				sounds.pop() #remove the last space
				return sounds
			else:
				return None
		else:
			return None

	def save(self,a):
		self.tweetcatalog[tuple(a)]=1
		if not a[0] in self.data[""]:
			self.data[""][a[0]]=1
		else:
			self.data[""][a[0]]+=1
		a.insert(0,"")
		a.append("")
		for i in range(0,len(a)-2):
			pred = a[i]+a[i+1]
			succ = a[i+2]
			if not pred in self.data:
				self.data[pred]={}
			if succ in self.data[pred]:
				self.data[pred][succ]+=1
			else:
				self.data[pred][succ]=1

	def build(self):
		self.limiter+=1
		if self.limiter < 1000 or not self.limiter%300==0:
			return None
		retries = 0
		s = ""
		penWord=""
		ultWord = ""
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
					penWord=ultWord
					ultWord=word
					s+=word
					break
			lastWord=penWord+ultWord
			if ultWord=="":
				if tuple(s.split(" ")) not in self.tweetcatalog:
					break
				else:
					s=""
					penWord=""
					ult=""
					lastWord=""
					#print("Retry: "+str(retries))
					retries +=1
					if retries >5:
						return None
		return s.lower()
