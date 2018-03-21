# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)
tot = 0
count = 0

for line in fh:
    if not line.startswith("X-DSPAM-Confidence:"):
        continue
    # col = line.find(':')
    # fline = float(line.rstrip()[col + 1:]) # this is a 1 line strip and clip
    sline = line.rstrip()
    col = sline.find(':')
    tline = sline[col + 1:]
    fline = float(tline)
    tot += fline
    count += 1
avg = round(tot / count, 13)
# avg = round(avg, 12)
print("Average spam confidence:", avg)
