# In this we have to calculate the price after taxes and discount

def calculate_total(price,tax_rate,discount):
    tax = price * tax_rate
    final_price = price + tax - discount
    print(f"Total : ${final_price}")

calculate_total(100,0.08,10) 


calculate_total(price=200,tax_rate=0.08,discount=10)


# global variables can be accessed anywhere
# local variables have scope 
# same variable name in local and global both can be used 
# local value will be used for the scope where it's initialised
# but global will be used outside of their scope


value = 10

def scope():
    value = 20
    print(f"Value in Local : {value}")
    pass

scope()
print(f"Value in Global : {value}")

