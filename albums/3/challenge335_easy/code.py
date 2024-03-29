'''


We'll call the consecutive distance rating of an integer sequence
the sum of the distances between consecutive integers. Consider
the sequence 1 7 2 11 8 34 3. 1 and 2 are consecutive integers,
but their distance apart in the sequence is 2. 2 and 3 are
consecutive integers, and their distance is 4. The distance
between 7 and 8 is 3. The sum of these distances is 9.

Your task is to find and display the consecutive distance rating
of a number of integer sequences.
Input description

You'll be given two integers a and b on the first line denoting
the number of sequences that follow and the length of those
sequences, respectively. You'll then be given a integer
sequences of length b, one per line. The integers will always
be unique and range from 1 to 100 inclusive.
Example input

6 11
31 63 53 56 96 62 73 25 54 55 64
77 39 35 38 41 42 76 73 40 31 10
30 63 57 87 37 31 58 83 34 76 38
18 62 55 92 88 57 90 10 11 96 12
26 8 7 25 52 17 45 64 11 35 12
89 57 21 55 56 81 54 100 22 62 50

Output description

Output each consecutive distance rating, one per line.
Example output

26
20
15
3
6
13

Challenge input

6 20
76 74 45 48 13 75 16 14 79 58 78 82 46 89 81 88 27 64 21 63
37 35 88 57 55 29 96 11 25 42 24 81 82 58 15 2 3 41 43 36
54 64 52 39 36 98 32 87 95 12 40 79 41 13 53 35 48 42 33 75
21 87 89 26 85 59 54 2 24 25 41 46 88 60 63 23 91 62 61 6
94 66 18 57 58 54 93 53 19 16 55 22 51 8 67 20 17 56 21 59
6 19 45 46 7 70 36 2 56 47 33 75 94 50 34 35 73 72 39 5
'''

candidates = '''76 74 45 48 13 75 16 14 79 58 78 82 46 89 81 88 27 64 21 63
37 35 88 57 55 29 96 11 25 42 24 81 82 58 15 2 3 41 43 36
54 64 52 39 36 98 32 87 95 12 40 79 41 13 53 35 48 42 33 75
21 87 89 26 85 59 54 2 24 25 41 46 88 60 63 23 91 62 61 6
94 66 18 57 58 54 93 53 19 16 55 22 51 8 67 20 17 56 21 59
6 19 45 46 7 70 36 2 56 47 33 75 94 50 34 35 73 72 39 5'''

import re

candidates = candidates.splitlines()

for nums in candidates:
    nums = re.findall('\d+', nums)
    num_list = []
    for item in nums:
        num_list.append(int(item))

    # index each number then reverse for reference.
    enum = list(enumerate(num_list))
    lst = []
    for tup in enum:
        # reverse the tuple
        tup = tup[::-1]
        lst.append(tup)

    lst = sorted(lst)
    n = 0
    for x in range(0, len(lst) - 1):
        if lst[x + 1][0] == lst[x][0] + 1:
                m = lst[x + 1][1] - lst[x][1]
                n += abs(m)


    print(n)