def is_phrase_palindrome(str):
            '''(str) -> str
            return true if palindrome
            '''
            filtered_str = ''
            for letter in str:
                    if letter.isalpha():
                            filtered_str += letter
            str = filtered_str.lower()

            reverse_str = str[:: -1]
            half_len =len(str) // 2
            r_str = ''
            f_str =''
            for x in range(0, half_len):
                r_str += reverse_str[x]
            for y in range(0, half_len):
                f_str += str[y]



            return  r_str == f_str

is_or_not_pal = "Dammit, I'm mad"
ans = is_phrase_palindrome(is_or_not_pal)
print(ans)