def reverse(str):
            ''' (str) -> str
            return reversed string
            '''
            str2 = ''
            ln = len(str)
            for x in range( ln-1, -1, -1):
                    str2 =str2 + str[x]
            return  str2

str = 'I am testing'
ans = reverse(str)
print(ans)