"""
1.Bigram Probabilities
Desc : Probability of a written sentence using the bigram language model
Submitted by : Vidya Sri Mani
vxm163230
"""

from collections import Counter

totalWords = 0
testSentence = """retired vice president and treasurer of"""

#writes the unigram and bigram count list to file
def writeToFile(filename,countList):
    with open(filename, 'w') as f:
        for count in countList:
            f.write((str(count)+'  -->  '+str(countList[count])+"\n"))


#get the number of token(and frequencey of each token space/newline separated word)
#This is also the unigram count
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
    bigramCount = (Counter(zip(words[1:],words)))

    writeToFile('C:\\Users\\Vidya\\Desktop\\NLP\\Homework2\\bigramCount.txt', bigramCount)
    print('Unigram and Bigram counts written to file')

    getBigramProb(testSentence.split(), unigramCount, bigramCount)

def getBigramProb(testSentencewords, unigramCount, bigramCount):

    testSentencewordCount = len(testSentencewords)
    testSentenceBigramCount = {}
    bigramProbability = 1
    probabiilty=1


    if(testSentencewordCount<2):
        print ('Enter a sentence with atleast two words')
    else:
        print('Calculating probabilities')
        testSentenceBigramCount = Counter(zip(testSentencewords[1:],testSentencewords))

        #Calculating probabilty without smoothing
        print('Calculating Probabilty without smoothing')
        for pair in testSentenceBigramCount.keys():#pair has every bigram in the test sentence
            if (pair  in bigramCount.keys()):
                numerator = bigramCount[pair] #count of the bigram
                denominator = unigramCount[pair[1]]#pair[1] gives the previous word in the bigram pair

            else:
                numerator=0
            if denominator!= 0:
                probability = numerator/denominator
            bigramProbability *=probability

        print('---------------------------------------')
        print('Test sentence: ' + testSentence)
        print('Bigram Probabilty without smoothing : ')
        print(bigramProbability)

#PROGRAM EXECUTION BEGINS HERE
#input file
file ='C:\\Users\\Vidya\\Desktop\\NLP\\Homework2\\corpus.txt'
#file=input("Enter file path to corpus")
#testSentence = input('Enter Test Sentence')
print('Calculating count of tokens')
getTokenCount(file)





print ('Done')

