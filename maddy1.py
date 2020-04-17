
'''
#binary search
def Binary_Search(l,key):
    found = False
    start = 0
    End = len(l)-1
    mid = len(l)//2
    while(start<=End and not found):
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
'''
'''
# Pattern : 1

for row in range(7):
    for col in range(5):
        if ((col== 4 or col== 0 ) and (row!=0)) or ((row==0 or row==3) and (col>0 and col<=3)):

            print('*', end = '')
        else:
            print(end=" ")
            
            
    print()
        
Output:

        ***
       *   *
       *   *
       *****
       *   *
       *   *    
'''

'''
#Pattern : 2

for row in range(7):
    for col in range(5):
        if (row%3==0) or (row%3!=0) and (col==0 or col==4):
            print('*',end='')
        else:
            print(end=' ')

    print()

*****
*   *
*   *
*****   
*   *
*   *
*****
'''

#multiplication of complex number     
'''
def complex_mul(x,y):
    real = (x.real*y.real-x.imag*y.imag)
    imag = (y.real*x.imag+x.real+y.imag)
    return complex(real,imag)
    
x = complex(input('Enter the First complex number(x+yj):'))
y = complex(input('Enter the Second complex number(x+yj):'))

multiplication = complex_mul(x,y)
print(multiplication)
'''

#addition and substraction of matrix:
'''
row = int(input("Enter the of row:"))
col = int(input("Enter the of Column:"))

print("Enter the matrix 1:")
matrix1 = [[int(input()) for i in range(col)] for j in range(row)]
print("matrix 1:")
for i in range(row):
    for j in range(col):
        print(format(matrix1[i][j],"<3"),end="")
    print()


print("Enter the matrix 2:")
matrix2 = [[int(input()) for i in range(col)] for j in range(row)]
print("matrix 2:")
for i in range(row):
    for j in range(col):
        print(format(matrix2[i][j],"<3"),end="")
    print()

result = [[0 for i in range(col)] for j in range(row)]
for i in range(row):
    for j in range(col):
        result[i][j] = matrix1[i][j] + matrix2[i][j]

print("Addition:")
for i in range(row):
    for j in range(col):
        print(format(result[i][j],"<3"),end="")
    print()         

'''
'''
def factorial(num):
    if num==0 or num==1:
        return 1
    else:
        return num*factorial(num-1)

def fact_tailing_to_Zero(number):
    count = 0
    i = 5
    
    while(number//i!=0):
        count += int(number/i)
        i = i*5
    
    return count
    
    
    
number = int(input("Enter the number:"))
fac = factorial(number)
print(f"factorial :{fac}")

print(f"Count of Zeroes:{fact_tailing_to_Zero(number)}")

'''

'''
with open('data.txt') as f:
    lines = f.readlines()
 
currency_dict = {} 
for line in lines:
    parsed = line.split('\t')
    currency_dict[parsed[0]] = parsed[1]
    
amount = int(input("Enter the amount:"))

[print(currencies) for currencies in currency_dict.keys()]


print("\nChoose in which currency do you want to convert your amount.\n")

currency = input(":")

print(f"{amount} in INR is {amount * float(currency_dict[currency])} in {currency}.")

'''
    
    

    
    
    

