'''Given a set of up to 20 letter tiles, determine the longest word from the
enable1 English word list that can be formed using the tiles.

longest("dcthoyueorza") ->  "coauthored"
longest("uruqrnytrois") -> "turquois"
longest("rryqeiaegicgeo??") -> "greengrocery"
longest("udosjanyuiuebr??") -> "subordinately"
longest("vaakojeaietg????????") -> "ovolactovegetarian"

(For all of these examples, there is a unique longest word from the list.
In the case of a tie, any word that's tied for the longest is a valid output.)'''

import re

def length_order(f):
    f = sorted(f, key=len, reverse=True)
    return f


def sort_by_length():
    # read, order by length, write back
    with open('enable1.txt') as f:
        file = f.readlines()
        # if \n not needed
        file = [line.strip('\n') for line in file]
        ordered_file = length_order(file)
    with open('sorted_enable1.txt', 'w') as f:
        for sentence in ordered_file:
            f.write(sentence + '\n')


if __name__ == '__main__':
    # sort the text by length
    len_sort = sort_by_length()

    # open text for reading a list of test sentences
    with open('sorted_enable1.txt') as f:
        word_list = f. read().splitlines()
        # list of tiles and expected results
        candidates = '''longest("dcthoyueorza") ->  "coauthored"
            longest("uruqrnytrois") -> "turquois"
            longest("rryqeiaegicgeo??") -> "greengrocery"
            longest("udosjanyuiuebr??") -> "subordinately"
            longest("vaakojeaietg????????") -> "ovolactovegetarian"'''


        # generate a list of tiles and words
        candidates = candidates.splitlines()
        tile_list = []
        for candidate in candidates:
            ans = re.findall('([a-z|\?]+)', candidate)
            tile = ans[1]
            tile = list(tile)
            tile_list.append(tile)

        # use the reserve list to check for duplicates
        reserve = []
        for tile in tile_list:
            # the test sentences
            for word in word_list:
                reserve = []
                acc = 0
                wild = tile.count('?')
                for s in word:
                    if s in tile and (reserve.count(s) < tile.count(s)):
                        reserve.append(s)
                        # add 1 for each match
                        acc += 1

                # add the accumulator and wild cards
                # compare against the length of word.
                if acc + wild >= len(word):
                    print('gotcha! ' + str(word))
                    break