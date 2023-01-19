def bracketed(num):
            import random
            a ='['
            b = ']'
            c = int(num)
            lst =[]
            sett = set()
            sett.add(a)
            sett .add(b)
            # randomize the brackets
            for x in range(1,c + 1):
                    lst.append(random.sample(sett,2))
            # convert to string for display purposes.
            strng = ''
            for item in lst:
                    for items in item:
                       strng += items
            print(strng)
            # iterate in blocks to check True/False
            for i in range(0, len(strng), 2):
                    slice = strng[i:i+2]
                    if slice[0] == a and slice[1] == b:
                            continue
                    else:
                            return  False
            return  True
n = 5
#n = input('Enter amount of brackets: ' )
ans = bracketed(n)
print('Result: ', ans)