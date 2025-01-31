x={"Hello","World","1","2","3"}
y={"1","2","7"}

z=x-y
print(z)
print("1" in y)

x.add("world")
x.add("World")
print(x)

#remove
x.remove("world")
print(x)

#Adding two sets
a=x.union(y)
b=x|y
print(a)
print(b)

