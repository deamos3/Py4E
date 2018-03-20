han = open('mbox-short.txt')

for line in han:
    line = line.rstrip()
    # the following two lines are another way to skip blank lines
    # if line == '':
    #     continue
    wds = line.split()
    # we can also compound the following two checks with an or
    # and order is important, as the first check protects the second check from
    # blowing up
    # if len(wds) < 3 or wds[0] != 'From':
    # this gets a traceback due to wds[0] hitting a blank line
    # so we can add a guardian statement to protect from this
    # guardian
    if len(wds) < 3:  # this was originally 1, but having this at 3 also
                            # protects the last statement where we call wds[2]
        continue
    if wds[0] != 'From':
        continue
    print(wds[2])
