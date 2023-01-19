'''
A sequence of n > 0 integers is called a jolly jumper if the absolute values of the differences
between successive elements take on all possible values through n - 1 (which may include
negative numbers). For instance,

1 4 2 3

is a jolly jumper, because the absolute differences are 3, 2, and 1, respectively.
The definition implies that any sequence of a single integer is a jolly jumper. Write a program
to determine whether each of a number of sequences is a jolly jumper.
Input Description

You'll be given a row of numbers. The first number tells you the number of integers to calculate
over, N, followed by N integers to calculate the differences. Example:

4 1 4 2 3
8 1 6 -1 8 9 5 2 7

Output Description

Your program should emit some indication if the sequence is a jolly jumper or not. Example:

4 1 4 2 3 JOLLY
8 1 6 -1 8 9 5 2 7 NOT JOLLY

Challenge Input

4 1 4 2 3
5 1 4 2 -1 6
4 19 22 24 21
4 19 22 24 25
4 2 -1 0 2

Challenge Output

4 1 4 2 3 JOLLY
5 1 4 2 -1 6 NOT JOLLY
4 19 22 24 21 NOT JOLLY
4 19 22 24 25 JOLLY
4 2 -1 0 2 JOLLY

'''
import re

def sorted_set(n):
    sett = set()
    for x in range(1, n):
        sett.add(x)

    sett = set(sorted(sett))
    return sett


def string_set(n):
    s_set = set(n)
    s_set = set(sorted(s_set))
    return s_set


candidates = '''4 1 4 2 3
5 1 4 2 -1 6
4 19 22 24 21
4 19 22 24 25
4 2 -1 0 2'''

num_set = set()

candidates = candidates.splitlines()
for strng in candidates:
    num_set = set()
    temp = strng[1:]
    strng = re.findall('[-]?\d+', strng)
    strng = list(map(int, strng))
    n = strng[0]
    test_set = sorted_set(n)
    for x in range(1, len(strng) - 1):
        num_set.add(abs(strng[x] - strng[x + 1]))
    strng_set = string_set(num_set)
    if test_set == strng_set:
        print('{0}{1}'.format(temp, ' JOLLY'))
    else:
        print('{0}{1}'.format(temp, ' NOT JOLLY'))