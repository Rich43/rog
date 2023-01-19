from functools import reduce
def reduce_func(lst):
            '''(list) -> number
            return the maximum number in the list
            '''
            f = lambda a,b: a if (a > b) else b
            maximum = reduce(f, lst)
            return maximum

num_list = [47,11,42,102,13]
ans = reduce_func(num_list)
print(ans)

# reduce is a function and may be called directly

f = lambda a,b: a if (a > b) else b
maximum = reduce(f, [47,11,42,102,13])
print(maximum)