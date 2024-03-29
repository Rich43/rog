'''
Software like Swype and SwiftKey lets smartphone users enter text by dragging
their finger over the on-screen keyboard, rather than tapping on each letter.

Example image of Swype

You'll be given a string of characters representing the letters the user
has dragged their finger over.

For example, if the user wants "rest", the string of input characters
might be "resdft" or "resert".
Input

Given the following input strings, find all possible output words 5
characters or longer.

    qwertyuytresdftyuioknn
    gijakjthoijerjidsdfnokg

Output

Your program should find all possible words (5+ characters)
that can be derived from the strings supplied.

Use http://norvig.com/ngrams/enable1.txt as your search dictionary.

The order of the output words doesn't matter.

    queen question
    gaeing garring gathering gating geeing gieing going goring

Notes/Hints

Assumptions about the input strings:

    QWERTY keyboard
    Lowercase a-z only, no whitespace or punctuation
    The first and last characters of the input string will always
    match the first and last characters of the desired output word
    Don't assume users take the most efficient path between letters
    Every letter of the output word will appear in the input string

'''


def swype(s):
    s2 = s[::]
    lst = []
    temp = ''
    with open('enable1.txt') as f:
        for word in f:
            # resets s between words
            s = s2
            temp = ''
            word = word.strip('\n')
            # word at least 5 letters and start / finish letters
            if len(word) >= 5 and word[0] == s[0] and word[-1] == s[-1]:
                temp = ''
                for y in range(0, len(word)):
                    for x in range(0, len(s)):
                        if s[x] == word[y]:
                            s = s[x:]
                            temp += word[y]
                            if temp == word:
                                lst.append(word)
                                break
                            else:
                                break

    print(lst)


if __name__ == '__main__':
    string1 = 'qwertyuytresdftyuioknn'
    string2 = 'gijakjthoijerjidsdfnokg'

    ans = swype(string1)
    print(ans)

    ans = swype(string2)
    print(ans)