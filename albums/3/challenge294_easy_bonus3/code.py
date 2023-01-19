''' Consider the case where every tile you use is worth a certain number of points,
given on the Wikpedia page for Scrabble. E.g. a is worth 1 point, b is worth 3 points, etc.

For the purpose of this problem, if you use a blank tile to form a word, it
counts as 0 points. For instance, spelling "program" from "progaaf????" gets you 8 points,
because you have to use blanks for the m and one of the rs, spelling prog?a?. T
his scores 3 + 1 + 1 + 2 + 1 = 8 points, for the p, r, o, g, and a, respectively.

Given a set of up to 20 tiles, determine the highest-scoring word from the word list
that can be formed using the tiles.

highest("dcthoyueorza") ->  "zydeco"
highest("uruqrnytrois") -> "squinty"
highest("rryqeiaegicgeo??") -> "reacquiring"
highest("udosjanyuiuebr??") -> "jaybirds"
highest("vaakojeaietg????????") -> "straightjacketed"
'''
import re


def length_sort(l):
    new_list = []
    for element in l:
        len_element = len(element)
        if (len_element < 6) or (len_element > 8):
            continue
        else:
            new_list.append(element)
    return new_list


def cmpr(wrd, tile):
    # accumulator
    acc = 0
    # wild card count
    wild_cards = tile.count('?')
    # a set of word elements
    wrd_set = set(wrd)
    # store alphabet chars in the tile.
    alpha_tile = []
    for element in tile:
        if element.isalpha():
            alpha_tile.append(element)
    for letter in wrd_set:
        wcount = wrd.count(letter)
        tcount = tile.count(letter)
        num = wcount - tcount
        if num > 0:
            acc += num

    if acc > wild_cards:
        return False
    return wrd


def maximum_score(l, l2):
    # l = valid_words
    # l2 = alphabet list
    max_score = 0
    max_word = ''
    for word in l:
        acc = 0
        word_score = 0
        for letter in word:
            score = l2[letter]
            acc += score
        if acc > max_score:
            max_score = acc
            max_word = word
    return max_word, max_score


if __name__ == '__main__':

    # open text for reading a list of test sentences
    with open('enable1.txt') as f:
        word_list = f. read().splitlines()
        word_list = length_sort(word_list)

        # list of tiles and expected results
        candidates = '''highest("dcthoyueorza") ->  "zydeco"
                    highest("uruqrnytrois") -> "squinty"
                    highest("rryqeiaegicgeo??") -> "reacquiring"
                    highest("udosjanyuiuebr??") -> "jaybirds"
                    highest("vaakojeaietg????????") -> "straightjacketed""'''

        # generate a list of tiles and words
        candidates = candidates.splitlines()
        for candidate in candidates:
            ans = re.findall('([a-z|?]+)', candidate)

            # assemble a tile list
            tile_list = []
            tile = ans[1]
            tile = list(tile)
            tile_list.append(tile)

            score_dict = {'a': 1,
                          'b': 3,
                          'c': 3,
                          'd': 2,
                          'e': 1,
                          'f': 4,
                          'g': 2,
                          'h': 4,
                          'i': 1,
                          'j': 8,
                          'k': 5,
                          'l': 1,
                          'm': 3,
                          'n': 1,
                          'o': 1,
                          'p': 3,
                          'q': 10,
                          'r': 1,
                          's': 1,
                          't': 1,
                          'u': 1,
                          'v': 4,
                          'w': 4,
                          'x': 8,
                          'y': 4,
                          'z': 10}
            valid_words = []

            # check words to see if valid
            for tile in tile_list:
                for word in word_list:
                    valid_word = cmpr(word, tile)
                    if valid_word:
                        valid_words.append(valid_word)

            # check for maximum score
            highest_score = maximum_score(valid_words, score_dict)

            print(highest_score)