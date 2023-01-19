def largest_of_three(a, b, c):
            ''' (number) -> number
            return the largest of a, b, c
            '''
            largest = 0
            if (a > b) and (a > c):
                    largest = a
            elif (b > a) and (b > c):
                    largest = b
            else:
                    largest = c
            return largest

ans = largest_of_three(-4, 4, 7)
print(ans)