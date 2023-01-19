# This took a LOT of research! so I added a bit of fluff.
def translate(lst):
            '''(list) -> list
            return a list of translated words.
            '''
            return dict[lst]

dict = {"merry":"god", "christmas":"jul", "and":"och", "happy":"gott",
    "new":"nytt", "year":"år"}

strng = 'happy new year'
strng_2_list = list(strng.split())
ans = list(map(translate, strng_2_list))
ans = ' '.join(str(x) for x in ans)
print(ans)