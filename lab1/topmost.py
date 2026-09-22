import wordfreq
from wordfreq import tokenize
from wordfreq import countWords
import sys
import urllib.request
##response = urllib.request.urlopen(sys.argv[2])
##lines = response.read().decode("utf8").splitlines()

def printTopMost(frequencies, n):
    frequencies = sorted(frequencies.items(), key=lambda x: -x[1])
    y = 0
    while y < n:
        print(frequencies[y][0].ljust(20),str(frequencies[y][1]).rjust(5))
        y += 1

    


def main(StopWords, File, n):
    
    inp_file = File
    tokens = tokenize(inp_file)
    inp_words = open(StopWords, encoding="utf-8").read()
    count = countWords(tokens, inp_words)
    printTopMost(count, n)
    pass


response = urllib.request.urlopen(sys.argv[2])
main('eng_stopwords.txt',response.read().decode("utf8").splitlines(),int(sys.argv[3]))