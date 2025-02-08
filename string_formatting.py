
name="Geethma"
height=154

message="Hello "+name+". Your height is "+str(height)

message="Hello %s. Your height is %d." %(name,height)

message="Hello {0}. Your height is {1:05d}".format(name,height)

message=f"Hello {name}, Your height is {height:05d}"

print(message)