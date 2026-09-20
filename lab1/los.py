def tokenize(lines):
     words = []
     for line in lines:
         start = 0
         while start < len(line):
              while line[start].isspace():
                   start = start + 1
              if line[start].isdigit():
                   end = start
                   while line[end].isdigit():
                        end = end + 1
                   word = line[start:end]
                   words.append(line[start:end])
                   start = end - 1

              elif line[start].isalpha():
                   end = start
                   while line[end].isalpha():
                       end = end + 1
                   word1 = line[start:end]
                   word1.lower
                   words.append(word1)
                   start = end - 1

              else:
                   end = start
                   words.append(line[start])
              start = start+1
     return words
print(tokenize(['    Sweet apple 10,  abac.']))
