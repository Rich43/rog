import re

def truth_check(a, b):
    # a = tiles b = word
    acc = 0
    for s in b:
        if s in a:
            acc += 1
            a.remove(s)
    if acc >= len(b):
        return 'true'
    else:
        return 'false'


candidates = '''scrabble("ladilmy", "daily") -> true
scrabble("eerriin", "eerie") -> false
scrabble("orrpgma", "program") -> true
scrabble("orppgma", "program") -> false'''

candidates = candidates.splitlines()
for line in candidates:
    data = re.findall('[\?|a-z]+', line)
    tiles = data[1]
    word = data[2]
    tiles = list(tiles)

    ans = truth_check(tiles, word)
    print(ans)