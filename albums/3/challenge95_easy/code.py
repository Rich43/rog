'''
Write a program that reads text from a file, and then outputs
the text to another file but with all the lines reversed and
all the words in each line reversed.

So, for instance, if you had one file called the "thetyger.txt"
which contained the two first verses of William Blake's The Tyger:

Tyger! Tyger! burning bright
In the forests of the night,
What immortal hand or eye
Could frame thy fearful symmetry?

In what distant deeps or skies
Burnt the fire of thine eyes?
On what wings dare he aspire?
What the hand dare sieze the fire?

Your program would output this to "thetyger2.txt"
(or whatever you want to call the file):

fire? the sieze dare hand the What
aspire? he dare wings what On
eyes? thine of fire the Burnt
skies or deeps distant what In

symmetry? fearful thy frame Could
eye or hand immortal What
night, the of forests the In
bright burning Tyger! Tyger!


'''

file = 'theTyger.txt'
with open(file) as f:
    txt = []
    for line in f:
        line = line.strip('\n')
        txt.append(line)
temp = ''
txt2 = txt[::-1]
lst = []
for x in range(0, len(txt2)):
    temp = txt2[x]
    temp = temp.split()
    temp = temp[::-1]

    lst.append(temp)

with open('theTyger3.txt', 'x') as f:
    for item in lst:
        item = ' '.join(item) + '\n'
        f.write(item)