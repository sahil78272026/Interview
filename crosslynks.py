# HR, Monika- 7209412355, date: 01-Aug-2023, 4PM


# explain the project
# caching mechanism
# mixins
# inheritence
# authentication
# JWT
# difference between make migrations and migrate

# selection sort
# binary search,

n=1

list1 = [2,3,6,1,7,5,8]

for i in range(len(list1)):
    for j in range(i+1,len(list1)):
        if list1[i]>list1[j]:
            list1[i],list1[j] = list1[j],list1[i]

print(list1)


# [1, 2, 3, 5, 6, 7, 8]
def findNum(n):
        # n=1
        l,r = 0, len(list1)-1

        while l <= r:

            mid = (l+r)//2 # 3,  second iter   l=0, r=2, mid=1  , third iter, l=0, r=0, mid=0
            if n == list1[mid]:
                return list1[mid]

            if n > list1[mid]:
                l = mid+1

            if n < list1[mid]:
                r = mid-1


print(findNum(n))