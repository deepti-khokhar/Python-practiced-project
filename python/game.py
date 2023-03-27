import random

def gamewin(comp,you):
    if comp == you:
        return None
    elif comp == 's':
        if you == 'w':
            return False
    elif comp == 's':
        if you =='g':
            return True
    elif comp == 'w':
            if you == 'g':
             return True
    elif comp == 'w':
            if you =='s':
                return False
    elif comp == 'g':
        if you == 's':
            return True
    elif comp == 'g':
        if you == 'w':
            return False
("comp turn:snake (s) water (w) gun (g)?")
randno = random.randint(1, 3)
if randno == 1:
    comp = ('s')
elif randno == 2:
    comp = ('w')
elif randno == 3:
    comp = ('g')

you = input("player's turn: Snake(s)Water(w) Gun(g)")
a =gamewin( comp , you)

print(f"comp choose {comp}")
print(f"you choose {you}")

if a == None:
        print("the game is a tie !!")
elif a :
       print("you win ***")
else:
             print("you loose")




