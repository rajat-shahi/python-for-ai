# creating lists

my_list = [] #empty list
fruits = ["apple","banana","orange"] #list with items
numbers = [1,2,3,4,5]
mixed_list = ["rajat",14,True,3.14]


"""
Accessing items : 
- get items 
- slicing items (you get the sliced values)
"""

print(fruits[0])
print(fruits[len(fruits)-1])
print(fruits[-1])
print(fruits[-(len(fruits))])

print(fruits[0:2])
print(fruits[1:])


"""
Changing Lists : 
- change an item directly
- add item at last
- remove from last (it gives value as well)
- add item at any position
- remove item from any position 
"""

fruits[0] = "mango"
print(fruits)

fruits.append("kiwi")
print(fruits)
last_item = fruits.pop()
print(last_item, fruits)

fruits.insert(0,"kiwi")
print(fruits)

fruits.insert(2,"Grapes")
print(fruits)

del fruits[2:5]
print(fruits)


"""
List methods : 
- sort
- reverse
- length
- create a copy
- count occurences
- find the position
"""

numbers = [1,2,3,4,5,1,6,1,3,5,11,1]
print(len(numbers))
print(numbers.count(1))
print(numbers.index(5))

numbers.sort()
print(numbers)

numbers.reverse()
print(numbers)

new_list = numbers.copy()
print(new_list)


"""
Checking list : 
- checking if a value exists in list or not
- list is empty or not
"""
print(fruits)
if "apple" in fruits:
    print("Found Apples")
else:
    print("Apples not found")

if fruits:
    print("List has items")
else:
    print("List is empty")


"""
Common mistakes : 
- Index out of range (check length first)
- modifying while looping 
- shallow copy issues
"""


nums = [1,2,3,4,5,6,7,8,9]
# return the even numbers except 2

even_nums = [num for num in nums if num!=2 and num%2==0]
print(even_nums)



"""
- shallow copy : original and copied both reference the same object in memory. 
- deep copy : original copy: both reference the different objects in memory. 
"""

nums_new = nums #shallow copy
nums_new.append(11)
print(nums) 


nums_new_deep = nums.copy() #deep copy
nums_new_deep.append(15)
print(nums_new_deep)
print(nums)