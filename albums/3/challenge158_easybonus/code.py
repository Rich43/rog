'''
I had the other day in my possession a label bearing the number 3 0 2 5 in large figures.
This got accidentally torn in half, so that 3 0 was on one piece and 2 5 on the other.
On looking at these pieces I began to make a calculation, when I discovered this
little peculiarity. If we add the 3 0 and the 2 5 together and square the sum we get as the result,
the complete original number on the label! Thus, 30 added to 25 is 55, and 55 multiplied by 55 is 3025.
Curious, is it not?

Now, the challenge is to find another number, composed of four figures, all different, which may be
divided in the middle and produce the same result.
Bonus

Create a program that verifies if a number is a valid torn number.
'''

def uniq(input):
    ''' Check for duplicate digits. '''
    output = []
    for x in input:
        if x not in output:
            output.append(x)
    return output


def torn_check(num):
    ''' Torn number check. '''
    num = str(num)
    # reject a number with odd length
    if len(num) % 2 == 1:
        return False
    # duplicate digit check
    lst = uniq(num)
    if len(lst) < len(num):
        return False
    # the math
    half_len_num = int(len(num) / 2)
    x = int(num[:half_len_num])
    y = int(num[half_len_num:])
    sum_xy = x + y
    if sum_xy ** 2 == int(num):
        return True
    return False

if __name__ == '__main__':

    test = input('Input number for testing: ')
    result = torn_check(test)
    print(result)