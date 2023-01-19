'''
Write a function that, given a 4-digit number, returns the largest digit in that number.
Numbers between 0 and 999 are counted as 4-digit numbers with leading 0's.

largest_digit(1234) -> 4
largest_digit(3253) -> 5
largest_digit(9800) -> 9
largest_digit(3333) -> 3
largest_digit(120) -> 2

In the last example, given an input of 120, we treat it as the 4-digit number 0120.

Today's challenge is really more of a warmup for the bonuses. If you were able to
complete it, I highly recommend giving the bonuses a shot!
Bonus 1

Write a function that, given a 4-digit number, performs the "descending digits"
operation. This operation returns a number with the same 4 digits sorted
in descending order.

desc_digits(1234) -> 4321
desc_digits(3253) -> 5332
desc_digits(9800) -> 9800
desc_digits(3333) -> 3333
desc_digits(120) -> 2100

Bonus 2

Write a function that counts the number of iterations in Kaprekar's Routine,
which is as follows.

Given a 4-digit number that has at least two different digits, take that number's
descending digits, and subtract that number's ascending digits. For example,
given 6589, you should take 9865 - 5689, which is 4176. Repeat this process with
4176 and you'll get 7641 - 1467, which is 6174.

Once you get to 6174 you'll stay there if you repeat the process. In this case we
applied the process 2 times before reaching 6174, so our output for 6589 is 2.

kaprekar(6589) -> 2
kaprekar(5455) -> 5
kaprekar(6174) -> 0

Numbers like 3333 would immediately go to 0 under this routine, but since we require
at least two different digits in the input, all numbers will eventually reach 6174,
which is known as Kaprekar's Constant. Watch this video if you're still unclear on
how Kaprekar's Routine works.

What is the largest number of iterations for Kaprekar's Routine to reach 6174? That is,
what's the largest possible output for your kaprekar function, given a valid input? Post
the answer along with your solution.
'''

import random

def generate_number():
    while True:
        num = random.randrange(10000)
        str_num = str(num)
        if not str_num == len(str_num) * str_num[0]:
            return num


def large_digit(n):
    return 'Largest_digit (' + str(n) +') -> ' + max(list(str(n)))


def pad_out(n):
    n = str(n)
    n = n.zfill(4)
    return n


def descending_digits(n):
    N = pad_out(n)
    sorted_N = sorted(str(N), reverse=True)
    num = ''
    for digit in sorted_N:
        num += digit
    return num


def ascending_digits(n):
    asc_n = str((descending_digits(n))[::-1])
    return asc_n


def Kaprekars_routine(n):
    acc = 0
    N = pad_out(n)
    while True:
        N = int(descending_digits(N))
        A = int(ascending_digits(N))
        S = N - A
        acc += 1
        S = pad_out(S)
        N = S
        if N == '6174':
            return 'kaprecar(' + str(n) + ') -> ' + str(acc)

if __name__ == '__main__':
    num = generate_number()
    ans = large_digit(num)
    print(ans)
    ans = descending_digits(num)
    print('{0}{1}{2}{3}'.format('desc_digits(', num, ') -> ', ans))
    ans = Kaprekars_routine(num)
    print(ans)