# Think of data structures as containers : 
# A list is like a shopping list: ordered items. 
# dictionary is like a phone book: name and number combinations. 
# A tuple is like coordinates: fixed values. 
# A set is like a bag of unique items. 


"""
The main structures:
1. List: ordered, changeable collections
2. Dictionaries: key-value pairs for fast lookup. 
3. Tuples: ordered, unchangeable collections 
4. Sets: unique values only. 
"""

"""
Practice which one should be used and when, that is, in which cases : 
- Whenever we need some ordered list or ordered values, and the values might change in the future 
- We need to look up things faster, or data faster, by some specific keys. 
- We need ordered values which should not change in the future. 
- We only care about unique values. 

NOTE : Python follows 0-based indexing
"""


list = [1,2,3,4,5]
tuple = (1,2,3)
dict = {
    "first_name" : "rajat",
    "last_name" : "shahi",
    "age" : 26
}

set = {1,2,3,4,5,5,5,1}

print(list)
print(tuple)
print(dict)
print(set)


"""
Common things : 
- how to create 
- how to access
- how to make changes 
- how to update values if needed
- how to delete things 
- how to add things
- how to iterate through the values
- how to search something
- what common methods they have ?
"""