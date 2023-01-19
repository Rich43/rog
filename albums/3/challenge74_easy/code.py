''' The Fibonacci numbers, which we are all familiar with, start like this:

0,1,1,2,3,5,8,13,21,34,...

Where each new number in the sequence is the sum of the previous two.

It turns out that by summing different Fibonacci numbers with each other,
you can create every single positive integer. In fact, a much stronger statement holds:

Every single positive integer can be represented in one and only one way as a sum of
non-consecutive Fibonacci numbers. This is called the number's "Zeckendorf representation".

For instance, the Zeckendorf representation of the number 100 is 89 + 8 + 3, and the Zeckendorf
representation of 1234 is 987 + 233 + 13 + 1. Note that all these numbers are Fibonacci numbers,
and that they are non-consecutive (i.e. no two numbers in a Zeckendorf representation can be
next to each other in the Fibonacci sequence).

There are other ways of summing Fibonacci numbers to get these numbers. For instance,
100 is also equal to 89 + 5 + 3 + 2 + 1, but 1, 2, 3, 5 are all consecutive Fibonacci numbers.
If no consecutive Fibonacci numbers are allowed, the representation is unique.

Finding the Zeckendorf representation is actually not very hard. Lets use the number 100 as an example of how it's done:

First, you find the largest fibonacci number less than or equal to 100. In this case that is 89.
This number will always be of the representation, so we remember that number and proceed recursively,
and figure out the representation of 100 - 89 = 11.

The largest Fibonacci number less than or equal to 11 is 8. We remember that number and proceed
recursively with 11 - 8 = 3.

3 is a Fibonacci number itself, so now we're done. The answer is 89 + 8 + 3.

Write a program that finds the Zeckendorf representation of different numbers.

What is the Zeckendorf representation of 3**15 ?
# 74
'''

def fib(num):
    acc = 0
    lst = [0, 1]
    while acc < num:
        acc = lst[-2] + lst[-1]
        lst.append(acc)
    return lst

def zec(num):
    lst = fib(num)
    lst2 = []
    # for consecutive test
    temp = len(lst) + 1
    while num >= 1:
        # work down the list
        for x in range(len(lst) -1, -1, -1):
            # consecutive test
            if temp - x > 1:
                if lst[x] <= num:
                    num -= lst[x]
                    lst2.append(lst[x])
                    temp = x


    return lst2


if __name__ == '__main__':

    ans = zec(3 ** 15)
    print(ans)