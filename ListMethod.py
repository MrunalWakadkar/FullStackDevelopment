a= [2,4,6,8,3,6]
print(a)
print(len(a))
print(a.count(6))
b=a.copy()
print(b)
b.append(9)
print(b)
print(a)
a.clear()
print(a)
c=a.reverse()  #returns none 
print(c)
b.insert(2,6)
print(b)
b.pop(2)
print(b)
b.remove(6)
print(b)
print(a.index(4))
