

def my_form(**params):
    if 'name' not in params:
        print("Error")
    else:
        print("Hello",params['name'])

my_form(height=154,city="Anuradhapura")
my_form(name="Geethma",height=154)