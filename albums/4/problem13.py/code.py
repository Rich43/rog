def in_list(the_lst):
            '''(list) -> number
            return the largest number in a list
            '''
            num = 0
            for x in range(0, len(the_lst)):
                    if the_lst[x] > num:
                            num = the_lst[x]
            return  num

ans = in_list([5, 8, -2, 40, 1, 38])
print(ans)