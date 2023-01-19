def check(line,n, title_lst):
            '''(list,index,list) -> bool
            checking for non-sentence-ending
            characters
            '''
            if line[n + 2].islower() and line[n + 2].isalpha():
                    return False
            elif line[n+1] == ' ' and line[n + 2] == line.isupper()\
                                                    and line[n + 2] == line.isalnum():
                    return True
            elif line[n+1].isalpha() or line[n+1].isnumeric():
                    return False
            elif line[n+1] == ' ' and (line[n-2:n] in title_lst\
                                                    or line[n-3:n] in title_lst):
                    return False
            elif  not ' ' in line[n-1:n+2]:
                    return False
            elif '.' in line[n+1] or ',' in line[n+1]:
                    return False
            else:
                    return True

def sentence_splitter():
            '''(file) -> str
            open and return a split text file
            '''
            line2 = ''
            line_starter = 0
            splitter = 0
            indexes = []
            title_lst = ['Mr', 'Mrs', 'Dr', 'Jr']
            f = open('sentence.txt','r' )
            for line in f:
                    chk_len = len(line)
                    # collect indexes of '.!?'
                    indexes = [n for (n,e) in enumerate(line) if e == '.']
                    indexes2 = [n for (n,e) in enumerate(line) if e == '?']
                    indexes3 = [n for (n,e) in enumerate(line) if e == '!']
                    indexes = indexes + indexes2 + indexes3
                    indexes = sorted(indexes)
                    print(indexes)

                    # select indexes one by one
                    for x in range(0, len(indexes)):
                            splitter = indexes[x]
                            if splitter == len(line)-1:
                                    line2 += line[line_starter + 1:splitter + 1].lstrip()
                                    print(line2)
                                    exit()
                            # Sort splitter index, return lowest index
                            truth = check(line,splitter,title_lst)

                            if truth:
                                    if line_starter == 0:
                                            line2 += line[line_starter:splitter + 1].strip() + '\n'
                                    else:
                                            line2 += line[line_starter + 1:splitter + 1].strip() + '\n'
                                    line_starter = splitter

                                    # end of sentence check
                                    len_line = len(line) - 1
                                    if splitter == len_line:
                                            line2 += line[line_starter+1:splitter + 1].strip() + '\n'
                                            print(line2)
                                            exit()
                            else:
                                    if line_starter == 0: # start of sentence
                                            line2 += line[line_starter:splitter + 1].lstrip()
                                            line_starter = splitter
                                    else:
                                            line2 += line[line_starter + 1:splitter + 1].lstrip()
                                            # start of slice
                                            line_starter = splitter


ans = sentence_splitter()
print(ans)