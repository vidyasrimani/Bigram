"""
1.Bigram Probabilities
Desc : Probability of a written sentence using the bigram language model
Submitted by : Vidya Sri Mani
vxm163230
"""

from collections import Counter
import re


#get the number of token(and frequencey of each space/newline separated word)
def getTokenCount():


def getBigramCount():


def getBigramProb():



#input file
file ='C:\\Users\\Vidya\\Desktop\\NLP\\Homework2\\corpus.txt'
content=open(file).read()
#Split words (space separated)
words = re.findall('[\n\S]+', content)

c = (Counter(zip(words, words[1:])))
print ('Hello')

