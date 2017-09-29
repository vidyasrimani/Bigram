"""
1.Bigram Probabilities
Desc : Probability of a written sentence using the bigram language model
Submitted by : Vidya Sri Mani
vxm163230
"""


#read file
file = open('C:\\Users\\Vidya\\Desktop\\NLP\\Homework2\\corpus.txt')
content = file.readlines()

#read the file line by line and tokenize each word(space separated)
for line in content:
    words=line.split()
