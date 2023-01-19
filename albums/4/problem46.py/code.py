'''An alternade is a word in which its letters, taken alternatively in a strict sequence,
    and used in the same order as the original word, make up at least two other words.
    All letters must be used, but the smaller words are not necessarily of the same length. For example,
    a word with seven letters where every second letter is used will produce a four-letter word and a
    three-letter word. Here are two examples:

      "board": makes "bad" and "or".
      "waists": makes "wit" and "ass".

    Using the word list at http://www.puzzlers.org/pub/wordlists/unixdict.txt.
    write a program that goes through each word in the list and tries to make
    two smaller words using every second letter. The smaller words must also be
    members of the list. Print the words to the screen in the above fashion.
     '''
line = open('unixdict.txt', 'r')
lst =[]
for lines in line:
            lines = lines.strip('\n')
            lst.append(lines)

strng2 = ''
strng3 = ''

for word in lst:
            for x in range(0, len(word), 2):
                    strng2 += word[x]

            for x in range(1, len(word), 2):
                    strng3 += word[x]

            if strng2 in lst and strng3 in lst:
                    print('"{0}": makes "{1}" and "{2}"'.format(word, strng2, strng3))
                    print()
            strng2 = ''
            strng3 = ''