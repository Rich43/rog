def is_member(lst, a):
            '''(list,str) -> bool
            return whether str is a member of lst
            '''
            x = 0
            while x <= len(lst) - 1:
                    if lst[x] == a:
                            return True
                    x += 1
                    continue
            return False

lst =['a', 'c', 'f', 'g']
str = 'g'
ans = is_member(lst, str)
print(ans)