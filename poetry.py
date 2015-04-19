#!/usr/bin/python
import os
import sys
import time
import codecs
from twitter import *

language = ["en","und"]
saveDirName = "./saved_poems/"
saveFileName = None

def setupTwitter():
	CONSUMER_CREDENTIALS = open('.consumer_credentials')
	CONSUMER_KEY = CONSUMER_CREDENTIALS.readline()[:-1]
	CONSUMER_SECRET = CONSUMER_CREDENTIALS.readline()[:-1]
	MY_TWITTER_CREDS = os.path.expanduser('./.my_app_credentials')
	if not os.path.exists(MY_TWITTER_CREDS):
		oauth_dance("My App Name", CONSUMER_KEY, CONSUMER_SECRET,
                MY_TWITTER_CREDS)
	oauth_token, oauth_secret = read_token_file(MY_TWITTER_CREDS)
	stream = TwitterStream(auth=OAuth(oauth_token, oauth_secret, CONSUMER_KEY, CONSUMER_SECRET))
	return stream.statuses.sample()

def generatePoetry(form, getIterator):
	while True:
		iterator = getIterator()
		for tweet in iterator:
			if "text" in tweet and "lang" in tweet and tweet["lang"] in language:
				tweetText = tweet["text"]
				form.readTweet(tweetText)
				poemText = form.build()
				if not poemText==None:
					printpoem(poemText)
		time.sleep(10) #If the stream runs out or hits an error, take a break and restart.

def generateMultiPoetry(forms, iterator):
	for tweet in iterator:
		if "text" in tweet and "lang" in tweet and tweet["lang"] in language:
			tweetText = tweet["text"]
			for form in forms:
				form.readTweet(tweetText)
				poemText = form.build()
				if not poemText==None and len(poemText)>1:
					if poemText[-1]!="\n":
						poemText+="\n"
					printpoem(poemText)

def setupSaveFile(forms):
	if not os.path.exists(saveDirName):
		os.makedirs(saveDirName)
	global saveFileName
	saveFileName = saveDirName+("".join(forms)+"-"+time.strftime("%Y-%m-%d")+".txt")
	

def printpoem(text):
	print(text)
	if saveFileName!=None:
		with codecs.open(saveFileName,encoding="utf-8",mode="a") as saveFile:
			saveFile.write(text+"\n")

poemforms = ["haiku","because","acrostic","atoz","couplet",
		"iambicpentameter","limerick","alliterative"]

otherforms = ["markov","markov2","markovsounds"]

def getForm(arg):
	## POEMS
	if arg==poemforms[0]:
		import haiku
		form = haiku.form()
	elif arg==poemforms[1]:
		import because
		form = because.form()
	elif arg==poemforms[2]:
		import acrostic
		form = acrostic.form()
	elif arg==poemforms[3]:
		import atoz
		form = atoz.form()
	elif arg==poemforms[4]:
		import rhymingcouplet
		form = rhymingcouplet.form()
	elif arg==poemforms[5]:
		import iambicpentameter
		form = iambicpentameter.form()
	elif arg==poemforms[6]:
		import limerick
		form = limerick.form()
	elif arg==poemforms[7]:
		import alliterative
		form = alliterative.form()
	## OTHER THINGS
	elif arg==otherforms[0]:
		import markov
		form = markov.form()
	elif arg==otherforms[1]:
		import markov2
		form = markov2.form()
	elif arg==otherforms[2]:
		import markovsounds
		form = markovsounds.form()
	else:
		form = None
	return form


def usage():
	print("Usage: python3 poem.py FORM")
	print("Available forms: "+", ".join(poemforms))

if __name__ == "__main__":
	if len(sys.argv)==2 and (sys.argv[1] in poemforms or sys.argv[1] in otherforms):
		setupSaveFile(sys.argv[1:])
		form = getForm(sys.argv[1])
		generatePoetry(form,setupTwitter)
	elif len(sys.argv)==2 and sys.argv[1] == "all":
		setupSaveFile(["all"])
		forms = []
		for form in poemforms:
			forms.append(getForm(form))
		iterator = setupTwitter()
		generateMultiPoetry(forms,iterator)
	elif len(sys.argv)==2 and len(sys.argv[1])>4 and sys.argv[1][:4]=="-dev":
		setupSaveFile(sys.argv[1][1:])
		formName = sys.argv[1][4:]
		exec ("import "+formName)
		exec ("form = "+formName+".form()")
		generatePoetry(form,setupTwitter)
	elif len(sys.argv)>2:
		setupSaveFile(sys.argv[1:])
		forms = []
		for arg in sys.argv[1:]:
			form = getForm(arg)
			if form != None:
				forms.append(form)
		iterator = setupTwitter()
		generateMultiPoetry(forms,iterator)
	else:
		usage()
