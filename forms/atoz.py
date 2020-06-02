import wordtools
import random
from forms.form import Form

class AtozForm(Form):
	def __init__(self):
		self.letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
		self.data = {}
		for letter in self.letters:
			self.data[letter]=[]
		self.lookup = {}
		self.count = 0

	def validate(self,tweet):
                cleaned = wordtools.clean(tweet)
                if wordtools.validate(cleaned) and len(cleaned)>0:
                        return [''.join(c for c in self.letters if c in tweet.upper()),tweet]
                else:
                        return None

	def save(self,cleaned):
		tweetLetters = cleaned[0]
		tweet = cleaned[1]
		self.count+=1
		self.lookup[self.count]=tweet
		for letter in tweetLetters:
			self.data[letter].append(self.count)
		self.data[self.count]=tweetLetters

	def build(self):
		for letter in self.letters:
			if len(self.data[letter])==0:
				return None
		checklist = list(self.letters)
		random.shuffle(checklist)
		poem = ""
		while (len(checklist)>0):
			letter1 = checklist.pop()
			tweetId = self.data[letter1][0]
			for letter2 in self.data[tweetId]:
				self.data[letter2].remove(tweetId)
				if letter2 in checklist:
					checklist.remove(letter2)
			self.data[tweetId]=[]
			poem+=self.lookup[tweetId]+"\n"
		return poem
