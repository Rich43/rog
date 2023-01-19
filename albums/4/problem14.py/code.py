def map(lst):
            '''(list) -> list
            return a mapped list
            '''
            map_list = []
            for word in lst:
                    leng = len(word)
                    map_list.append(leng)
            return map_list

word_list = ['one', 'four', 'seven']
ans = map(word_list)
print(ans)