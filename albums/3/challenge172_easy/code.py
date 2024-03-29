'''
A portable bitmap is one of the oldest image formats around and grants access to very simple image creation and sharing. Today, you will be creating an image of this format.

A simple PBM program can be seen here (Note that we'll be
creating the simplest version, a PBM, not PPM or PGM.)

But basically the program consists of the following:

    A 2byte string (usually 'P1') denoting the file format
    for that PBM

    2 integers denoting the Width and Height of our image
    file respectively

    And finally, our pixel data - Whether a pixel is 1 - Black or 0 - White.

Formal Inputs & Outputs
Input description

On standard console input you should be prompted to enter a
small piece of text ("programming", "proggit", "hello world" etc...)
Output description

The output will be a .PBM file consiting of an image which
contains the text you have entered
'''

code = '''
A
0 0 1 0 0
0 1 0 1 0
1 0 0 0 1
1 1 1 1 1
1 0 0 0 1
1 0 0 0 1
1 0 0 0 1
B
1 1 1 1 0
1 0 0 0 1
1 0 0 0 1
1 1 1 1 0
1 0 0 0 1
1 0 0 0 1
1 1 1 1 0
C
0 1 1 1 0
1 0 0 0 1
1 0 0 0 0
1 0 0 0 0
1 0 0 0 0
1 0 0 0 1
0 1 1 1 0
D
1 1 1 1 0
1 0 0 0 1
1 0 0 0 1
1 0 0 0 1
1 0 0 0 1
1 0 0 0 1
1 1 1 1 0
E
1 1 1 1 1
1 0 0 0 0
1 0 0 0 0
1 1 1 1 0
1 0 0 0 0
1 0 0 0 0
1 1 1 1 1
F
1 1 1 1 1
1 0 0 0 0
1 0 0 0 0
1 1 1 1 0
1 0 0 0 0
1 0 0 0 0
1 0 0 0 0
G
0 1 1 1 1
1 0 0 0 0
1 0 0 0 0
1 0 0 1 1
1 0 0 0 1
1 0 0 0 1
0 1 1 1 1
H
1 0 0 0 1
1 0 0 0 1
1 0 0 0 1
1 1 1 1 1
1 0 0 0 1
1 0 0 0 1
1 0 0 0 1
I
0 1 1 1 0
0 0 1 0 0
0 0 1 0 0
0 0 1 0 0
0 0 1 0 0
0 0 1 0 0
0 1 1 1 0
J
0 0 0 0 1
0 0 0 0 1
0 0 0 0 1
0 0 0 0 1
0 0 0 0 1
1 0 0 0 1
0 1 1 1 1
K
1 0 0 0 1
1 0 0 1 0
1 0 1 0 0
1 1 0 0 0
1 0 1 0 0
1 0 0 1 0
1 0 0 0 1
L
1 0 0 0 0
1 0 0 0 0
1 0 0 0 0
1 0 0 0 0
1 0 0 0 0
1 0 0 0 0
1 1 1 1 1
M
1 0 0 0 1
1 1 0 1 1
1 0 1 0 1
1 0 0 0 1
1 0 0 0 1
1 0 0 0 1
1 0 0 0 1
N
1 0 0 0 1
1 0 0 0 1
1 1 0 0 1
1 0 1 0 1
1 0 0 1 1
1 0 0 0 1
1 0 0 0 1
O
0 1 1 1 0
1 0 0 0 1
1 0 0 0 1
1 0 0 0 1
1 0 0 0 1
1 0 0 0 1
0 1 1 1 0
P
1 1 1 1 0
1 0 0 0 1
1 0 0 0 1
1 1 1 1 0
1 0 0 0 0
1 0 0 0 0
1 0 0 0 0
Q
0 1 1 1 0
1 0 0 0 1
1 0 0 0 1
1 0 0 0 1
1 0 1 0 1
0 1 1 1 0
0 0 0 1 1
R
1 1 1 1 0
1 0 0 0 1
1 0 0 0 1
1 1 1 1 0
1 0 1 0 0
1 0 0 1 0
1 0 0 0 1
S
0 1 1 1 0
1 0 0 0 1
1 0 0 0 0
0 1 1 1 0
0 0 0 0 1
1 0 0 0 1
0 1 1 1 0
T
1 1 1 1 1
0 0 1 0 0
0 0 1 0 0
0 0 1 0 0
0 0 1 0 0
0 0 1 0 0
0 0 1 0 0
U
1 0 0 0 1
1 0 0 0 1
1 0 0 0 1
1 0 0 0 1
1 0 0 0 1
1 0 0 0 1
0 1 1 1 0
V
1 0 0 0 1
1 0 0 0 1
1 0 0 0 1
1 0 0 0 1
1 0 0 0 1
0 1 0 1 0
0 0 1 0 0
W
1 0 0 0 1
1 0 0 0 1
1 0 0 0 1
1 0 1 0 1
1 1 0 1 1
1 0 0 0 1
1 0 0 0 1
X
1 0 0 0 1
1 0 0 0 1
0 1 0 1 0
0 0 1 0 0
0 1 0 1 0
1 0 0 0 1
1 0 0 0 1
Y
1 0 0 0 1
1 0 0 0 1
0 1 0 1 0
0 0 1 0 0
0 0 1 0 0
0 0 1 0 0
0 0 1 0 0
Z
1 1 1 1 1
0 0 0 0 1
0 0 0 1 0
0 0 1 0 0
0 1 0 0 0
1 0 0 0 0
1 1 1 1 1

'''
import re

candidates = 'PYTHONISTA'
wordlist = []
for candidate in candidates:

    pattern = re.compile(r'{0}\n(((\d\s|\d|\n))+)'.format(candidate))
    ans = re.findall(pattern, code)
    ans = ''.join(ans[0])
    ans = ans.split('\n')
    wordlist.append(ans[:7])

lst = sum(wordlist, [])

cols = len(candidates)
lenl = int(len(lst))
split = [lst[i:i + int(lenl / cols)] for i in range(0, lenl, int(lenl / cols))]

for row in zip(*split):
    print("".join(str.ljust(i, 12) for i in row))