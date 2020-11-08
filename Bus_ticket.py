#Get Data from txt file
'''
def Ticket(l):
	T = []
	for i in l:
		for j in l:
			if i!=j:
				T.append(( i , j))
	return T

num_lines = 0
f = open("City.txt","r")
lines = f.readlines()

Tickets = Ticket(lines)	

for i in Tickets:
	source = i[0]
	destination = i[1]
	print("happy journey.")
	print(f"From {source}To {destination}")
'''

#Get Data from User
'''
def Ticket(l):
	T = []
	for i in l:
		for j in l:
			if i!=j:
				T.append(( i , j))
	return T

n = int(input('Enter the how many stops: '))
l = []
for i in range(n):		  
	temp = input(f'Enter the Stop-{i+1} : ')
	l.append(temp)

Tickets = Ticket(l)	

for i in Tickets:
	source = i[0]
	destination = i[1]
	print(f"From {source} To {destination}")
	print("happy journey.\n")
'''	