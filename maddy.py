
'''
import pandas as pd

x = 1 
y = 3 
a = list(bin(x))
d = list(bin(y))

b = a[2:]
e = d[2:]

print(b,e)

c = pd.DataFrame([b])
c = c.append(pd.DataFrame([e]))
#print(c)

p = c.iloc[:,0]

import time

p = time.asctime(time.localtime(time.time()))
print(p)

'''

#Write a program to identify if the character is a vowel or consonant 
'''
ch =input('Enter the character:')

if(ch=='a' or ch=='e' or ch=='i' or ch=='o' or ch=='    u'):
    print("It's a Vowel")
else:
    print("It's a constant")
    
'''

#Write a program to identify if the character is an alphabet or not 
#a=97, z=122, A=65, Z=90 
'''
n = input('Enter the alphabet:')

if((ord(n)<=90 and ord(n)>=65) or (ord(n)<=122 and ord(n)>=97)):
    print("It's a alphabet.")
    
else:
    print("It's not a alphabet.")
'''
#Write a program to find ASCII values of a character 
'''
n = input('Enter the alphabet:')
print(ord(n))
'''
#Write a program to find Number of digits in an integer
'''
n =int(input("Enter the number:"))
count = 0 
while (n>0):
    count+=1
    n = n//10
print(f"count is {count}")
'''

#Write a program to find Factorial of a number 
#n = 5
#120 = 5*4*3*2*1
'''
n = int(input('Enter the number :'))
fact = 1
if(n<0):
    print("factorial should not be possible")
    
elif(n==0):
    print("factorial of 0 is 1.")
for i in range(1,n+1):
    fact = fact*i 

print(f"factorial of {n} is {fact}.")

'''

#Write a program to find Fibonacci series up to n       1  1 2
'''
n = int(input('Enter the how many numbers :'))
prev = 0
next = 1
list = [0,1]
while len(list)<n:
    sum = prev + next
    prev = next
    next = sum
    list.append(sum)    
print(list)    
'''

#Write a program to identify of the a number is positive or negative
'''
num = int(input('Enter the number :'))
if num >= 0:
   if num == 0:
       print("Zero")
   else:
       print("Positive number")
else:
   print("Negative number")
'''

#Write a program to find Sum of N natural numbers 
'''
N = int(input('Enter the number :'))
sum = 0
for i in range(N+1):
    sum += i
    
print('sum :',sum)
'''
#Write a program to find Sum of numbers in a given range 
'''
start = int(input())
end = int(input())
sum = 0
for i in range(start, end + 1, 1):
    sum = sum + i
print(sum)
'''


#Write a program to reverse a given number 
'''
Number = int(input("Please Enter any Number: "))
Reverse = 0
while(Number > 0):
    Reminder = Number%10
    Reverse = (Reverse *10) + Reminder
    Number = Number//10
print("\n Reverse of entered number is = %d" %Reverse)
'''

#Write a program to find LCM of two numbers 
'''
x = int(input('Enter the first number:'))
y = int(input('Enter the second:'))
   # choose the greater number
if x>y:
    greater = x
else:
    greater = y

while(True):
    if((greater % x == 0) and (greater % y == 0)):
        lcm = greater
        break
    greater += 1

print("The L.C.M. is",lcm)
'''

#Python Program to find Strong Number
'''
Number = int(input("Enter any Number: "))
Sum = 0
Temp = Number

while(Temp > 0):
    Factorial = 1
    i = 1
    Reminder = Temp % 10

    while(i <= Reminder):
        Factorial = Factorial * i
        i = i + 1

    print("\n Factorial of %d = %d" %(Reminder, Factorial))
    Sum = Sum + Factorial
    Temp = Temp // 10

print("\n Sum of Factorials of a Given Number %d = %d" %(Number, Sum))
    
if (Sum == Number):
    print(" %d is a Strong Number" %Number)
else:
    print(" %d is not a Strong Number" %Number)
    
'''

#Write a program to identify if the number is Perfect number or not 
'''
n = int(input('Enter the Number:'))
sum = 0
for i in range(1,n,1):
    if n%i==0:
        sum+=i
    
if sum==n:
    print('Number is perfect.')
    
else:
    print('Number is not perfect.')

'''
#find the power of the number
'''
number = int(input(" Please Enter any Positive Integer : "))
exponent = int(input(" Please Enter Exponent Value : "))
power = 1

for i in range(1, exponent + 1):
    power = power * number
    
print("The Result of {0} Power {1} = {2}".format(number, exponent, power))
'''

#Write a program to find the Factors of a number
'''
n = int(input("Enter the number:"))

list = []

for i in range(1,n+1,1):
    if n%i==0:
        list.append(i)
        
print(list)
'''

#Write a program to find HCF
'''
x = int(input("Enter the First number:")) 
y = int(input("Enter the Second number:")) 

if x>y:
    small = y
else:
    small = x
    
for i in range(1,small+1):
    if(x%i==0 and y%i==0):
        hcf = i
        
    
print('HCF is :',hcf)   
'''

#Write a program to identify if the number is Armstrong number or not 
'''
n = int(input('Enter the number:'))
num = n
sum = 0

while n!=0:
    rem = n%10
    sum +=rem**3
    n = n//10

if(sum==num):
    print('Number is Armstrong.')
else:        
    print('Number is Not Armstrong.')
'''

#Write a program to identify if the number is Palindrome or not  
'''
n=int(input("Enter number:"))
temp=n
rev=0
while(n>0):
    dig=n%10
    rev=rev*10+dig
    n=n//10
if(temp==rev):
    print("The number is palindrome")
else:
    print("The number not palindrome")
    
'''

#Write a program to Replace all 0’s with 1 in a given integer 
'''    
def replace(number):

    if (number == 0):

        return 0;

    digit = number % 10

    if (digit == 0):

        digit = 1

    return replace(int(number/10)) * 10 + digit

number = int(input("Enter the number : "))

print("Number after replacement : ",replace(number))
    
'''


    
