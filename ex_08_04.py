fname = input("Enter file name: ")
try:
    fh = open(fname)
except FileNotFoundError:
    print("File not found")
    quit()

text = []
for line in fh:
    add_text = line.split()
    for word in add_text:
        # print("Add ", word, "?")
        # if word in text:
        # print("Nope, not adding: ", word)
        if word not in text:
            text.append(word)
        # print(word, " added")
text.sort()
print(text)
