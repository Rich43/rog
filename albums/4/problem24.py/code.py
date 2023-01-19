def make_3g_form(lst):
            '''(list) -> list
            return a modified list
            '''
            output = []
            ies = 'ies'
            es = 'es'
            s ='s'
            for word in lst:
                    if word.endswith('y'):
                            word = word.replace(word[-1], ies)
                            output.append(word)
                    elif word.endswith('s') or  word.endswith('o')\
                            or word.endswith('ch') or word.endswith('sh')\
                            or word.endswith('x') or word.endswith('z'):
                            word = word + es
                            output.append(word)
                    else:
                            word = word + s
                            output.append(word)

            return  output

verb_list=['try', 'brush', 'move', 'hug', 'fizz']
ans = make_3g_form(verb_list)
print(ans)