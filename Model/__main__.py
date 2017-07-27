from nltk.corpus import stopwords
import time
import string
import random

millis = int(round(time.time() * 1000))
# stop = set(stopwords.words('english'))

# print(stop)
docs = range(4)

doc1 = open("../Train/Doc1.txt", "r")
millis = int(round(time.time() * 1000))-millis
print("Opened document in " + str(millis))


# Doc cleaning
train = doc1.read()
train = train.replace("\n", " ")
train = train.decode('string_escape')
train = train.lower()
train = train.split(".")
train = [x.translate(string.maketrans("",""), string.punctuation) for x in train]

millis = int(round(time.time() * 1000))

mapFirsts 	= {}
mapCentres 	= {}
mapLasts 	= {}
mapRhymes  	= {}

# Map with lag 1 (Hope to create a probabilistic model)

Firsts 	= []
Lasts 	= []
Centres = []

for i in range(len(train)):
	sentence = train[i]
	sentence = sentence.split(" ")
	if(len(sentence) > 1):
		Firsts.append(sentence[0])
		mapFirsts[sentence[0]] = mapFirsts.get(sentence[0], []) + [sentence[1]]
		for j in range(1,len(sentence)-1):
			Centres.append(sentence[j])
			mapCentres[sentence[j-1]] = mapCentres.get(sentence[j-1], []) + [sentence[j]]
		Lasts.append(sentence[len(sentence)-1])
		mapLasts[sentence[len(sentence)-2]] = mapLasts.get(sentence[len(sentence)-2], []) + [sentence[len(sentence)-1]]

millis =  int(round(time.time() * 1000)) - millis
print("Processed document in " + str(millis))
millis =  int(round(time.time() * 1000))


for i in range(len(Lasts)):
	if(len(Lasts[i])>1):
		ending 		=  Lasts[i][len(Lasts[i]) - 2:]
		mapRhymes[ending] = mapRhymes.get(ending, []) + [Lasts[i]]


millis =  int(round(time.time() * 1000)) - millis
print("Created rhyme maps for the document in " + str(millis))
millis =  int(round(time.time() * 1000))

print("Now I will start writing!")
print(mapLasts)

for i in range(10):
	line1 	= random.choice(Firsts)	
	word  	= random.choice(mapFirsts[line1])
	line1 	= line1 + " " + word
	word 	= random.choice(mapCentres[word])
	line1 	= line1 + " " + word
	word 	= random.choice(mapCentres[word])
	line1 	= line1 + " " + word
	word 	= random.choice(mapLasts[word])
	line1 	= line1 + " " + word + ",\n"
	endword = random.choice(mapRhymes[word[len(word)-2:]])
	line1 	= random.choice(Firsts)	
	word  	= random.choice(mapFirsts[line1])
	line1 	= line1 + " " + word
	word 	= random.choice(mapCentres[word])
	line1 	= line1 + " " + word
	word 	= random.choice(mapCentres[word])
	line1 	= line1 + " " + word
	line1 	= line1 + " " + endword + ",\n"
		

