import re

def truth_check(a, b):
    # a = tiles b = word
    acc = 0
    for s in b:
        if s in a:
            acc += 1
            a.remove(s)
        elif s not in a:
            try:
                a.remove('?')
                acc += 1
            except:
                continue
        else:
            continue
    # are there enough wild cards (?)
    if acc >= len(b):
        return 'true'
    else:
        return 'false'



candidates = '''scrabble("pizza??", "pizzazz") -> true
scrabble("piizza?", "pizzazz") -> false
scrabble("a??????", "program") -> true
scrabble("b??????", "program") -> false'''

candidates = candidates.splitlines()
for line in candidates:
    data = re.findall('[\?|a-z]+', line)
    tiles = data[1]
    word = data[2]
    tiles = list(tiles)


    tiles = list(tiles)

    ans = truth_check(tiles, word)
    print(ans)