def leng(str):
            '''(str) -> integer
            return the length of a string
            '''
            count = 0
            for x in str:
                    count += 1
            return count

ans = leng('there')
print(ans)