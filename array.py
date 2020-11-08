import math
def swap(a,b):
    temp = a
    a = b
    b = temp
    
    return a,b
arr = [2 ,3 ,4, 1, 5]
some = 0

m = 0
while(m<math.sqrt(len(arr))):
    print(m)
    for index,num in enumerate(arr):
        if num!=index+1:
            index = arr.index(num)
            print("index:",index)
            print("num-1:",num-1)
            arr[index] , arr[num-1] = swap(arr[index] , arr[num-1])
            some += 1
            
    m += 1    
print(arr , some)
   