'''
Wikipedia has a great definition for Pangrams: "A pangram or holoalphabetic sentence for a given alphabet
is a sentence using every letter of the alphabet at least once." A good example is the English-language
sentence "The quick brown fox jumps over the lazy dog"; note how all 26 English-language letters are used
in the sentence.

Your goal is to implement a program that takes a series of strings (one per line) and prints either True
(the given string is a pangram), or False (it is not).

Bonus: On the same line as the "True" or "False" result, print the number of letters used, starting from
'A' to 'Z'. The format should match the following example based on the above sentence:

a: 1, b: 1, c: 1, d: 1, e: 3, f: 1, g: 1, h: 2, i: 1, j: 1, k: 1, l: 1, m: 1, n: 1, o: 4, p: 1, q: 1, r: 2,
s: 1, t: 2, u: 2, v: 1, w: 1, x: 1, y: 1, z: 1

Formal Inputs & Outputs
Input Description

On standard console input, you will be given a single integer on the first line of input. This integer
represents the number of lines you will then receive, each being a string of alpha-numeric characters
 ('a'-'z', 'A'-'Z', '0'-'9') as well as spaces and period.
Output Description

For each line of input, print either "True" if the given line was a pangram, or "False" if not.
Sample Inputs & Outputs
Sample Input

3
The quick brown fox jumps over the lazy dog.
Pack my box with five dozen liquor jugs
Saxophones quickly blew over my jazzy hair

Sample Output

True
True
False

'''

import string


def alphabet(s):
    alpha_dict = {}

    for letter in line:
        letter = letter.lower()
        if letter.isalpha():
            alpha_dict[letter] = alpha_dict.get(letter, 0) + 1
    return ((len(alpha_dict), alpha_dict))


if __name__ == '__main__':
    alpha_string = string.ascii_lowercase

    candidates = '''The quick brown fox jumps over the lazy dog.
    Pack my box with five dozen liquor jugs
    Saxophones quickly blew over my jazzy hair
    Fat hag dwarves quickly zap jinx mobs'''

    candidates = candidates.splitlines()
    for line in candidates:
        ans = alphabet(line)
        if ans[0] == 26:
            print('{0}{1}'.format('True.', ans[1]))
        else:
            print('{0}{1}'.format('False.', ans[1]))