'''
'r'=read only
'w'=write only
'x'=open for exclusive creation
'a'=append
'b'=binary
't'=text mode
'+'=updating
'''

with open("data.txt",'a') as file:
    x=[str(i*2)for i in range(0,10)]
    msg='\n'.join(x)
    file.write(msg)