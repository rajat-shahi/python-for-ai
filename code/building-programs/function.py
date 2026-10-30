# we use functions to create reusable blocks of code
# DRY - Don't Repeat Yourself

def say_hello():
    print("Hello!")
    pass 

def add(x,y):
    result = x + y
    return result,x,y

def calculate(x,y):
    add = x+y
    diff = x-y
    mul = x*y 
    div = x/y 
    return dict(add=add,diff=diff,mul=mul,div=div)

def check_weather(temp):
    if(temp>25):
        return "Hot"
    elif (temp<=25 and temp>15):
        return "Moderate"
    else:
        return "Cold"


say_hello()
print("hello ji")
res,num1,num2 = add(10,15)
print(res,num1,num2)

calculate_res = calculate(10,15)
print(calculate_res)

print(check_weather(-12))


def greet(first_name, last_name):
    print(f"Hello, {first_name} {last_name}")

greet(last_name="shahi",first_name="rajat")


# assigning default values 
def sum(b,c,a=10):
    print(f"Addition Result of {a},{b},{c}: {a+b+c}")

sum(5,10,15)