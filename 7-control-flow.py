# our programs need to make decisions 
# if this, then that 
# controlling the flow of the program is an excellent idea

temperature = 25 

if temperature > 25:
    print("The temperature is high")
elif(temperature > 18 and temperature <=25):
    print("The temperature is moderate")
else:
    print("The temperature is low")


# loops - repeat code multiple times
# python is a 0-indexed based programming language 

for i in range(5):
    print(f"Case:{i} Hello", sep="|", end="<3 ")

# print 1 second intervals from 1 to 5
for i in range(1,6):
    print(f"{i}sec")

# print 2 second intervals from 0 to 10 
for i in range(0,11,2):
    print(f"{i}sec")