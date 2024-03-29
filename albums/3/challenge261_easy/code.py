'''
A 3x3 magic square is a 3x3 grid of the numbers 1-9 such that each row, column, and major diagonal
adds up to 15. Here's an example:

8 1 6
3 5 7
4 9 2

The major diagonals in this example are 8 + 5 + 2 and 6 + 5 + 4. (Magic squares have appeared here on
r/dailyprogrammer before, in #65 [Difficult] in 2012.)

Write a function that, given a grid containing the numbers 1-9, determines whether it's a magic square.
Use whatever format you want for the grid, such as a 2-dimensional array, or a 1-dimensional array of
length 9, or a function that takes 9 arguments. You do not need to parse the grid from the program's
input, but you can if you want to. You don't need to check that each of the 9 numbers appears in the
grid: assume this to be true.
Example inputs/outputs

[8, 1, 6, 3, 5, 7, 4, 9, 2] => true
[2, 7, 6, 9, 5, 1, 4, 3, 8] => true
[3, 5, 7, 8, 1, 6, 4, 9, 2] => false
[8, 1, 6, 7, 5, 3, 4, 9, 2] => false

Optional bonus 1

Verify magic squares of any size, not just 3x3.
Optional bonus 2

Write another function that takes a grid whose bottom row is missing, so it only has the first 2 rows
(6 values). This function should return true if it's possible to fill in the bottom row to make a magic
square. You may assume that the numbers given are all within the range 1-9 and no number is repeated.
Examples:

[8, 1, 6, 3, 5, 7] => true
[3, 5, 7, 8, 1, 6] => false

Hint: it's okay for this function to call your function from the main challenge.

This bonus can also be combined with optional bonus 1. (i.e. verify larger magic squares that
are missing their bottom row.)
'''
import math

def the_magic_test(l):
    side = len(l[0])
    N = sum(l[0])
    p = 0
    # diagonal
    magic = 0
    for x in range(0, n):
        num = l[x][p]
        magic += num
        p += 1
    if magic != N:
        return False
    # horizontal columns
    magic = 0
    for x in range(0, side):
        for y in range(0, side):
            num = l[x][y]
            magic += num
        if magic != N:
            return False
        magic = 0
    # vertical columns
    magic = 0
    for x in range(0, side):
        for y in range(0, side):
            num = l[y][x]
            magic += num
        if magic != N:
            return False
        magic = 0
    return True



lsts = [[8, 1, 6, 3, 5, 7, 4, 9, 2],
        [2, 7, 6, 9, 5, 1, 4, 3, 8],
        [3, 5, 7, 8, 1, 6, 4, 9, 2],
        [8, 1, 6, 7, 5, 3, 4, 9, 2]]

# Varahamihira square
lsts1 = [[2, 3, 5, 8, 5, 8, 2, 3, 4, 1, 7, 6, 7, 6, 4, 1]]


# split into list of lists for indexing
for lst in lsts:
    i = 0
    new_list = []
    while i < len(lst):
        n = int(math.sqrt(len(lst)))
        new_list.append(lst[i:i+n])
        i += n


    # first check,is it magic?
    ans = the_magic_test(new_list)
    if ans:
        pass
    else:
        print('False')
        continue
    # reverse and test
    new_list = list(reversed(new_list))

    ans = the_magic_test(new_list)
    if ans:
        print('True')
    else:
        print('False')