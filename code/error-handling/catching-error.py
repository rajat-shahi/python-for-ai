def age_increment(age,num):
    try:
        print(f"In 10 years you'll be {age+10}")
        print(f"You age/random_num = {age/num}")
    except ValueError:
        print("Please enter a valid input[number]")
    except ZeroDivisionError:
        print("You can't divide a number by zero")


age = input("Enter your age :")
num = int(input("Enter the random number :"))
age_increment(age,num)