
#find min and max number of given numbers set

x=[12,23,567,123,88]

max=x[0]
min=x[0]

for i in x:
    if max<i:
        max=i
    if min>i:
        min=i

print("Maximum number is: ",max)
print("Minimum number is: ",min)