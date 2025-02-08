
file=open("data.txt",'w')

x=[str(i) for i in range(0,10)]
msg=', '.join(x)
file.write(msg)
file.close()