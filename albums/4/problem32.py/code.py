# requires palindrome.txt

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



def palindrome_printer():
            f = open('palindrome.txt', 'r')
            for line in f:
                    line = line.strip('\n')
                    if is_phrase_palindrome(line):
                            print(line)


ans = palindrome_printer()
print(ans)