'''
1474 is a pandigital in Roman numerals (MCDLXXIV). It uses each of the symbols I, V, X, L, C,
and M at least once. Your challenge today is to find the small handful of pandigital Roman
numbers up to 2000.

Output Description

A list of numbers. Example:

1 (I), 2 (II), 3 (III), 8 (VIII) (Examples only, these are not pandigital Roman numbers)

Challenge Input

Find all numbers that are pandigital in Roman numerals using each of the symbols
I, V, X, L, C, D and M exactly once.
Challenge Input Solution

1444, 1446, 1464, 1466, 1644, 1646, 1664, 1666

'''
import  re

M = 1000
D = 500
C = 100
L = 50
X = 10
V = 5
I = 1

numbers ={M: 'M', D: 'D', C: 'C', L: 'L', X: 'X', V: 'V', I: 'I'}


def roman_to_decimal(candidate):
    numstring = ''
    accum = 4
    candidate = str(candidate)
    num_len = len(candidate)
    while accum > 2:
        num = re.findall(r'\d+', candidate)
        try:
            numb = int(num[0][-accum])
            numstring += numbers[M]
        except IndexError:
            pass

        '''Hundreds'''
        accum -= 1
        numb = int(num[0][-accum])  # 8
        if numb == 1:
            numbr = numbers[C]
        elif numb == 4:
            numbr = numbers[C] + numbers[D]
        elif numb > 8:
            numbr = numbers[C] + numbers[M]
        elif numb == 0:
            numbr = ''
        else:
            remainder = numb % 5
            if 1 < numb < 4:
                numbr =  str((remainder * numbers[C]))
            else:
                numbr = numbers[D] + str(remainder * numbers[C])
        numstring += numbr

        ''' Tens'''
        accum -= 1
        numb = int(num[0][-accum])
        if numb == 1:
            numbr = numbers[X]
        elif numb == 4:
            numbr = numbers[X] + numbers[L]
        elif numb > 8:
            numbr = numbers[X] + numbers[C]
        elif numb == 0:
            numbr = ''
        else:
            remainder = numb % 5
            if numb < 5:
                numbr = str((remainder * numbers[X]))
            else:
                numbr = numbers[L] + str(remainder * numbers[X])
        numstring += numbr

        ''' Ones'''
        accum -= 1
        numb = int(num[0][-accum])
        if numb == 1:
            numbr = numbers[I]
        elif numb == 4:
            numbr = numbers[I] + numbers[V]
        elif numb > 8:
            numbr = numbers[I] + numbers[X]
        elif numb == 0:
            numbr = ''
        else:
            remainder = numb % 5
            if numb < 5:
                numbr = str((remainder * numbers[I]))
            else:
                numbr = numbers[V] + str(remainder * numbers[I])
        numstring += numbr
        return numstring


if __name__ == '__main__':
    lst = []
    bonus_list = []
    num_set = set()

    for n in range(1999, 1000, -1):
        # roman to decimal
        roman_number = roman_to_decimal(n)
        # place the letters in a set
        for letter in roman_number:
            num_set.add(letter)
        # if we have seven letters = pandigital
        if len(num_set) == 7:
            lst.append(n)
            # but if the length of the number is seven = bonus
            if len(roman_number) == 7:
                bonus_list.append(n)
        num_set = set()
    print(lst, '\n', bonus_list)