from functools import reduce
def find_longest_word(lst):
            '''(list( -> str
            return longest word in the list
            using high order functions
            '''
            f = lambda a,b: a if (len(a) > len(b)) else b
            max_word = reduce(f, lst)
            return max_word

word_list = ['one', 'four', 'seventeen', 'twenty']
ans = find_longest_word(word_list)
print(ans)