'''
We are given a list of numbers in a "short-hand" range notation where only the significant
part of the next number is written because we know the numbers are always increasing
(ex. "1,3,7,2,4,1" represents [1, 3, 7, 12, 14, 21]). Some people use different separators
for their ranges (ex. "1-3,1-2", "1:3,1:2", "1..3,1..2" represent the same numbers
[1, 2, 3, 11, 12]) and they sometimes specify a third digit for the range step
(ex. "1:5:2" represents [1, 3, 5]).

Input:

You'll be given strings in the "short-hand" range notation

"1,3,7,2,4,1"
"1-3,1-2"
"1:5:2"
"104-2"
"104..02"
"545,64:11"

Output:

You should output a string of all the numbers separated by a space

"1 3 7 12 14 21"
"1 2 3 11 12"
"1 3 5"
"104 105 106 107 108 109 110 111 112"
"104 105 106...200 201 202" # truncated for simplicity
"545 564 565 566...609 610 611" # truncated for simplicity

'''
import re


def condition_strings(l, n):
    candidates = l.splitlines()
    strng = candidates[n]
    lst = strng.strip('"')
    #lst2 = [int(x) for x in lst]
    return lst


def seperator(l, n):
    l = l.split(',')
    l2 = []
    for num in l:
        l2.append(int(num))
    lst2 = []
    test = 0
    acc = 0
    num2 = 0
    for num in l2:
        if num < test:
            acc += 1
            num2 = (num + (acc * n))
            lst2.append(num2)
            test = num
            continue
        test = num
        num2 = (num + (acc * n))
        lst2.append(num2)
    return lst2


def seperator2(l, n):
    l = l.split(',')
    l2 = []
    for num in l:
        l2.append(int(num))
    lst2 = []
    test = 0
    acc = 0
    num2 = 0
    for num in l2:
        if num < test:
            acc += 1
            num2 = (num + (acc * n))
            lst2.append(num2)
            test = num
            continue
        test = num
        num2 = (num + (acc * n))
        lst2.append(num2)
    return lst2


candidates = '''"1,3,7,2,4,1"
"1-3,1-2"
"1:5:2"
"104-2"
"104..02"
"545,64:11"'''


#----------- Part1 --------------------------

num_string = condition_strings(candidates, 0)
ans = seperator(num_string, 10)

print(ans)

#----------------- Part2 -------------------------------------

strng = condition_strings(candidates, 1)
lst = strng.split(',')
first_string = lst[0]
first_string = first_string.split('-')
second_string = lst[1]
second_string = second_string.split('-')
lst3 = []
for n in range(int(first_string[0]), int(first_string[1]) + 1):
    lst3.append(n)
for n in range(int(second_string[0]), int(second_string[1]) + 1):
    lst3.append(n)
lst4 = []
test = 0
acc = 0
num2 = 0
for num in lst3:
    num = int(num)
    if num < test:
        acc += 1
        num2 = (num + (acc * 10))
        lst4.append(num2)
        test = num
        continue
    test = num
    num2 = (num + (acc * 10))
    lst4.append(num2)

print(lst4)

#----------------Part3 --------------

strng = condition_strings(candidates, 2)
lst = strng.split(',')
first_string = lst[0]
first_string = first_string.split(':')
nums = []
output = ''
for i in first_string:
    nums.append(int(i))
for y in range(nums[0], nums[1] + 1, nums[2]):
    output += str(y) + ' '

print(output)

#------------ Part4 ------------

strng = condition_strings(candidates, 3)
first_string = strng.split('-')
list2string = ','.join(first_string)
out_list = seperator(list2string, 110)
output = []
for num in range(out_list[0], out_list[1] + 1):
    output.append(num)
print(output)

#-------------==part5 -------------------------
# 104 to 202
strng = condition_strings(candidates, 4)
first_string = strng.split('..')
list2string = ','.join(first_string)
end02 = '02'
output = []
for x in range(104, 1000):
    x = str(x)
    if x.endswith(end02):
        print(x)
        break

#--------------- Part6 -------------------------

strng = condition_strings(candidates, 5)
first_string = strng.split(':')
list2string = ':'.join(first_string)
endswith11 = list2string[-2:]
first_string = strng.split(':')
first_string = first_string[0]
new_num = int(first_string[0] + first_string[-2:])

for x in range(new_num, 1000):
    x = str(x)
    if x.endswith(endswith11):
        print(x)
        break