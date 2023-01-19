def is_palindrome(str):
            '''(str) -> str
            return bool if str is a palindrome
            '''
            half_str = len(str) // 2
            rear_str = ''
            front_str = ''

            for x in range( half_str - 1, -1, -1):
                    rear_str += str[x]
            rear_str = rear_str[::-1]
            for x in range(0,half_str):
                    front_str += str[x]

            return  rear_str == front_str



ans = is_palindrome('radar')
print(ans)