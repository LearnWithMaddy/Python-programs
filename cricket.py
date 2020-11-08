def function(striker, Non_striker , scores , balls):
    s = []
    for i in scores:
        if i!='w':
            s.append(int(i))
        else:
            s.append(i)

    for i in s:    
        if i==1 or i==3:
            striker += i
            temp = striker
            striker = Non_striker
            Non_striker = temp
        
        if i==2 or i==4 or i==6:
            striker += i
            
        if i=="w":
            striker = 0
        
        balls += 1 
        if balls%6==0:
            temp = striker
            striker = Non_striker
            Non_striker = temp
        
    return striker , Non_striker
            
        
RR1 = float(input("Enter:"))
striker , Non_striker = map(int , input().split())

scores = list(input("Enter:").split())

b = len(scores)
r = 0
for i in scores:
    if i!="w":
        r += int(i)
        
RR2 = float(input("Enter:"))

numerator = (RR1 * ( (6*r) - (RR2*b) ) )
denominator = ((RR2*6) - (6*RR1))

R1 = numerator/denominator

B1 = int((6*R1)//RR1)

final_score = int(R1+r)

p1 , p2 = function(striker , Non_striker , scores , int(B1))

print(final_score,p1,p2)