fname = 'words.txt'
fh = open(fname)
lst = []
count = 0
total = 0
for line in fh:
            line = line.rstrip('\n').split()
            for word in line:
                    lst.append(word)
                    count += 1
for x in range(0, len(lst)):
            total += len(lst[x])

av = float(total / count)

print('Average word length: ',av)