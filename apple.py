# [80,48,82] == 144

# [7,40,77] == 80

n = 3
arr = [80,48,82]

d = {}

s = 0

temp = sorted(arr)


for i in range(n):
    index = arr.index(arr[i])
    
    for j in temp:
        if arr[index]<=j:
            s += arr[index] 
        
    
print(s)
