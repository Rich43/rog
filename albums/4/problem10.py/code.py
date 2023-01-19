def overlapping(lst,lst2):
            '''(lists) -> bool
            return True if they have at least
            one member in common
            '''
            for x in range(0, len(lst)):
                    for y in range(0, len(lst2)):
                            if lst[x] == lst2[y]:
                                    return True
            return False

list_one =[1, 2, 3, 4]
list_two = [5, 6, 7, 8]

ans = overlapping(list_one, list_two)
print(ans)