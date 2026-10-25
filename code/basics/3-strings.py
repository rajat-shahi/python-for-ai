# strings are text - any character inside quotes

"""
- we can store texts 
- we can manipulate it 
- we can perform operations on it
"""

first_name = "Rajat"
last_name = 'Shahi'

string = "My name is Rajat Shahi"

long_string = """
My first name is Rajat.
My last name is Shahi. 
I am learning python
"""

full_name = first_name + " " + last_name
long_dash = "-" * 30

print(full_name)
print(long_dash)

full_name_length = len(full_name)
