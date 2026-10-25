# immutable ordered values 


"""
CREATE 
"""
empty_tuple = ()
single_tuple = (12,) # not (12)
colors = ("green","red","blue","yellow")
coordinates = 2.14,17.23
print(coordinates)



"""
ACCESS 
"""
lat = coordinates[0]
long = coordinates[1]
print(f"latitude : {lat}, longitude : {long}")

# slicing works here as well 
print(colors[1:3])



"""
TUPLE UNPACKING
"""
point = (3,14)
x,y = point
print(x,y)

y,x = x,y
print(x,y)

first_color, second_color , *_ = colors
print(first_color,second_color,*_)


"""
COMMON MISTAKES : 
- forgetting comma in the single tuple (12,) 
    - else treated like integer with parentheses

- Trying to modify tuples 
    - either reassign new values to the variable 
    - or convert to list, change and then change to tuple again
"""

point = (1,5)
point = (2,point[1])
print(point)


colors = list(colors)
print(colors)
print(type(colors))
colors.append("maroon")
colors = tuple(colors)
print(colors)