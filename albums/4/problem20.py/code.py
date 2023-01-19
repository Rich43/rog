def translate(lst):
            '''(list) -> list
            return a list of translated words
            '''
            dict = {'christmas': 'jul', 'day': 'dag'}

            lst2 =[]
            for word in lst:
                    lst2.append(dict[word])
            return  lst2

eng_list = ['christmas', 'day']
ans = translate(eng_list)
print(ans)