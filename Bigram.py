"""
    1.Bigram Probabilities
    Desc : Probability of a written sentence using the bigram language model
    Submitted by : Vidya Sri Mani
    vxm163230
"""

from collections import Counter, defaultdict


testSentence = """retired vice president and treasurer of"""

def writeProbabilityToFile(bigramCount,unigramCount,file):
    with open(file, 'w') as f:
        f.write("Bigram Count and Probabilities\n")
        f.write("--------------------------------------------------------------------\n")
        for pair in bigramCount.keys():
            numerator = bigramCount[pair]  # count of the bigram
            denominator = unigramCount[pair[1]]  # pair[1] gives the previous word in the bigram pair
            probability = numerator/denominator
            f.write("Bigram:"+str(pair)+",\tCount:"+str(bigramCount[pair])+",\tProbability:"+str(probability)+"\n")

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

    wordCount = {}
    wordCount = Counter(words)

    #writeToFile('C:\\Users\\Vidya\\Desktop\\NLP\\Homework2\\unigramCount.txt', wordCount)
    getBigramCount(words,wordCount)


def getBigramCount(words,unigramCount):
    print('Getting Bigram count...')

    #store word and next word in BigramCount not all combinations
    bigramCount = (Counter(zip(words[1:],words)))

    writeToFile('C:\\Users\\Vidya\\Desktop\\NLP\\Homework2\\bigramCount.txt', bigramCount)

    print('Unigram and Bigram counts written to file')

    getBigramProb(testSentence.split(), unigramCount, bigramCount,words)

def getBigramProb(testSentencewords, unigramCount, bigramCount,words):

    file = 'C:\\Users\\Vidya\\Desktop\\NLP\\Homework2\\bigramProbabilty.txt'
    writeProbabilityToFile(bigramCount, unigramCount, file)

    testSentencewordCount = len(testSentencewords)
    testSentenceBigramCount = {}
    bigramProbability = 1
    probabiilty=1

    #TEST SENTENCE CALCULATIONS
    #WITHOUT SMOOTHING

    if(testSentencewordCount<2):
        print('sentence less than two words')

    else:
        print('Calculating probabilities')
        testSentenceBigramCount = Counter(zip(testSentencewords[1:],testSentencewords))

        numerator = 0
        denominator = 1
        probability = 1
        bigramProbabilityWithSmoothing = 1

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
        print(bigramProbability)# TO DO --> try log probability as well

        # WITH SMOOTHING
        numerator = 1
        denominator = 1
        totalWords = len(unigramCount)
        # Calculating probabilty with add one smoothing
        print('Calculating Probabilty with add one smoothing')
        for pair in testSentenceBigramCount.keys():  # pair has every bigram in the test sentence
            if (pair in bigramCount.keys()):
                numerator = bigramCount[pair]+1  # count of the bigram
                denominator = unigramCount[pair[1]]+totalWords  # pair[1] gives the previous word in the bigram pair

            else:
                numerator = 1
                if pair[1] in unigramCount.keys():
                    denominator = totalWords + unigramCount[pair[1]]
                else:
                    denominator = totalWords
            if denominator != 0:
                probability = numerator / denominator
            bigramProbabilityWithSmoothing *= probability

        print('---------------------------------------')
        print('Test sentence: ' + testSentence)
        print('Bigram Probabilty with add one smoothing : ')
        print(bigramProbabilityWithSmoothing)  # TO DO --> try log probability as well
        goodTuringProbability(words, unigramCount, bigramCount,testSentencewords)


def goodTuringProbability(words, unigram, bigram, testSentenceWords):
    countAsDict = defaultdict(list)
    testCountAsdict = defaultdict(list)
    countOfBigram = len(bigram)
    countOfUnigram = len(unigram)
    totalCount = countOfUnigram*countOfUnigram
    testSentenceWordLen = len(testSentenceWords)

    bigramGT = {}
    bigramProbGT = {}
    sentenceBigramGT = {}
    sentenceBigramProbGT = {}
    sentenceProbability = 1


    for value in bigram.values():
        if value in countAsDict.keys():
            countAsDict[value] += 1
        else:
            countAsDict[value] = 1

    countAsDict[0] = totalCount - countOfBigram

    TestBigram = Counter(zip(words[1:], words))

    for pair in TestBigram.keys():  # pair has every bigram in the test sentence
        if (pair in bigram.keys()):
            count=bigram[pair]+1

            if count not in countAsDict:
                bigramGT[pair] = 0
                bigramProbGT[pair] = 0
            else:
                countStar = count*(countAsDict[count] / countAsDict[count-1])
                bigramGT[pair] = countStar
                bigramProbGT[pair] = countStar / countOfBigram
        else:
            bigramGT[pair] = countAsDict / countAsDict[0]
            bigramProbGT[pair] = countAsDict[1] / countOfBigram

    #writeToFile('C:\\Users\\Vidya\\Desktop\\NLP\\Homework2\\goodTuringBigramCount.txt',bigramGT)
    #writeToFile('C:\\Users\\Vidya\\Desktop\\NLP\\Homework2\\goodTuringBigramProbability.txt',bigramProbGT)
    filename = 'C:\\Users\\Vidya\\Desktop\\NLP\\Homework2\\goodTuringWithProbability.txt'

    #COMPUTING PROBABILITY FOR GOOD TURING USING TEST SENTENCE

    for value in bigram.values():
        if value in testCountAsdict.keys():
            testCountAsdict[value] += 1
        else:
            testCountAsdict[value] = 1

    testCountAsdict[0] = totalCount - countOfBigram

    TestSentenceBigram = Counter(zip(testSentenceWords[1:], testSentenceWords))

    if (testSentenceWordLen < 2):
        print('Sentence has less than two words')
    else:
        for pair in TestSentenceBigram.keys():
            if (pair) in bigram.keys():
                count = bigram[pair] + 1

                if count not in testCountAsdict:
                    sentenceBigramGT[pair] = 0
                    sentenceBigramProbGT[pair] = 0
                else:
                    countStar = count * (testCountAsdict[count] / testCountAsdict[count - 1])
                    sentenceBigramGT[pair] = countStar
                    sentenceBigramProbGT[pair] = countStar / countOfBigram
            else:
                sentenceBigramGT[pair] = testCountAsdict[1] / testCountAsdict[0]
                sentenceBigramProbGT[pair] = testCountAsdict[1] / countOfBigram
    #print(sentenceBigramProbGT)
    for prob in sentenceBigramProbGT.values():
        sentenceProbability *= prob
    print('Test sentence:'+testSentence)
    print('Proability with good Turing Discounting:')
    print(sentenceProbability)
    print('---------------------------------------')



#PROGRAM EXECUTION BEGINS HERE
#input file
file ='C:\\Users\\Vidya\\Desktop\\NLP\\Homework2\\corpus.txt'
#file=input("Enter file path to corpus in the format : C:\\Users\\Vidya\\Desktop\\NLP\\Homework2\\corpus.txt")
#testSentence = input('Enter Test Sentence')
print('Calculating count of tokens')
getTokenCount(file)

print ('Done')

