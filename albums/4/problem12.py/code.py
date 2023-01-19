def histogram(a, b, c):
            '''(ints) -> str
            return a histogram using three inputs
            '''
            count = 0
            strng =''
            while True:
                    lst = [a, b, c]
                    for x in range(0,len(lst)):
                            n = lst[x]
                            for y in range(n):
                                    strng += 'x'
                            print(strng)
                            strng =''
                            count +=1
                            if count == 3:
                                    exit()

ans = histogram(2, 3, 4)
print(ans)