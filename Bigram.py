"""
1.Bigram Probabilities
Desc : Probability of a written sentence using the bigram language model
Submitted by : Vidya Sri Mani
vxm163230
"""

from collections import Counter
import re

totalWords = 0
testSentence = """The memo
attempts to remove the tourist board as far as possible from the
agency"""

#get the number of token(and frequencey of each token space/newline separated word)
#This is also the unigram count


def writeToFile(filename,countList):
    with open(filename, 'w') as f:
        for count in countList:
            f.write((str(count)+'  -->  '+str(countList[count])+"\n"))
def getTokenCount(file):
    print('Getting Token count...')
    content = open(file).read()

    # Split words (space separated)
    #words = re.findall('\S+', content)
    words = content.split()
    totalWords = len(words)
    wordCount = {}
    wordCount = Counter(words)

    writeToFile('C:\\Users\\Vidya\\Desktop\\NLP\\Homework2\\unigramCount.txt', wordCount)
    getBigramCount(words,wordCount)


def getBigramCount(words,unigramCount):
    print('Getting Bigram count...')
    bigramCount = {}
    #store word and next word in BigramCount
    bigramCount = (Counter(zip(words,words[1:])))

    writeToFile('C:\\Users\\Vidya\\Desktop\\NLP\\Homework2\\bigramCount.txt', bigramCount)
    print('Unigram and Bigram counts written to file')

    getBigramProb(testSentence.split(), unigramCount, bigramCount)

def getBigramProb(testSentencewords, unigramCount, bigramCount):
    print('Test Sentence words without smoothing...')

    #unzipping words from bigramCount.keys()
    #ord1,word2=zip(*(bigramCount.keys()))

    testSentencewordCount = len(testSentencewords)
    testSentenceBigramCount = {}

    if(testSentencewordCount<2):
        print ('Enter a sentence with atleast two words')
    else:
        print('Calculating probabilities')
        testSentenceBigram = Counter(zip(testSentencewords, testSentencewords[1:]))
        for pair in testSentenceBigram.keys():
            if (pair  in bigramCount.keys()):
                print(pair)
        else:
            print('okay')

        writeToFile('C:\\Users\\Vidya\\Desktop\\NLP\\Homework2\\testSentenceBigramCount.txt', testSentenceBigramCount)

#PROGRAM EXECUTION BEGINS HERE
#input file
file ='C:\\Users\\Vidya\\Desktop\\NLP\\Homework2\\corpus.txt'
#file=input("Enter file path to corpus")
#testSentence = input('Enter Test Sentence')
print('Calculating count of tokens')
getTokenCount(file)





print ('Done')

