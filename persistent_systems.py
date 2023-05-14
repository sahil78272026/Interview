# remove nesting in a list

sample_list = [1, [2, 3, [4, 5, [6, 7], 8], [9, 10], 11], 12, [13, [14], 15]]

# lis = [1,[2,3]]

def recur(sample_list):
    newList = []
    for i in sample_list:
        if not type(i)==list:
            newList.append(i)
        else:
            newList.extend(recur(i))
    
    return newList


print(recur(sample_list))


# context managers
# authentication system
# dunder methods