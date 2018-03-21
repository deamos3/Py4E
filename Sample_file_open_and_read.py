fname = input("Enter file name: ")
try:
    fh = open(fname)
except FileNotFoundError:
    print("File not found")
    quit()
for line in fh:
    line = line.rstrip()
    print(line)
