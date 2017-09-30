"""
1.Bigram Probabilities
Desc : Probability of a written sentence using the bigram language model
Submitted by : Vidya Sri Mani
vxm163230
"""

from collections import Counter
import re

totalWords = 0

#get the number of token(and frequencey of each token space/newline separated word)
#This is also the unigram count
def getTokenCount(file):
    print('Getting Token count...')
    content = open(file).read()

    # Split words (space separated)
    words = re.findall('\S+', content)
    totalWords = len(words)
    wordCount = {}

    for word in words:
        if word in wordCount:
            wordCount[word] += 1
        else:
            wordCount[word] = 1

    #Write Contents to file
    getBigramCount(words)


def getBigramCount(words):
    print('Getting Bigram count...')
    bigramCount = {}
    #bigrams = Counter(zip(words, nextword))
    #store word and next word in BigramCount
    for i in range (0,totalWords-1):
        #Note to self:use Re for newline search
        if(words[i]+" "+words[i+1]) in bigramCount:#already present
            bigramCount[words[i] + " " + words[i + 1]] += 1
        else:
            bigramCount[words[i] + " " + words[i + 1]] += 1
    #write content to file

def getBigramProb():
    print('getting Bigram Probabilty...')


#PROGRAM EXECUTION BEGINS HERE
#input file
file ='C:\\Users\\Vidya\\Desktop\\NLP\\Homework2\\corpus.txt'
#file=input("Enter file path to corpus")

#testSentence = input('Enter Test Sentence')
testSentence = ''

getTokenCount(file)
#getBigramProb()

print ('Done')

