#hogwarts
#program asks for a name and assigns that person to one of the harry potter houses

#init
import time
import random
#functions
def main():
    print("Welcome to Hogwarts")
    num = 0
    again = "yes"
    while again == "yes":
        name = input("What is your name:  ")
        name = name.lower()
        for i in range(2):
            time.sleep(2)
            print("...")
        time.sleep(3)
        print(".....")
        time.sleep(1)
        if num == 0:
            print(house(name))
        elif num == 1:
            print(house1(name))
        elif num == 2:
            print(house2(name))
        elif num == 3:
            print
        again = input("Would you like to be assigned to a new house? (yes/no):  ")
        again = again.lower()
        if again == "no":
            break
        elif again != "yes":
            print("That was unexpected, so I'll take that as a no.")
            break
#this function checks a name and returns a house from harry potter
def house(name):
    if name == "harry" or name == "ron" or name == "hermione":
        return "Gryffindor!"
    elif name == "newt" or name == "nymphadora" or name == "pomona":
        return "Hufflepuff!"
    elif name == "luna" or name == "cho" or name == "filius":
        return "Ravenclaw!"
    elif name == "voldemort" or name == "draco" or name == "severus":
        return "Slytherin!"
    else:
        num = random.randint(1,4)
        if num == 1:
            return "Gryffindor!"
        elif num == 2:
            return "Ravenclaw!"
        elif num == 3:
            return "Slytherin!"
        else:
            return "Hufflepuff!"
#main
main()
