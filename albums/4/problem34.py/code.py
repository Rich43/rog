# requires a text file

def char_freq_table():
            '''(text file) -> histogram
            generate a histogram based on a text file
            '''
            store = ''
            dict = {}
            input_text = input('Enter a text file: ')
            file = open(input_text, 'r')
            for line in file:
                    line = line.strip()
                    for letter in line:
                            if letter.isalpha():
                                    store += letter

            for letter in store:
                    counter = store.count(letter)
                    dict[letter] = counter
                    store.replace(letter, '')

            for entry in dict:
                    yield(entry, 'x' * dict[entry])

for x in char_freq_table():
        print(x)