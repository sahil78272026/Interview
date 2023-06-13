# 08-May-2023, Monday

"""varname = 'Sahil123 garg!'

vowels = 'aeiou'
# remainingChar = 'bcdfghjklmnpqrstvwxyz'
vowelList = []
constList = []

def vowelCount(name):
    strg = name.replace(' ','')
    for ch in strg:
        if ch in vowels:
            vowelList.append(ch)
        else:
            if not ch.isdigit():
             constList.append(ch)
    print(len(vowelList))
    print(len(constList))


vowelCount(varname)


"""



# factorial

# 5 = 5*4*3*2*1

result = 0
def fact(num):
    if num==1 or num==0:
        return 1

    else:
         return num*fact(num-1)

print(fact(3))

dict = {1:"anil",True:"Aera",1.0:"Sahil"}
print(dict)
# output = {1:"anil",True:"Aera",1.0:"Sahil"}

list1 = [[1]]*3
# output = [[1],[1],[1]]
print(list1)


# output = [10,[1],[1]]
print(list1)

var1 = "Sahil"
print(var1[-1:-3])
# output : li

print(var1[:3])
# Sah


# why we use generators?
# what datastructure used in recursion?
