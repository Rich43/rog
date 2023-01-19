def max(num,num2):
            ''' (number) -> number
            return largest of two numbers
            '''
            largest = 0
            temp = 0
            if num > num2:
                    temp = num
            else:
                    temp = num2
            if temp > largest:
                    largest = temp
            return  largest

ans = max(-4,7)
print(ans)