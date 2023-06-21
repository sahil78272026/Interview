# 1 to 100 , even number


# list1 =  [i for i in range(0,101) if i%2==0]


'''
a = [1,2,3]
b = [4,5,6]
c = [7,8,9]

 

final_op = [(1,4,7), (2,5,8), (3,6,9)]
'''

a = [1,2,3]
b = [4,5,6]
c = [7,8,9]

tup1 = []
list1 = list(tup1)
print(type(list1))
for i in range(len(a)):
    tup1.append(a[i])
    tup1.append(b[i])
    tup1.append(c[i])
    list1.append(tup1)
    tup1 = []
    

    
print(list1)


