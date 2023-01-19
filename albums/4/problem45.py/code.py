import random
import copy
def poke45(file):
            f = open(file, 'r')
            lst = []
            lst2 = []
            count = 1
            total = 0
            list_out =[]
            temp = []
            for line in f:         # create list of text file content
                    line = line.strip('\n')
                    line = line.split()
                    for word in line:
                            lst.append(word)
                    temp = copy.deepcopy(lst)

            for x in range(0, len(lst)):
                    lst = temp
                    candidate = lst[x]     # select starting word
                    lst2.append(candidate) # place in lst2 (list)
                    trail = candidate[-1]  # select trailing letter
                    lst =lst[1:]           # list minus the selected word

                    while True:
                            if candidate == lst[-1]:
                                    break
                            if lst[x].startswith(trail): # lst[x] now the second word of the original list
                                    count += 1               # rinse and repeat......
                                    candidate = lst[x]
                                    lst2.append(lst[x])
                                    trail = lst[x][-1]
                                    del lst[x]
                                    x = 0
                            else:
                                    x += 1
                                    if x == len(lst):
                                            if count > total:
                                                    total = count
                                                    list_out = lst2
                                            lst2 = []
                                            count = 0
                                            break

            return (total, list_out )


ans = poke45('pokemon.txt')
print(ans)