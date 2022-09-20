with open('sometext.txt') as text:
    for line in text:
        words = line.split() 
        individual_words = dict((word,words.count(word)) for word in set (words))

print(individual_words)