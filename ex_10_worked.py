name = input("Enter file:")  # get file name from user
if len(name) < 1:  # give a default if no file is given
    name = "clown.txt"
handle = open(name)

counts = dict()
for line in handle:
    line = line.rstrip()  # strip whitespace and newlines
    words = line.split()  # splits the line into individual words
    for w in words:
        counts[w] = counts.get(w, 0) + 1

# print(counts)

tmp = list()
for k, v in counts.items():  # this flips the key value pairs
    # print(v, k)
    newt = (v, k)
    tmp.append(newt)

tmp = sorted(tmp, reverse=True)  # reverse sorts highest first
# print(tmp[:5])  # prints the top 5 items
# x = sorted(counts.items())
# print(x[:5])

# to print this in a nicer looking format, we can flip the list back
# and print it down

for v, k in tmp[:10]:
    print(k, v)
