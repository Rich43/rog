'''
Poor Mr.Tinkles is having some troubles. Similar to The Loneliest Whale In The World,
no one can hear his cries. Or in this case, understand them.

He talks in a sequence of on's and off's. 0's and 1's, it's binary.
Obviously as a mere human you can't possibly translate what he's saying as he says it.
Looks like you'll have to think of a way around this....
Formal Inputs & Outputs
Input description

On console input you will be given a variable number of 0's and 1's that correspond
to letters in the alphabet [a-z] and whitespace ' '. These will be integers coming in,
it's your job to cast them however you need.
Output description

The program should output the english translation (or other languages
if you feel so inclined!) of the binary phrase
Samples

Input

010010000110010101101100011011000110111100100
0000101011101101111011100100110110001100100

Output

Hello World

Test Input
1

011100000110110001100101011000

010111001101100101001000000111

010001100001011011000110101100

100000011101000110111100100000

0110110101100101
2

011011000110100101100110011001

010010000001110010011010010110

011101101000011101000010000001

101110011011110111011100100000

011010010111001100100000011011

000110111101101110011001010110

110001111001
'''

astring = """010010000110010101101100011011000110111100100
0000101011101101111011100100110110001100100"""
b = ''.join(astring.splitlines())

bstring = """011100000110110001100101011000

010111001101100101001000000111

010001100001011011000110101100

100000011101000110111100100000

0110110101100101"""

cstring = """011011000110100101100110011001

010010000001110010011010010110

011101101000011101000010000001

101110011011110111011100100000

011010010111001100100000011011

000110111101101110011001010110

110001111001"""


def decode(b):
    b = ''.join(b.splitlines())
    output = ''
    for x in range(0, len(b), 8):
        c = b[x:x + 8]
        ans = int(c, 2)
        out =  chr(ans)
        output += out
    return output

if __name__ == '__main__':

    ans = decode(astring)
    print(ans)
    ans = decode(bstring)
    print(ans)
    ans = decode(cstring)
    print(ans)