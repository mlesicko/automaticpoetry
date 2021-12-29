import time
import codecs
import wordtools

SUPPORTED_LANGUAGES = ["en"]

def doUntilStopped(f):
   while True:
       try:
           f()
       except Exception:
           time.sleep(10)
       except KeyboardInterrupt:
           break

def generatePoetry(form, getTwitter, saveFileName):
    doUntilStopped(lambda: _generatePoetry(form, getTwitter, saveFileName))

def generateMultiPoetry(form, getTwitter, saveFileName):
    doUntilStopped(lambda: _generateMultiPoetry(form, getTwitter, saveFileName))

def _generatePoetry(form, getTwitter, saveFileName=None):
   while True:
       twitter = getTwitter()
       for tweet in twitter:
           if _isTweetUsable(tweet):
               tweetText = tweet["text"]
               fixedText = wordtools.fixTextErrors(tweetText)
               form.readTweet(fixedText)
               poemText = form.build()
               if not poemText==None:
                   printpoem(poemText)
                   savepoem(poemText, saveFileName)
       time.sleep(10) #If the stream runs out or hits an error, take a break and restart.


def _generateMultiPoetry(forms, getTwitter, saveFileName=None):
    while True:
        twitter = getTwitter()
        for tweet in twitter:
            if _isTweetUsable(tweet):
                tweetText = tweet["text"]
                for form in forms:
                    form.readTweet(tweetText)
                    poemText = form.build()
                    if not poemText==None and len(poemText)>1:
                        if poemText[-1]!="\n":
                            poemText+="\n"
                        printpoem(poemText)
                        savepoem(poemText, saveFileName)
        time.sleep(10) #If the stream runs out or hits an error, take a break and restart.

def _isTweetUsable(tweet):
    if "lang" not in tweet:
        return False
    if tweet["lang"] not in SUPPORTED_LANGUAGES:
        return False 
    if "text" not in tweet:
        return False
    if len(tweet["text"]) == 0:
        return False
    if tweet["text"][0] == "@":
        return False
    return True

def printpoem(text):
    print(text)

def savepoem(text, saveFileName):
    if saveFileName!=None:
        with codecs.open(saveFileName,encoding="utf-8",mode="a") as saveFile:
            saveFile.write(text+"\n")

