'''
Morse code, as we are all aware, consists of dots and dashes. Lets define a "Morse code sequence"
as simply a series of dots and dashes (and nothing else). So ".--.-.--" would be a morse code
sequence, for instance.

Dashes obviously take longer to transmit, that's what makes them dashes. Lets say that a dot takes
1 unit of time to transmit, and a dash takes 2 units of time. Then we can say that the "size" of a
certain morse code sequence is the sum of the time it takes to transmit the dots and dashes. So,
for instance "..-." would have a size of 5 (since there's three dots taking three units of time and
one dash taking two units of time, for a total of 5). The sequence "-.-" would also have a size of 5.

In fact, if you list all the the possible Morse code sequences of size 5, you get:

.....  ...-  ..-.  .-..  -...  .--  -.-  --.

A total of 8 different sequences.

Your task is to write a function called Morse(X) which generates all morse code sequences of size X
and returns them as an array of strings (so Morse(5) should return the 8 strings I just mentioned,
in some order).

Use your function to generate and print out all sequences of size 10.

Bonus: Try and write your code so that it can generate Morse(35) (or even Morse(36) or higher, but that
takes a significant amount of memory) in a "reasonable" amount of time. "Reasonable" obviously depend on
what computer and programming language you are using, but a good rule of thumb should be that it should
finish in less than a minute.
Being a morse enthusiast I have dealt with the code itself, numbers and letters.
'''

import re
# read in the morse letters and numbers
morse_dict = {}
# create a morse dictionary
with open('morse.txt') as f:
    while True:
        line = f.readline()
        if not line:
            break
        if line[0].isalnum():
            a = line[0]
            b = re.findall('\w\s(\S+)', line)
            morse_dict[a] = b
def morse(x):
    # convert morse to units of time
    morse_count = {}  # morse character and unit count
    #N = 2 # value of sequence required
    sequence = [] # number of sequences found
    code_count = 0 # unit count of character
    for k,v in morse_dict.items():
        for char in v[0]:
            if char == '.':
                code_count += 1
            else:
                code_count += 2
        if code_count == x:
            sequence.append(v)
        morse_count[k] = code_count
        code_count = 0
    return sequence

if __name__ == '__main__':
    N = 10
    ans = morse(N)
    print(ans)