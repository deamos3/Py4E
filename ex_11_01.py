import re
name = input("Enter file:")  # get file name from user
if len(name) < 1:  # give a default if no file is given
    name = "sample_text.txt"
handle = open(name)

sum = 0
for line in handle:
    line = line.rstrip()
    # print('line', line)
    x = re.findall('[0-9]+', line)
    # print('x:', x)
    for xs in x:
        # print('xs: ', xs)
        try:
            xs = int(xs)
        except ValueError as err:
            continue
        sum += xs
print('sum: ', sum)
