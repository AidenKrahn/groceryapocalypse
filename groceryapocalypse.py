#----------------------
#program with lists
#Aiden Krahn
#OCDONOTSTEAL
#Started March 21, 2023
#-----------------------

import random
#lists
#items = [name, price, damage, bribe%]
tomato = ["tomato", 3, 5, 10]
milk = ["milk", 7, 10, 15]
raisins = ["raisins", 2, 1, 1]
printerink = ['printerink', 60, 4, 80]
football = ['football', 15, 15, 40]
bleach = ['bleach', 10, 11, 20]
novel = ['novel', 7, 8, 50]
mop = ['mop', 5, 10, 20]
toiletpaper = ['toiletpaper', 13, 3, 67]
beef = ['beef', 20, 6, 44]

aisle1items = [tomato, milk, raisins, beef]
aisle2items = [mop, toiletpaper, bleach]
aisle3items = [printerink, football]


def aisleask():
    print("Money-", money)
    print("1- food. 2-cleaning supplies. 3-misc. 4-exit")
    aisle = int(input("Which aisle will you go to?  "))
    if aisle == 1:
        aisle1()
        
    elif aisle == 2:
        aisle2()
        
    elif aisle == 3:
        aisle3()
        
    elif aisle == 4:
        finalencounter()
        
def extract(itm):
    return [item[0] for item in itm]
    
def aisle1():
    global money
    print(f"You have {money} dollars")
    
    print(f"You have-", have)
    
    varsol = extract(aisle1items)
    
    print(f"You look at the shelves. They have-{varsol}")
    
    food = int(input("What will you buy?  "))
    
    if money < aisle1items[food][1]:
        print("You don't have enough money")
        
    else:
        money -= aisle1items[food][1]
        have.append(aisle1items.pop(food))
    
    print("You have-", have)
    
    leave = input("Anything else?(y/n)  ")
    
    if leave == "y":
        aisle1()
        return money
        
    elif leave == "n":
        aisleask()
        return money
    
    
    
def aisle2():
    global money
    print(f"You have {money} dollars")
    print(f"You have-", have)
    varsol = extract(aisle2items)
    print(f"You look at the shelves. They have-{varsol}")
    food = int(input("What will you buy?  "))
    if money < aisle2items[food][1]:
        print("You don't have enough money")
        
    else:
        money -= aisle2items[food][1]
        have.append(aisle2items.pop(food))
    print("You have-", have)
    leave = input("Anything else?(y/n)  ")
    if leave == "y":
        aisle2()
        return money
        
    elif leave == "n":
        aisleask()
        return money
    
def aisle3():
    global money
    print(f"You have {money} dollars")
    print(f"You have-", have)
    varsol = extract(aisle3items)
    print(f"You look at the shelves. They have-{varsol}")
    food = int(input("What will you buy?  "))
    if money < aisle3items[food][1]:
        print("You don't have enough money")
        
    else:
        money -= aisle3items[food][1]
        have.append(aisle3items.pop(food))
        
    print("You have-", have)
    leave = input("Anything else?(y/n)  ")
    if leave == "y":
        aisle3()
        return money
        
    elif leave == "n":
        aisleask()
        return money
        
def finalencounter():
    print("You were about to leave, but you were ambushed!")
    print("Someone tries to rob you of your things/money")
    print('''
1. Attack
2. Negotiate
3. Flee
''')
    print(have)
    play = True
    while play == True:
        action = int(input("What will you do?  "))
        
        if action == 1:
            print(have)
            atk = int(input("What will you attack with?  "))
            ehealth -= have[atk][2]
            have.pop(atk)
            print(f" You did {have[atk][2]} damage.")
            
            if ehealth < 0:
                print("You defeated the crook and ran away with your stuff!")
                play = False
                break
            
            else:
                play = True
                
        elif action == 2:
            print(have)
            atk = int(input("What can you give him to get him to go away?  "))
            con = random.randint(1, 100)
            
            if con > have[atk][3]:
                print("It wasn't enough to convince the crook.")
                play = True
                have.pop(atk)
                
            elif con < have[atk][3]:
                print("He went away!")
                have.pop(atk)
                play = False
                break
            
        elif action == 3:
            shot = random.randint(1, 100)
            if shot > 90:
                print("You got away!")
                break
                
            elif shot < 90:
                print("The crook shot, you and you died.")
                print("Game Over")
                break
                
def doyousurvive():
    chance = len(have)
    survival = random.randint(chance, 10)
    if survival <= 5:
        print("You died to the nuclear wastes due to lack of supplies")
        print("You failed")
        
    elif survival > 5:
        print("You managed to make it in the apocalypse.")
        print("So long space cowboy")
        

#--Main code
print("You walk into a grocery store, and you need some supplies for an apocalypse shelter.")
print("You have $70")
money = 70
have = []
ehealth = 44
aisleask()
doyousurvive()

