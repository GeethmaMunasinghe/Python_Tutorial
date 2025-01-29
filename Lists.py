x=[12,434,565,77]

x.append(100)
x.insert(2,500)

print(x)

x.remove(12)
x.pop(2)
print(x)

print("Adding two lists....")

y=[0,10,20,30,40]
z=x+y
print(z)

print("Searching a number....")

a= 10 in z
print(a)

b=10 not in z
print(b)

