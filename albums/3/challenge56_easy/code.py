''' The ABACABA sequence is defined as follows: start
with the first letter of the alphabet ("a").
This is the first iteration. The second iteration,
you take the second letter ("b") and surround it with
all of the first iteration (just "a" in this case).
Do this for each iteration, i.e. take two copies of the
previous iteration and sandwich them around the next letter of the alphabet.

Here are the first 5 items in the sequence:

a
aba
abacaba
abacabadabacaba
abacabadabacabaeabacabadabacaba

And it goes on and on like that, until you get to the 26th iteration
(i.e. the one that adds the "z"). If you use one byte for each character,
the final iteration takes up just under 64 megabytes of space.

Write a computer program that prints the
26th iteration of this sequence to a file.
'''
import string
output = ''
strng = ''
# alphabetical list
alpha = [i for i in string.ascii_lowercase]

for x in range(0, 25):
    candidate = alpha[x]
    output = strng + candidate + strng
    strng = output
with open('/home/feltonortiz/webapps/files/problem56.txt', 'w') as f:
    f.write(strng)

print("Output is available at http://files.pynguins.com/problem56.txt")