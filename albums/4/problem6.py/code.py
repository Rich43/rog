def sum(lst):
            '''(list) -> number
            return a sum of a list
            '''
            num = 0
            for x in range(0, len(lst)):
                    num += lst[x]
            return num

def multiply(lst):
            '''(list) -> number
            return a sum of a list
            '''
            num = 1
            for x in range(0, len(lst)):
                    num *= lst[x]
            return num

lst =[1, 2, 3, 4]
ans = sum(lst)
ans2 = multiply(lst)
print(ans, ans2)