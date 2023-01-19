target_list = ['here', 'there', 'and', 'everywhere']
def mapping(lst):
            '''(list) -> list
            return a list of word lengths
            '''
            output = []
            for word in lst:
                    output.append(len(word))
            return output

ans = mapping(target_list)
print(ans)

ans =list(map((lambda x: len(x)), target_list))
print(ans)

ans = [len(x) for x in target_list]
print(ans)