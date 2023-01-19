'''
To disarm the bomb you have to cut some wires. These wires are either white, black, purple, red, green or orange.

The rules for disarming are simple:

If you cut a white cable you can't cut white or black cable.
If you cut a red cable you have to cut a green one
If you cut a black cable it is not allowed to cut a white, green or orange one
If you cut a orange cable you should cut a red or black one
If you cut a green one you have to cut a orange or white one
If you cut a purple cable you can't cut a purple, green, orange or white cable

If you have anything wrong in the wrong order, the bomb will explode.
'''


def bomb_squad(l, l2):
    for x in range(0, len(l) -1):
        col1 = l[x]
        col2 = l[x + 1]
        if col2 in l2[col1]:
            return 'boom!'
    return 'defused!'


wire_combos = [['white', 'red', 'green', 'white'], ['white', 'orange', 'green', 'white']]

colour_dict = {'white': ['white', 'black'],
               'red': ['white', 'black', 'orange', 'purple'],
               'black': ['white', 'green', 'orange'],
               'orange': ['white', 'red', 'green', 'purple'],
               'green': ['red', 'black', 'green', 'purple'],
               'purple': ['purple', 'green', 'orange', 'white']}


for combo in wire_combos:
    result = bomb_squad(combo, colour_dict)
    print(result)