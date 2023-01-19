def correct(str):
            '''(str) -> str
            return a corrected string
            '''
            import  re

            match = re.sub(r'  ',' ',str)
            match2 = re.sub(r'\.(?=[A-Z])', '. ', match)
            return match2

strng = 'One fine  day we  walked to the  farm.It was  Wednesday.'
ans = correct(strng)
print(ans)