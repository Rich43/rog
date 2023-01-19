def filter_long_words(lst, n):
            '''(list) -> list
            return a filtered list
            '''
            filtered_list = []
            for word in lst:
                    if len(word) > n:
                            filtered_list.append(word)
            return filtered_list

lst = ['an', 'answer', 'racket', 'a', 'modal']
ans = filter_long_words(lst, 4)
print(ans)