
def printLeaders(arr,size): 
      
    for i in range(0, size): 
        for j in range(i+1, size):
            print('j in inner loop: ',j) 
            if arr[i]<=arr[j]: 
                print(f'break arr[i]:{arr[i]}, arr[j]:{arr[j]} ')
                break
        print('j after inner loop:', j)
        if j == size-1: # If loop didn't break 
            print ('leader: ',arr[i],end=' ') 
  
# Driver function 
arr=[16, 17, 4, 3, 4, 5, 4, 2] 
printLeaders(arr, len(arr)) 
  