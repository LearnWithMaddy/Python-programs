import time
start = time.time()
q = "({{[()()())(()())][{}[]{}{}[]{}[]][{}{}{}{}{}{}][()()()()]}})"

paren1 = ["(" , "{" , "["]
paren2 = [")" , "}" , "]"]
sol = [('(',')') , ('[',']') , ('{','}')]

l = []
#For opening parenthesis
for i in paren1:
    for s in q:
        if i==s:
            l.append(i)
#print(l)
a = []
#For closing parenthesis
for i in paren2:
    for s in q:
        if i==s:
            a.append(i)
#print(a)
for i in zip(l,a):
    if i not in sol:
        key = False
        break
    else:    
        key = True
print(key)
end = time.time()
print(end-start)












