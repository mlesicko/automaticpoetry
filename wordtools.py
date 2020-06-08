from num2words import num2words

f = open("cmudict.0.7a.txt")
cmudict = {}
for line in f:
	if line[0:3]==";;;":
		continue
	pieces = line.split("  ") #two spaces
	cmudict[pieces[0]]=pieces[1][:-1]

def fixTextErrors(text):
	#fix ampersands being rendered with web encoding
	return text.replace("&amp;","&")

def fixUnreadableCharacters(text):
	#read ampersands as "AND"
	return text.replace("&", " and ")


def clean(text):
	fixedText = fixUnreadableCharacters(text)
	clean = ''.join(c for c in fixedText if c.isalnum() or c==" ")
	cleanArray = []
	for word in clean.split(" "):
		if len(word)>0 and len(word)==len(''.join(c for c in word if c in "0123456789")):
			cleanArray.append(num2words(int(word)).upper())
		else:
			cleanArray.append(word.upper())
	return cleanArray

def syllableCount(words):
	count = 0
	for word in words:
		i = wordSyllableCount(word)
		if i ==-1:
			return -1
		else:
			count+=i
	return count

def wordSyllableCount(word):
	if word in cmudict:
		return len(''.join(c for c in cmudict[word] if c in "012"))
	else:
		return -1

def validate(words):
	for word in words:
		if not word in cmudict:
			return False
	return True

def getRhyme(word):
	if not word in cmudict:
		return None
	else:
		pron = cmudict[word]
		lastAccent = -1
		if "1" in pron:
			lastAccent = pron.rindex("1")
		elif "0" in pron:
			lastAccent = pron.rindex("0")
		if lastAccent == -1: #Somehow word has no vowel sounds!?
			return None
		index=-1
		if " " in pron[:lastAccent]:
			index = pron[:lastAccent].rindex(" ")
		return pron[index+1:]

def getInitialSound(word):
	if not word in cmudict:
		return None
	else:
		pron = cmudict[word]
		lastAccent = -1
		if "1" in pron:
			lastAccent = pron.rindex("1")
		elif "0" in pron:
			lastAccent = pron.rindex("0")
		if lastAccent == -1:
			return None
		index=-1
		if " " in pron[:lastAccent]:
			index = pron[:lastAccent].rindex(" ")
		elif " " in pron[lastAccent:]:
			index = pron[lastAccent:].rindex(" ")
		return pron[:index]
		

def getMeter(words):
	meter = ""
	for word in words:
		wordMeter = getWordMeter(word)
		if wordMeter == None:
			return None
		meter+=wordMeter
	return meter
	

def getWordMeter(word):
	if not word in cmudict:
		return None
	else:
		pron = cmudict[word]
		meter = ''.join(c for c in pron if c in '012')
		meter = meter.replace('2','1')
		return meter

def getPronunciationNoStress(word):
	if not word in cmudict:
		return None
	else:
		pron = cmudict[word]
		pron = ''.join(c for c in pron if c not in '012')
		return pron.split(" ")
