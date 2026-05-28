#Helena
#weather
#reccomends clothing based on the temperature
#functions
def weather():
    temperature = int(input("Enter the temperature outside: "))
    if temperature >= 90:
        print("Wear shorts, a t-shirt or tank top, and bring a waterbottle with you!!")
    elif temperature >= 70:
        print("Wear shorts and short sleeves.")
    elif temperature >= 40:
        print("Wear long pants and a sweater or jacket.")
    elif temperature >= 0:
        print("Wear sweatpants, layers, and a coat with hat and gloves.")
    else:
        print("BUNDlE UP!!! Wear your biggest coat possible. Or maybe just stay inside.")
#main
weather()
