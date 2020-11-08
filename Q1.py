# Age
'''	  
age = int(input('Enter the your age:'))

if age>=100:
    print("you are very old")
    
else:
    a = 100-age
    print('after {} years you will become 100yr old'.format(a))       

B_year = int(input('Enter the your B`year:')) 

if B_year>=200:
    print("First you have to born")

else:
    b = 2020-B_year
    print("'{}' years old are you.".format(b))       

'''

try:
    n = int(input('Enter the no. of apples:'))
    mn = int(input('Enter the minimum:'))
    mx = int(input('Enter the maximum:'))

except ValueError:
    print("Enter only Integer")
    

else:

    if mn>=mx:
        print("It should not be range")
    else:    
        for i in range(mn, mx+1):
            if n%i==0:
                print(f"{i} is divisible of {n}")
                
            else:
                print(f"{i} is not divisible of {n}")
             
                
            
        