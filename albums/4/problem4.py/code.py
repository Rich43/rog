def is_vowel(str):
            '''(str) -> bool
            return str True or False
            '''
            vowels ='aeiou'
            str = str.lower()
            return  str in vowels

ans = is_vowel('R')
ans2 = is_vowel('e')
print(ans, ans2)