# date: 11-Aug-2023, HR Ankita:

# select related, pre-fetch related
# query optimization in django
# Q in django
# what is lazy loading
# atomic query in django
# generators



# foo = [[1,2],5,[6,7,8,[11,12,13]],30]

# # Expected:- foo = [1,2,5,6,7,8,11,12,13,30]


# newList = []
# def nestedList(foo):
#     newList = []
#     for i in foo:
#         if isinstance(i,list):
#             newList.extend(nestedList(i))
#         else:
#             # print(i)
#             newList.append(i)


#     return newList
# print(nestedList(foo))


# # print(newList)



# Ques:- Write a function to find the longest common prefix string amongst an array of strings. If there is no common prefix, return an empty string "".



# Input:

strs = ["flower","flow","flight"]

# Output: "fl"

# Input: strs = ["dog","racecar","car"]

# Output: ""


def commonPrefix(strs):
    prefix = ""
    for i in range(len(strs)):
        for j in range(len(strs[i])):
            print(strs[i])
            prefix = strs[i][j]
            print(strs[i][j])
            if strs[i+1][j] != prefix:
                return ""
            else:
                prefix += strs[i+1]

    return prefix

print(commonPrefix(strs))








