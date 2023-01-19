def char_freq(str):
            '''(str) -> dict
            return a dictionary representing
            frequency distribution.
            '''
            dict ={}
            count = 0
            store =''
            for y in range(len(str)):
                    for letter in str:
                            if letter == str[y] and letter not in store:
                                    count += 1
                    if count == 0:
                            continue
                    store += str[y]
                    dict[str[y]] = count
                    count  = 0
            return dict

chars = "abbabcbdbabdbdbabababcbcbab"
ans = char_freq(chars)
print(ans)