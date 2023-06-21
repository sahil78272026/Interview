list1 = [10,25,3,9,75,6,863,57]

list1.sort()


# [1, 2, 3, 4, 4, 5, 6, 57, 863]


finalList=[]
for i in range(len(list1)//2):
    finalList.append(list1[i])
    finalList.append(list1[-i-1])


print(finalList)



"""def decorator(func,*args,**kwargs):
    def wrapper_func():
        print(args)
        print("In wrapper Func")
        func()
        return func
    return wrapper_func

def div(num,denom):
    newNum = num/denom
    print("In Sum")


    
"""

filepath = 'D:\\pwd.txt'
with open(filepath,'r') as f:  # context manager
    file_data = f.read()
    print(file_data)



