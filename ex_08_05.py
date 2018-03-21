fname = input("Enter file name: ")
try:
    fh = open(fname)
except FileNotFoundError:
    print("File not found")
    quit()

text = []
count = 0
for line in fh:
    line = line.rstrip()
    if not line.startswith('From '):
        continue
    from_line = line.split()
    count += 1
    print(from_line[1])
print("There were", count, "lines in the file with From as the first word")
