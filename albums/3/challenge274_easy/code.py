the_code = ''

with open('274_text.txt') as f:
    data = f.read()
    data = data.split()
    word_dict = dict(enumerate(data, start = 1))



print(word_dict)

with open('274_numbers.txt') as file:
    nums = file.read()
    nums = nums.split(',')
    for num in nums:
        # the trailing [0] grabs the first letter
        letter  = word_dict[int(num)][0]
        the_code = the_code + letter

print(the_code)