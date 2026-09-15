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
    for line in lines:
        wordstart = 0
        previoustype = "s"

        for i in range(len(line)):
            currenttype = get_type(line[i])

            if currenttype != previoustype:
                if previoustype != "s":
                    words.append(line[wordstart:i].lower())

                wordstart = i

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
        
     

