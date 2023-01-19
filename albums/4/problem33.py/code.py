# requires semordnilap.txt

def semordnilap():
            f = open('semordnilap.txt','r')
            word_store = []
            sorted_in_pairs = []
            for line in f:
                    line = line.strip().split()
                    for word in line:
                            word_store.append(word)
            for x in range(0, len(word_store)):
                    candidate = word_store[x]
                    target = candidate[::-1]
                    if target in word_store:
                            sorted_in_pairs.append((target,candidate))
            # remove duplicates
            for x in sorted_in_pairs:
                    for y in sorted_in_pairs:
                            if x[0] == y[1]:
                                    sorted_in_pairs.remove(x)
            print(len(sorted_in_pairs))
            return (sorted_in_pairs)



ans = semordnilap()
print(ans)