'''
This challenge comes to us from user skeeto

Write a program to count the number years in an inclusive
range of years that have no repeated digits.

For example, 2012 has a repeated digit (2) while 2013 does not.
Given the range [1980, 1987], your program would return 7
(1980, 1982, 1983, 1984, 1985, 1986, 1987).

Bonus: Compute the longest run of years of repeated digits
and the longest run of years of non-repeated digits for [1000, 2013].

'''

def no_repeat(n, n2):
    accum = 0
    sett = set()
    for x in range(n, n2 + 1):
        x = str(x)
        for digit in x:
            sett.add(int(digit))
        if len(str(n)) == len(sett):
            accum += 1
            sett = set()
    return accum


if __name__ == '__main__':
    num = 1980
    num2 = 1987
    ans = no_repeat(num, num2)
    print(ans)