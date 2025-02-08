
def get_odd_numbers(upper_limit):
    for i in range(0,upper_limit):
        if i%2 ==1:
            print("Odd",i)
            yield i
print("Starting")
x=get_odd_numbers(10)
print("Finished")

for i in x:
    print("Loop",i)

print("*" * 20)

x=get_odd_numbers(10)

for i in x:
    print("Loop",i)

print(x)