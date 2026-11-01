def divide(a,b):
    return a/b

def try_divide(a,b):
    try:
        # code that might cause an error
        print(divide(a,b))

    except:
        # code that runs if there's an error
        print("There is some error")

try_divide(10,2)
try_divide(10,0)