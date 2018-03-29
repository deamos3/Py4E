name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name)

counts = dict()
lst = list()
for line in handle:
    line = line.rstrip()  # strip whitespace and newlines
    words = line.split()  # split the line into words words[1] is email address
    # words[0] is the first word of the line, so using the following we can
    # just look at the lines that start with 'From' and we ignore any blank
    # lines so that words[0] and words[1] don't blow up, hence the following
    # len(words) < 2
    if len(words) < 6 or words[0] != 'From':
        continue
    # here we look at the email address words[1], and count how many times
    # it has sent an email
    time = words[5].split(':')
    counts[time[0]] = counts.get(time[0], 0) + 1

for key, value in list(counts.items()):
    lst.append((key, value))
lst.sort()
for key, value in lst:
    print(key, value)
