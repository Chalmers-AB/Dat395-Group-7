def get_type(letter):
    if letter.isspace():
        return "s"
    elif letter.isalpha():
        return "a"
    elif letter.isdigit():
        return "d"
    else:
        return "o"

def tokenize(lines):
    words = []
    #Ba så den gör alla lines efter varandra.
    for line in lines:
        wordstart = 0
        previoustype = "s"
        #Kör en i för varje bokstav så man kan köra line[i]
        for i in range(len(line)):
            currenttype = get_type(line[i])
            #om förra typen inte är samma som nuvarande typ, och förra typen inte är space, så lägg till ordet i listan
            if currenttype != previoustype:
                if previoustype != "s":
                    words.append(line[wordstart:i].lower())

                wordstart = i
            #just so if we just made a new word and got a space it will skip that and go to the next for wordstart
            if currenttype == "s":
                wordstart = i + 1

            previoustype = currenttype

        if len(line) > 0 and previoustype != "s":
            words.append(line[wordstart:].lower())

    return words

   
        #take each word in the line, figure out how to create new words aka variable for each,
        #to do this check the current letter type, and the previous one, if they differ, 
        #put the current one into a new word, if it's a space, skip entirely then next one 
        #will see previous was a space thus new word
        
     

def countWords(arr, stopWords):
    dic = {}
    #kör för varje ord i listan vi inputar
    for word in arr:
        #om den är i stopwords ignorera den
        if word in stopWords:
            pass
        #om den inte redan finns i dictionary
        elif word not in dic:
            #initierar hashen
            dic[word] = 1
        else:
            #ökar hashets värde med 1
            dic[word] += 1
    return dic
