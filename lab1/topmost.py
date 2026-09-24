import wordfreq
from wordfreq import tokenize
from wordfreq import countWords
from wordfreq import printTopMost
import sys
import urllib.request
##response = urllib.request.urlopen(sys.argv[2])
##lines = response.read().decode("utf8").splitlines()

def main(StopWords, File, n):
    
    inp_file = File
    tokens = tokenize(inp_file)
    inp_words = open(StopWords, encoding="utf-8").read()
    count = countWords(tokens, inp_words)
    printTopMost(count, n)
    pass


if sys.argv[2].startswith(("http://", "https://")):
    response = urllib.request.urlopen(sys.argv[2])
    inp_file = response.read().decode("utf8").splitlines()
else:
    inp_file = open(sys.argv[2], encoding="utf-8").read().splitlines()
main(sys.argv[1], inp_file, int(sys.argv[3]))
