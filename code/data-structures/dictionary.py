# store data in {key,value} pairs
# key must be unique

# creating dictionaries
my_dict = {}

phone_dir = {
    "rajat" : "921",
    "aman" : "21321",
    "shreya": "213321"
}

print(phone_dir)
print(type(phone_dir))

scores = dict(math=22,physics=91,english=26)
print(scores)

scores_tmp = scores.copy()

"""
accessing dictionary
"""

print(scores["math"])
# print(scores["hindi"]) -> raises key error 

print(scores.get("math"))
print(scores.get("hindi")) # this returns None - safe check 


# if not found then lets return not available
print(scores.get("math","not available")) # available so 22 printed
print(scores.get("chemistry","not available")) # not available printed


"""
CHANGING DICTIONARIES
"""

person = {
    "name":"rajat shahi",
    "age" : 26,
    "country" : "India",
    "fav_driver" : "Lewis Hamilton"
}

print(person)

person["fav_driver"] = "Max Verstappen"
print(person)

person["email"] = "rajatshahixyz@mail.com"
print(person)


del person["fav_driver"]
print(person)

country = person.pop("country")
print(country)

print(person)

person.clear()
print(person)



"""
DICTIONARY METHODS : 
"""

person = {
    "name":"rajat",
    "age":26,
    "city":"delhi"
}

print(person.keys())
print(person.values())
print(person.items())


# check if key exists 
if "city" in person:
    print("city exists")

#update multiple values
person.update({"age":22,"email":"xyz@mail.com"})
print(person)



"""
NESTED DICTIONARY
"""

students = {
    "rajat" : {"class":12,"age":15},
    "aman" : {"class":5,"age":7}
}

print(students["rajat"]["class"])



"""
COMMON MISTAKES : 
- key error when key doesn't exists (use get)
- use immutable keys only or strings
"""

dictionary = {
    (1,2) : "location",
    "name" : "rajat",
}

print(dictionary)
print(dictionary[(1,2)])