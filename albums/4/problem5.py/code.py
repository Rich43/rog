def translate(str):
            '''(str) -> str
            return modified string
            '''
            vowels = 'aeiou '
            strng = ''
            for x in str:
                    if x not in vowels:
                            x = x +'o' + x
                            strng = strng + x
                    else:
                            strng = strng + x

            return strng

ans = translate('this is fun')
print(ans)