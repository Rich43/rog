'''
Print out the lyrics of The Twelve Days of Christmas
'''
import re

num_to_text = {
            'and 1': 'and one',
            '1': 'one',
            '2': 'two',
            '3': 'three',
            '4': 'four',
            '5': 'five',
            '6': 'six',
            '7': 'seven',
            '8': 'eight',
            '9': 'nine',
            '10': 'ten',
            '11': 'eleven',
            '12': 'twelve'
}

with open('296.txt') as file:
    for line in file:
        line = line.rstrip()
        sample = re.findall('^\d+|^[a-z]+\s\d+', line)
        if sample:
            sample = sample[0]
            sample2 = num_to_text[sample]
            line = re.sub(sample, sample2, line)

            print(line)

with open('296_bonus2.txt') as file:
    num = 1
    for line in file:
        line = line.rstrip()
        print(num_to_text[str(num)] + ' ' + line)
        num += 1