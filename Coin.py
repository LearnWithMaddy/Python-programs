amount = int(input("Enter:"))
five=0
if amount>5:
	five = (amount//5)-1
	amount -= five*5

if amount%2==0:
	one = 2
	amount -= one

else:
	one = 1
	amount -= one

two = amount//2

d = {}
d["five"] = five
d["two"] = two
d["one"] = one

print(one+two+five)
