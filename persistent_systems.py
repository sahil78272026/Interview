# remove nesting in a list

sample_list = [1, [2, 3, [4, 5, [6, 7], 8], [9, 10], 11], 12, [13, [14], 15]]

sample_list = [1,[2,3]]

def recur(sample_list):
    newList = []
    print(newList)
    for i in sample_list:
        if not type(i)==list:
            print(i)
            newList.append(i)
        else:
            print(i)
            newList.extend(recur(i))
    
    return newList


print(recur(sample_list))


# context managers
# authentication system
# dunder methods