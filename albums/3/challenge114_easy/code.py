'''
A word ladder is a sequence of words made by changing one letter at a time. For example:

cold → cord → card → ward → warm

Given a word, list all the words that can appear next to it in a word ladder,
using this list of 3,807 four-letter words. Sample input:

puma

Sample output:

duma
pima
puja
pula
pump
puna
pupa

How many words from the list can appear next to the word best in a word ladder?

Bonus 1: One word in the list has 33 other words that can appear next to it. What is this word?

Bonus 2: How many different words can be reached, starting from best, in 3 or fewer steps?
'''
import re

word_set = set()
with open('selected_four_letter_words.txt') as f:
    for line in f:
        line = line.strip()
        word_set.add(line)

output = list()
alpha_string = 'abcdefghijklmnopqrstuvwxyz'
word = 'puma'

for letter in word:
    for item in alpha_string:
        sub_word = re.sub(letter, item, word)
        if sub_word in word_set:
            if sub_word == word:
                continue
            if sub_word not in output:
                output.append(sub_word)

print(output)