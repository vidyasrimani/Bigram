"""
1.Bigram Probabilities
Desc : Probability of a written sentence using the bigram language model
Submitted by : Vidya Sri Mani
vxm163230
"""

from collections import Counter
import re


#get the number of token(and frequencey of each space/newline separated word)
def getTokenCount(file):
    print('Getting Token count...')
    content = open(file).read()

    # Split words (space separated)
    words = re.findall('\S+', content)
    wordCount = {}
    for word in words:
        if word in wordCount:
            wordCount[word]+=1
        else:
            wordCount[word] = 1

    getBigramCount(words)



def getBigramCount(words):
    print('Getting Bigram count...')
    c = (Counter(zip(words, words[1:])))

def getBigramProb():
    print('getting Bigram Probabilty...')


#PROGRAM EXEVUTION BEGINS HERE
#input file
file ='C:\\Users\\Vidya\\Desktop\\NLP\\Homework2\\corpus.txt'

#file=input("Enter file path")
getTokenCount(file)
#getBigramProb()

print ('Done')

