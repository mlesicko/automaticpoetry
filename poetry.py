#!/usr/bin/env python3
import os
import sys
import time
from twitter import *

from generate_poetry import generatePoetry, generateMultiPoetry
from handle_forms import getForm, poem_forms, tool_forms, other_forms

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

def setupSaveFile(forms):
	if not os.path.exists(saveDirName):
		os.makedirs(saveDirName)
	global saveFileName
	saveFileName = saveDirName+("".join(forms)+"-"+time.strftime("%Y-%m-%d")+".txt")
	
def usage():
	print("Usage: poetry.py FORM...")
	print("Poem forms:\n\t"+"\n\t".join(sorted(poem_forms)))
	print("Other forms:\n\t"+"\n\t".join(sorted(other_forms)))
	print("Tools:\n\t"+"\n\t".join(sorted(tool_forms)))

if __name__ == "__main__":
	if len(sys.argv)==2:
		setupSaveFile(sys.argv[1:])
		form = getForm(sys.argv[1])
		if form != None:
			generatePoetry(form,setupTwitter,saveFileName)
		else:
			print("Error: " + sys.argv[1] + " is not a supported form")
			usage()
	elif len(sys.argv)>2:
		setupSaveFile(sys.argv[1:])
		forms = []
		for arg in sys.argv[1:]:
			form = getForm(arg)
			if form != None:
				forms.append(form)
			else:
				print("Error: " + arg + " is not a supported form")
		if (len(forms) > 0):
			generateMultiPoetry(forms,setupTwitter,saveFileName)
		else:
			usage()
	else:
		usage()
