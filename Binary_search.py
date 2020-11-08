def Binary_Search(l,key):
    found = False
    start = 0
    End = len(l)-1  
    while(start<=End and not found):
        mid = len(l)//2
        if (key == l[mid]):
            found = True
        else:
            if key<l[mid]:
                End = mid-1
            else:
                Start = mid+1
                
    if(found == True):
        return ("Key is present.")
    else:
        return ("Key is Not Present.")
        
list = []
n = int(input('How namy number want to Enter:'))
for i in range(n):
    data = int(input('Enter list itoms:'))
    list.append(data)
    
list.sort()    
key = int(input('Enter the key:'))
Binary_Search(list,key)