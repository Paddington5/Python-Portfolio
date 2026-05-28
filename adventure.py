#Helena
#adventure - choose your own adventure story

#functions
def forest():
    print("Welcome to Python Forest!")
    path = input("There are two ways you can go. Would you like to take the stairs or follow the trail?:  ")
    if path == "stairs":
        print("You climb up all the stairs, and see a cliff ahead.")
        cliff = input("Would you like to take the risk and look over the cliff? (yes/no):  ")
        if cliff == "yes":
            print("There is a beautiful view here! Take a photo!")
        elif cliff == "no":
            print("Safe choice. You enjoy the trees and head back down.")
    elif path == "trail":
        print("You follow the woodchip trail until the path splits again.")
        split = input("Would you like to follow the muddy path or the sandy path?(muddy/sandy):  ")
        if split == "muddy":
            print("You follow the mud to a swamp, and suddenly a crocodile comes out of nowhere!")
            print("RUNNNN!")
        elif split == "sandy":
            print("You follow the sand to a lovely beach. Now you can relax in the sun!")
#main
forest()
