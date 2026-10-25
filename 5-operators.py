# In this we can explore different types of operators in python


# Arithmetic Operators 

"""
=> + , - , / , * , // , % , **
=> Python follows maths rules (PEMDAS)
=> PEMDAS = parantheses, exponentiation, multiplication, division, addition, subtraction 
"""



# Comparison Operators

"""
=> == , != , > , >= , < , <= 
"""


# Logical Operators
"""
- and
- or
- not
"""

age = 25
has_license = True

car_drive = age >= 16 and has_license
print(car_drive)


day = "Saturday"
is_weekend = day == "Saturday" or day == "Sunday"
print(is_weekend)


is_adult = age >= 18
is_child = not is_adult
print(is_child)


# shortcut assignment 
score = 10
score = score + 10 
score += 5
