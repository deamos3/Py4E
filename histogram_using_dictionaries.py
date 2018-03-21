counts = dict()
names = ['csev', 'cwen', 'csev', 'zqian', 'cwen']
for name in names:
    if name not in counts:
        counts[name] = 1
    else:
        counts[name] += 1
print(counts)

# a quicker way, the get method for dictionaries

# sample of how the quicker way is constructed
if name in counts:
    x = counts[name]
else:
    x = 0
x = counts.get(name, 0)  # here name is a key, and 0 is the default value

# the quicker way
for name in names:
    counts[name] = counts.get(name, 0) + 1  # for new keys 0 is used as the
    # value, but for existing keys the current value is used, and 1 is added
print(counts)
