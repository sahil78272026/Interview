""""
Reverse a string without changing the position of special characters.
Eg:- abc.efg@pqr.comn
Result will be nmo.crq@pgf.ecba

abc!efg@pqr.comn
output:- nmo!crq@pgf.ecba

"""
str1 = 'abc.efg@pqr.comn'

splitStr = str1.split(".")
print(splitStr)

newStr = splitStr[1].split("@")
print(newStr)


"""
Get the longest subsequence  string present in 2 given strings.
eg:- string1 = abcde
 string2 = acef

Output:- "ace" length = 3
"""

"""
string1 = abcde
string2 = aecf

ae
"""

string1 = 'aabcde'
string2 = 'acef'

newSet = set()

newStr = ''
for ch in string1:
    if ch in string2:
        newSet.add(ch)

for ch in newSet:
    newStr+=ch

print(newSet)
print(newStr)





