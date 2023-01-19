def filter_long_words(lst, n):
            '''(list) -> list
            return a list of words filtered
            by length n
            '''
            f = list(filter(lambda x: len(x) >= n, word_list2))
            return  f

word_list2 = ['filter', 'my', 'list', 'nevertheless']
ans = filter_long_words(word_list2, 6)
print(ans)