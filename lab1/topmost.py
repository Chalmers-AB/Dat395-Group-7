import wordfreq
from wordfreq import tokenize
from wordfreq import countWords
import sys
import urllib.request
##response = urllib.request.urlopen(sys.argv[2])
##lines = response.read().decode("utf8").splitlines()

def printTopMost(frequencies, n):
    frequencies = sorted(frequencies, key=lambda x: -x[1])
    y = 0
    while y < n:
        print(frequencies[y[0]].ljust(20),frequencies[y[1]].rjust(5))

    


def main(StopWords, File, n):
    inp_file = open(sys.argv[1], encoding="utf-8")
    tokens = tokenize(inp_file)
    count = countWords(tokens, StopWords)
    printTopMost(count, n)
    pass



main(1,1,3)