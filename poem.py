class form:
	def readTweet(self,tweet):
		clean = self.validate(tweet)
		if clean!=None:
			self.save(clean)

	def validate(self,tweet):
		pass

	def save(self,clean):
		pass
