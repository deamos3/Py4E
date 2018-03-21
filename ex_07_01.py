# Use words.txt as the file name
fname = input("Enter file name: ")
try:
    fh = open(fname)
except FileNotFoundError:  # need to fix bare except
    print("File not found")
    quit()
for line in fh:
    line = line.rstrip()
    uline = line.upper()
    print(uline)
