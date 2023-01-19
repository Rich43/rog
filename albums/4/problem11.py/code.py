def generate_n_chars(char, n):
            ''' (str, int) -> str
            return n number of characters
            '''
            str = ''
            for x in range(n):
                    str += char
            return  str

ans = generate_n_chars('w', 6)
print(ans)