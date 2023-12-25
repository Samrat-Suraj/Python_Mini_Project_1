
import random
You = input("Enter Your Choice Sanke for s Gun fo g and water for w \n")
com=random.randint(0,2)
choise = ("s" , "w" , "g")
comp=choise[com]

def swg( comp,You ):
    if comp==You:
        return None
    elif comp=="g" and You=="w":
        return True
    elif comp=="w" and You == "s":
        return True
    elif comp=="s" and You =="g":
        return True
    else:
        return False
    
print(f"Your Coise is : {You} Computer genrate {comp} ")
win=swg(comp,You)

if win is None:
    print("Match Draw")
if win is True:
    print("Wow You Win")
else:
    print("You Lose ")

