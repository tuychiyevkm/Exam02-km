text  = input("Type a text: ")

text.split()

word_count = {}

for word in text.split():

    if word in word_count: 
        word_count[word] += 1
    else:
        word_count[word] = 1

print(word_count)