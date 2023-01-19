'''
[2016-12-12] Challenge #295 [Easy] Letter by letter
Description

Change the a sentence to another sentence, letter by letter.

The sentences will always have the same length.
Formal Inputs & Outputs
Input description

2 lines with the source and the target
Input 1

floor
brake

Input 2

wood
book

Input 3

a fall to the floor
braking the door in
'''


def the_change(a, b):
    '''str, str -> str
       Change the sentence as required '''

    duplicate_check = set()
    answer = ''
    answer += a + '\n'
    for x in range(len(a)):
        temp = a[:x] + b[x] + a[x + 1:]
        if temp in duplicate_check:
            continue
        duplicate_check.add(temp)
        a = temp
        answer += temp + '\n'
    return answer


if __name__ == '__main__':
    candidates = '''floor
    brake
    wood
    book
    a fall to the floor
    braking the door in'''
    candidate_list = candidates.splitlines()
    # select in pairs
    for n in range(0, len(candidate_list), 2):
        # select the 2 sentences to manipulate
        first = candidate_list[n].lstrip()
        second = candidate_list[n + 1].lstrip()
        # the function for manipulation
        ans = the_change(first, second)
        print(ans)