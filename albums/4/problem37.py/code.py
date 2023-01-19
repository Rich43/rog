'''Write a program that given a text file will create a new text file
    in which all the lines from the original file are numbered
    1 to n (where n is the number of lines in the file'''


file1 = open('words.txt')
lst = []
for line in file1:
            line = line.strip('\n')
            lst.append(line)

#number the list which creates a tuple
lst = list(enumerate(lst))

#clean up for presentation and write to txt file
file2 = open('numbered_lines.txt', 'w')
for tuple in lst:
            tuple = str(tuple)
            tuple = tuple.strip('()')
            tuple = tuple.strip("'")
            num = tuple.find(' ')
            print(tuple,num)
            first = tuple[:num + 1]
            second = tuple[num + 2:]
            print(first, second)
            tuple = first + second
            file2.write(tuple +'\n')

# 37a
'''One liner from the much smarter and more Pythonic son Richard'''

open('richwords.txt', "w").writelines([", ".join([str(x), str(y)]) for\
    x, y in enumerate(open('words.txt').readlines())])