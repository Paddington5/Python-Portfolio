#Helena
#nickname: answer questions to find out what kind of dessert you are

#functions
def dessert():
    repeat = "yes"
    while (repeat == "yes"):
        print("Answer the questions truthfully to find out what kind of dessert you are!")
        season = input("Do you prefer summer or winter?:  ")
        season = season.lower()
        if season == "summer":
            swim = input("Where would you go to swim in the summer, beach or pool?:  ")
            swim = swim.lower()
            if swim == "beach":
                flavor = input("Would you say you're more vanilla or fruit?:  ")
                flavor = flavor.lower()
                if flavor == "vanilla":
                    print("You are ice cream!")
                elif flavor == "fruit":
                    print("You are a popsicle!")
                else:
                    print("That input was unexpected. Please use the words in the question!")
            elif swim == "pool":
                topping = input("Which word sounds better: sprinkles or skittles?:  ")
                topping = topping.lower()
                if topping == "sprinkles":
                    print("You are a cupcake!")
                elif topping == "skittles":
                    print("You are candy!")
                else:
                    print("That input was unexpected. Please use the words in the question!")
            else:
                print("That input was unexpected. Please use the words in the question!")
        elif season == "winter":
            warm = input("Where would you go to warm up in winter, cafe or fireplace?:  ")
            warm = warm.lower()
            if warm == "cafe":
                shape = input("Are you a square or a circle?:  ")
                shape = shape.lower()
                if shape == "square":
                    print("You are a brownie!")
                elif shape == "circle":
                    print("You are a cookie!")
                else:
                    print("That input was unexpected. Please use the words in the question!")
            elif warm == "fireplace":
                size = input("Would you rather be big or small?:  ")
                size = size.lower()
                if size == "big":
                    print("You are a whole pie!")
                elif size == "small":
                    print("You are a little donut!")
                else:
                    print("That input was unexpected. Please use the words in the question!")
            else:
                print("That input was unexpected. Please use the words in the question!")
        else:
            print("That input was unexpected. Please use the words in the question!")
        repeat = input("Would you like to play again? (yes/no):  ")
        repeat = repeat.lower()
        if repeat == "no":
            break
        elif repeat != "yes":
            print("That was unexpected, so I'll take that as a no.")
            break


#main
dessert()
