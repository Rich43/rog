def make_ing_form(lst):
            '''(list) -> list
            return a modified list
            '''
            output = []
            ing = 'ing'
            for word in lst:
                    if word.endswith('ie'):
                            word = word.replace(word[-2:], 'y') + ing
                            output.append(word)
                    elif word.endswith('e'):
                            word = word.replace(word[-1], ing)
                            output.append(word)
                    else:
                            word = word + ing
                            output.append(word)

            return  output

verb_list=['try', 'brush', 'move', 'fizz', 'lie']
ans = make_ing_form(verb_list)
print(ans)