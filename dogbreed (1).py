#Helena
#Dog Breed
#The purpose of my program is to help users choose a dog breed that meets their needs.

#init
import pandas as pd
data = pd.read_csv('dogbreedinfo.csv') #reads dog data
minweight = data['Minimum Weight'].tolist() #adds minimum weight column to a list
name = data['Name'].tolist() #adds dog breed name column to a list
temperament = data['Temperament'].tolist() #adds dog temperament column to a list
image = data['Image'].tolist() #adds dog image links column to a list
bredfor = data['BredFor'].tolist() #adds dog purpose column to a list
options = []
output = []
check = 0
import random
import webbrowser
#functions
def getDogSize(size):
    global check
    for i in range(len(name)):
        if size == "tiny":
            if minweight[i] <= 10:                        #adds name of dog breeds that meet tiny qualifications to options list
                options.append(name[i])
                check = check + 1
        elif size == "small":
            if minweight[i] <= 25 and minweight[i] >= 11: #adds name of dog breeds that meet small qualifications to options list
                options.append(name[i])
                check = check + 1
        elif size == "medium":
            if minweight[i] <= 60 and minweight[i] >= 26: #adds name of dog breeds that meet medium qualifications to options list
                options.append(name[i])
                check = check + 1
        elif size == "large":
            if minweight[i] > 60:                         #adds name of dog breeds that meet large qualifications to options list
                options.append(name[i])
                check = check + 1
    if check > 0:
        output.append(options[random.randint(0,(len(options)-1))]) #chooses a random dog breed from the options and adds it to output list
        print(f"Here are some options: {options}")
        print(f"I reccomend {output[0]}.")
    else:
        print("Please enter a valid search term: tiny, small, medium, or large.")
    output.clear() #clear the list so it can be reused

def lookup(breedname):
    global check
    for i in range(len(name)):
        if name[i].lower() == breedname.lower():
            check = check + 1
            print(f"This dog is {temperament[i].lower()}. Here is an image!")  #prints the breed's temperament
            webbrowser.open(image[i]) #opens new tab with the image
    if check < 1:
        print("Sorry, we do not have data on that dog breed. :(")

def helpfuldog(purpose):
        global check
        for i in range(len(name)):
            if purpose.lower() in bredfor[i].lower() or purpose in temperament[i].lower():
                options.append(name[i])
                check = check + 1
        if check > 0:
            print(f"Here are some options: {options}")
            output.append(options[random.randint(0,(len(options)-1))])
            print(f"I reccomend {output[0]}.")
        else:
            print("Sorry, we could not find any dogs with that purpose. Try searching something else!")
        output.clear()

        #CANNOT do if purpose in list, else: print("Sorry, we could not find any dogs with that specific purpose. (Make sure to add -ing, like hunting instead of hunt.)")

def menu():
    global check
    print("Hi! Welcome to the Dog Finder. We have lots of options to help you find the dog of your dreams!")
    while check >= 0:
        check = 0
        choice = input("Would you like to (1)search for dogs based on size, (2)search for dogs based on purpose, (3)look up information about a specific breed, or (4)leave the program?:  ")
        if choice == "1" or choice == "size":
            size = input("What size dog would you like? (tiny/small/medium/large): ")
            getDogSize(size)
        elif choice == "2" or choice == "purpose":
            purpose = input("What purpose would you like your dog to have?:  ")
            helpfuldog(purpose)
        elif choice == "3" or choice == "info" or choice == "look up" or choice == "information":
            breedname = input("What type of dog would you like to search for?: ")
            lookup(breedname)
        elif choice == "4" or choice == "leave" or choice == "quit":
            print("Thanks for using this program. Come back soon!")
            check = -1
            break
        else:
            print("Sorry, this program could not understand that. Please enter the number (1, 2, 3, or 4) corresponding with the action you want.")


#Main
#menu()
menu()
#Sources
#Dog Dataset - shared by Mr. J
#Website Name: Code.org
#URL: https://code.org/en-US
#Dataset Source:https://thedogapi.com/en
