import random as rm 

num = rm.randint(1,10)
choice = rm.choice(["heart","diamond","spade"])


# if ace and of diamond the player wins 

if(num==1 and choice=="diamond"):
    print("CONGRATS!")
else:
    print("YOU LOSE!")
