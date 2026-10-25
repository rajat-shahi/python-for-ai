# string manipulations - advanced text operations
# fstring = formatted strings 

first_name = "Rajat"
last_name = "Shahi"
intro = f"Hi there, my name is {first_name} {last_name}"

print(r"\n\nC://rajat-shahi") #raw strings



"""
STRING METHODS : 
--------------

- changing case
- cleaning strings
- finding and replacing

"""

name = "rajat Shahi"
print(name.upper())
print(name.lower())
print(name.title())


text = "Hello    ji   "
print(len(text))
text = text.strip()
print(len(text))

price = "$21.99 $11"
price.strip("$")
price.replace("$","")


sentence = "i love python programming with python"
sentence = sentence.title()

print(sentence.startswith("I"))
print(sentence.endswith("python"))
print(sentence.endswith("Python"))
print(sentence.find("Python"))
print(sentence.count("Python"))
sentence.replace("Python","Javascript")
print(sentence)