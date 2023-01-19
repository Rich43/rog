# requires hapax_test.txt

def hapax():
            '''(text file) -> histogram
            generate a histogram based on a text file
            '''
            store = []
            store2 = []
            #input_text = input('Enter a text file: ')
            file = open('hapax_test.txt', 'r')
            for line in file:
                    line = line.lower()
                    line = line.strip().split()
                    for word in line:
                            if word.isalpha():
                                    store.append(word)

            for x in range (0, len(store)):
                    candidate = store[x]
                    if store.count(candidate) == 1:
                            store2.append(candidate)
            return store2

ans = hapax()
print(ans)