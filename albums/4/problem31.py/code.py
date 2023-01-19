y =[3, 4, 7]

def my_map(lst):
            doubled = []
            for x in lst:
                    x *= 3
                    doubled.append(x)
            return doubled


ans = my_map(y)
print(ans)

def my_filter(lst):
            filtered = []
            for x in range(0, len(lst)):
                    a = lst[x]
                    if a < 7:
                            filtered.append(a)
            return filtered

ans = my_filter(y)
print(ans)


def my_reduce(lst):
            a = lst[0]
            for x in range(1, len(lst)):
                    b = lst[x]
                    a /= b
            return a

ans = my_reduce(y)
print(ans)