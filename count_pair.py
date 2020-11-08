import time

n = 5
k = 3

l = [5,5,7,9,15,2]
d = {}

start = time.time()
for x_index in range(len(l)):
    end = l[x_index]+k
    start = l[x_index]-k
    #print((start , end))
    
    for i in range(len(l)):
        if l[i]>=start and l[i]<=end:
            if i!=x_index:
                d[l[i]]=True
s = set(l)
l = len(l)-len(s)

print(len(d)+l)
