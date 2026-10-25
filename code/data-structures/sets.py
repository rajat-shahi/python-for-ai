# unique elements in a bag
# it's a collection that stores only unique elements, automatically remove duplicates
# it's unordered, because it keeps it sorted

empty_set = set() # can't use {} - it's a dict

# for set with values both works
numbers = {1,2,3,4,5,5}
print(numbers)

even_nums = set([2,2,2,4,6,8])
print(even_nums)


# add values 
colors = {"red","yellow"}
colors.add("green")

# remove values
colors.remove("yellow")
colors.discard("red")



"""
Common uses : 
- remove duplicates 
- fast membership testing
"""

names = ["aman","rajat","shreya","aman"]
unique_names = list(set(names))
print(unique_names)

allowed_users = set(names.copy())
print(allowed_users)

if "aman" in allowed_users:
    print("Access Granted")

allowed_users.discard("aman")

if "aman" in allowed_users:
    print("Access Granted")
else:
    print("Not Found")


"""
COMMON MISTAKES : 
- empty set syntax
- sets are unordered, use lists if order matters
"""

nums_set = {11,1,2,3,4,5,5,6}
nums_list = [11,1,2,3,4,5,6]
nums_list = list(set(nums_list))
print(nums_set)
print(nums_list)