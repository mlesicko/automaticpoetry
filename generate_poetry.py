import time
import codecs
import wordtools

language = ["en"]

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
           if "text" in tweet and "lang" in tweet and tweet["lang"] in language:
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
            if "text" in tweet and "lang" in tweet and tweet["lang"] in language:
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

def printpoem(text):
    print(text)

def savepoem(text, saveFileName):
    if saveFileName!=None:
        with codecs.open(saveFileName,encoding="utf-8",mode="a") as saveFile:
            saveFile.write(text+"\n")

