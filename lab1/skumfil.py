
def countWords(words, stopWords):
    i = 0
    dict = {}
    for each in words:
        word = hash(words[i].split())
        if word in stopWords:
            pass
        elif word not in dic:
            dict << (word, 1)
        else:
            dict[word] += 1
        i += 1
    return dict

print(countWords(['it', 'is', 'a', 'book'], ['a', 'is', 'it']))