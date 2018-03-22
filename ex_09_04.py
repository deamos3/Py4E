name = input("Enter file:")  # get file name from user
if len(name) < 1:  # give a default if no file is given
    name = "mbox-short.txt"
handle = open(name)

counts = dict()
for line in handle:
    line = line.rstrip()  # strip whitespace and newlines
    words = line.split()  # split the line into words words[1] is email address
    # words[0] is the first word of the line, so using the following we can
    # just look at the lines that start with 'From' and we ignore any blank
    # lines so that words[0] and words[1] don't blow up, hence the following
    # len(words) < 2
    if len(words) < 2 or words[0] != 'From':
        continue
    # here we look at the email address words[1], and count how many times
    # it has sent an email
    counts[words[1]] = counts.get(words[1], 0) + 1

frequent_email = None
frequency = None

for email, count in counts.items():
    if frequency is None or count > frequency:
        frequent_email = email
        frequency = count

print(frequent_email, frequency)
