def find_longest_word(lst):
            '''(list) -> int
            return length of the longest
            word in the list
            '''
            num = 0
            for word in lst:
                    if len(word) > num:
                            num = len(word)
            return num

lst = ['are','there', 'longer', 'alphabets', 'than', 'this']
ans = find_longest_word(lst)
print(ans)