dict = {}
while True:
    print("1.To get the birthdate.")
    print("2.Add the Birthdate.")
    print("3.Exit")
    choice = int(input('Enter the choice:'))
    if(choice==1):
        if (len(dict.keys())!=0):
            name = input("Enter the name:")
            birthday = dict.get(name,"No data found")
            print(f"{name}'s Birthdate is {birthday}.")
        else:
            print("Nothong to show.")
             
    elif(choice==2):
        name = input("Enter the name:")
        date = input("Enter the Bdate:")
        dict[name]=date
    
    elif(choice==3):
        break
        
    else:
        print("Enter the right choice.")