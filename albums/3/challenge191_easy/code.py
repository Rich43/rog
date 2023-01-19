'''
You've recently taken an internship at an up and coming lingustic and natural language centre.
Unfortunately, as with real life, the professors have allocated you the mundane task of
counting every single word in a book and finding out how many occurences of each word there
are.

To them, this task would take hours but they are unaware of your programming background (They
really didn't assess the candidates much). Impress them with that word count by the end of the
day and you're surely in for more smooth sailing.
Description

Given a text file, count how many occurences of each word are present in that text file. To
make it more interesting we'll be analyzing the free books offered by Project Gutenberg

The book I'm giving to you in this challenge is an illustrated monthly on birds. You're free
to choose other books if you wish.
Inputs and Outputs
Input

Pass your book through for processing
Output

Output should consist of a key-value pair of the word and its word count.
Example

{'the' : 56,
'example' : 16,
'blue-tit' : 4,
'wings' : 75}

Clarifications

For the sake of ease, you don't have to begin the word count when the book starts, you can just count
all the words in that text file (including the boilerplate legal stuff put in by Gutenberg).
Bonus

As a bonus, only extract the book's contents and nothing else.
'''
import re
word_dict = {}
with open('gutenburg.txt', 'r') as f:
    for line in f:
        line = re.findall('[a-zA-Z]+', line)
        for word in line:
            word_dict[word] = word_dict.setdefault(word, 0) + 1

print(word_dict)

#-- Bonus --------------------------------------------
text_string = ''
word_dict = {}
with open('gutenburg.txt') as f:
    for line in f:
        line = line.rstrip()
        text_string += line + ' '

    txt = re.findall('Title:.*Patagonia.', text_string)
    txt = txt[0]
    txt = re.findall('[a-zA-Z]+', txt)
    for word in txt:
        word_dict[word] = word_dict.setdefault(word, 0) + 1

print(word_dict)