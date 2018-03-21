fh = open('mbox-short.txt')
print(fh)

for lx in fh:
    ly = lx.rstrip()
    uly = ly.upper()
    print(uly)
