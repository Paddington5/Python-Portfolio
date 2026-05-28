#Helena
#Init
import random
verbs = ["RUN", "DRIVE", "FLY", "SKIP", "CRAWL", "HOP", "YELL"]
places = ["MCDONALDS", "PARIS", "THE BEACH", "DETROIT", "CALIFORNIA", "JONES COLLEGE PREP"]
foods = ["PIZZA", "FETTUCINE ALFREDO", "ICE CREAM", "SUSHI", "STEAK", "CHIPS", "POPCORN", "DONUTS"]
adjectives = ["SPARKLY", "SPIKY", "LOUD", "TALL", "SMOOTH", "BLURRY", "MUDDY", "PRETTY", "ANGRY", "SCARY", "SMART","CLEAN", "GENTLE", "MYSTERIOUS", "HUGE", "DREADFUL", "HILARIOUS"]
names = ["WILLY WONKA", "HARRY POTTER", "SANTA", "OLAF", "THE LORAX", "SNOW WHITE", "TAYLOR SWIFT"]
pluralnouns = ["BOOKS", "HATS", "SNAKES", "TACOS", "PENNIES", "EYELASHES", "CARS", "DOORKNOBS"]
#functions
def madlibs():
    print("Welcome to Mad Libs!")
    print("Enter the types of words asked for to complete the story!")
    #gather input
    number = input("Enter a number: ").upper()
    if number == "RANDOM":
        number = random.randint(2,100)
    verb = input("Enter a verb: ").upper()
    if verb == "RANDOM":
        verb = random.choice(verbs)
    place = input("Enter a place: ").upper()
    if place == "RANDOM":
        place = random.choice(places)
    food = input("Enter a food: ").upper()
    if food == "RANDOM":
        food = random.choice(foods)
    adjective1 = input("Enter an adjective: ").upper()
    if adjective1 == "RANDOM":
        adjective1 = random.choice(adjectives)
    adjective2 = input("Enter another adjective: ").upper()
    if adjective2 == "RANDOM":
        adjective2 = random.choice(adjectives)
    name = input("Enter a name: ").upper()
    if name == "RANDOM":
        name = random.choice(names)
    pluralnoun = input("Enter a plural noun: ").upper()
    if pluralnoun == "RANDOM":
        pluralnoun = random.choice(pluralnouns)
    adjective3 = input("Enter an adjective: ").upper()
    if adjective3 == "RANDOM":
        adjective3 = random.choice(adjectives)
    #story
    print(f"""In \033[1m {number} \033[0m days, I'm going to \033[1m {verb} \033[0m to \033[1m {place} \033[0m. It's kind of far,
so I brought \033[1m {food} \033[0m for the road. The trees are so \033[1m {adjective1} \033[0m in autumn,
and I will take lots of \033[1m {adjective2} \033[0m photos! \033[1m {name} \033[0m is in charge, so we
will want to stop for \033[1m {pluralnoun} \033[0m on the way. I'm so \033[1m {adjective3} \033[0m!""")

#Main
madlibs()
