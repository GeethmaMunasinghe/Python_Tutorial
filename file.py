#read file line by line

print("Reading file line by line")
file=open("data.txt")

for i,line in enumerate(file):
    print("Line-->",i,line)
file.close()



