counts = dict()  # make a dictionary
# print('Enter a line of text: ')  # Prompt to get a line of text
# line = input(' ')  # getting a line of text
line = input('Enter a line of text: \n ')

words = line.split()  # splitting it on the spaces

print('Words: ', words)

print('Counting...')
for word in words:
    counts[word] = counts.get(word, 0) + 1
print('Counts', counts)

print('printing the dictionary')
for key in counts:
    print(key, counts[key])

print('printing the tuples')
for ks, vs in counts.items():
    print(ks, vs)
