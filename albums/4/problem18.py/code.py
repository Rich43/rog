def panagram(strng):
            '''(str) -> bool
            return whether the string is a panagram
            '''
            sett = set()
            strng = strng.lower()
            for letter in strng:
                    if letter.isalpha():
                            sett.add(letter)
            return len(sett) == 26

strng = 'The quick brown fox jumps over the lazy dog'
ans = panagram(strng)
print(ans)