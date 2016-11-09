# Deliverables:
# 1) Print the orginal text (150 tokens)
# 1) Print the new text
print("START*******")
import nltk
from nltk.book import * 
#from nltk import bigrams
#from nltk import word_tokenize,sent_tokenize
import random

def spaced(word):
	if word in [",", ".", "?", "!", ":", ";"]:
		return word
	else:
		return " " + word

print ("")
#print (text2[:150])

text = text2[:150]

orginalwords = []
for words in text:
	orginalwords.append(spaced(words))

string = "".join(orginalwords)
print (string)

tagged_tokens = nltk.pos_tag(text)
#print (tagged_tokens)

tagmap = {"NN":"a noun",
		"VB":"a verb",
		"JJ":"an adjective", 
		"PRB": "a proverb", 
		"RB": "an adverbs"}

substitution_probabilities = {"NN":.15,"VB":.1,"JJ":.1, "PRB": .1, "RB": .1}

final_words = []

for (word, tag) in tagged_tokens:
	if tag not in substitution_probabilities or random.random() > substitution_probabilities[tag]:
		final_words.append(spaced(word))
	else:
		new_word = input("Please enter %s:\n" % (tagmap[tag]))
		final_words.append(spaced(new_word))

print ("".join(final_words))


