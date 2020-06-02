import wordtools
from forms.form import Form

class GenerateDatasetForm(Form):
	def __init__(self):
		self.tweet = None

	def validate(self,tweet):
		clean = wordtools.clean(tweet)
		syl = wordtools.syllableCount(clean)
		if syl>0:
			return tweet
		return None

	def save(self,clean):
		self.tweet = clean.replace("\n"," ")

	def build(self):
		if self.tweet!=None:
			tweet = self.tweet
			self.tweet = None
			return tweet + "\n"
		else:
			return None
