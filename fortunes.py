#Fortunes
#This program takes a theme from user input and lets the user choose whether or not they want lucky numbers. Then the program outputs a fortune according to that input.

#init
import random
import time

#all the possible fortunes and their corresponding categories are at the same index of these lists
categories = ['advice', 'advice', 'advice', 'advice', 'advice', 'advice', 'advice',
              'advice', 'advice', 'advice', 'advice', 'advice', 'advice', 'advice',
              'advice', 'advice', 'advice', 'advice', 'advice', 'prediction',
              'prediction', 'prediction', 'prediction', 'prediction', 'prediction',
              'prediction', 'prediction', 'prediction', 'prediction', 'prediction',
              'prediction', 'personality', 'personality', 'personality', 'personality',
              'personality', 'personality', 'personality','personality', 'personality',
              'proverb', 'proverb', 'proverb', 'proverb', 'proverb', 'proverb', 'proverb',
              'proverb', 'proverb', 'proverb', 'proverb']
fortunes = ["Do not be afraid of competition.", "Get your mind set…confidence will lead you on.", "Sell your ideas-they have exceptional merit.", "Bloom where you are planted.",
            "Beware of all enterprises that require new clothes.", "Be true to your work, your word, and your friend.", "Respect yourself and others will respect you.",
            "Always do right. This will gratify some people and astonish the rest.", "Stay healthy. Walk a mile.", "Eat chocolate to have a sweeter life.",
            "Make yourself necessary to someone.", "Sing everyday and chase the mean blues away.", "Live this day as if it were your last.",
            "Move in the direction of your dreams.", "Appreciate. Appreciate. Appreciate.", "Dance as if no one is watching.", "Reach for joy and all else will follow.",
            "Borrow money from a pessimist. They don't expect it back.", "True love is not something that comes everyday, follow your heart, it knows the right answer.",
            "An exciting opportunity lies ahead of you.", "You will always be surrounded by true friends.", "A routine task will turn into an enchanting adventure.",
            "Your life will be happy and peaceful.", "You will be happy with your spouse.", "You should be able to undertake and complete anything.", "Plan for many pleasures ahead.",
            "You will receive money from an unexpected source.", "A journey of a thousand miles will begin with a single step.", "Expect the unexpected.", "Happy News is on its way.",
            "The one you love is closer than you think.", "You love peace.", "You are kind and friendly.", "You are wise beyond your years.", "Your ability to juggle many tasks will take you far.",
            "You are extremely funny, keep at it.", "You are beautiful.", "You are smarter than you know.", "Your smile lights up the whole room.", "You are strong and capable of anything.",
            "Once you make a decision the universe conspires to make it happen.", "Goodness is the only investment that never fails.", "It is easier to stay out than to get out.",
            "Attitude is a little thing that makes a big difference.", "The family that plays together stays together.", "Experience is the best teacher.",
            "The only way to have a friend is to be one.", "Nothing great was ever achieved without enthusiasm.", "He who throws dirt is losing ground.",
            "Love is like wildflowers…it is often found in the most unlikely places.", "Good things happen to good people."]

numbers = [] #this array holds lucky numbers when the user wants them
output = [] #this array is used to sort possible fortune outputs
check = 0 #this variable is used to check for unexpected input - it will stay 0 if user input is not expected

#functions
def fortuneteller():
    print("Hi, welcome to the Fortune Teller!") #intro to tell the user what the program is about
    print("Whether you are looking for some advice, a prediction about your future, a read on your personality, or a mysterious proverb, we have just what you need.")
    print("Answer a few questions to get your fortune!")
    userschoice = input("What type of fortune would you like - advice, prediction, personality, proverb, or any?:  ") #lets user choose out of 4 fortune categories, or let computer choose for them
    getfortune(userschoice)
    number = input("Would you like lucky numbers? (yes/no):  ") #lets user choose if they want lucky numbers
    if number.lower() != "no" and number.lower() != "yes": #if the user gives unexpected output, program allows one more chance to say yes to lucky numbers
        number = input("? That was not yes or no!! Please enter 'yes' if you want lucky numbers, otherwise we will take that as a no:  ")
        if number.lower() != "yes":
            print("Okay, 'no' it is.")
    print("Your fortune is coming right up...")
    time.sleep(2) #time adds suspense
    print("...")
    time.sleep(1)
    print(output[random.randint(0,(len(output)-1))]) #prints a random fortune from the list of possible options
    if number.lower() == "yes":
        luckynumbers() #if user entered "yes" earlier, lucky numbers are printed at the end of the fortune -- otherwise nothing happens here
    print("Thank you for playing! Enjoy your fortune and have a lucky day!") #conclusion statement signaling to the user that the program is over

def getfortune(theme): #based on the category input by the user, this function sorts all possible fortunes into one list
    global check
    for i in range(len(fortunes)):
        if theme.lower() == "any" or theme.lower() == "random": #if user entered "any", all possible fortunes are added to output list
            output.append(fortunes[i])
            check = check + 1
        elif theme.lower() == categories[i]: #if user entered a category earlier, the fortunes corresponding with that category are added to output list
            output.append(fortunes[i])
            check = check + 1
    if check < 1: #if the user gave unexpected input earlier (not a possible category), check variable will still be zero
        print("We could not understand what kind of fortune you wanted :(")
        userschoice = input("Please enter one of the following choices: advice / prediction / proverb / personality / any:  ") #this gives user another chance to input a category
        getfortune(userschoice) #once new input is in, the program skips back to the beginning of this function

def luckynumbers(): #prints 5 lucky numbers for user
        for i in range(5):
            numbers.append(random.randint(0,100))
        print(f"Your lucky numbers are: ✨{numbers}✨")
        numbers.clear()
#main
fortuneteller()

#Sources
    #Fortune data
    #Description: a collection of fortune cookie sayings
    #Website: Fortune Cookie Sayings - Best Ever Cookie Collection
    #URL: https://www.best-ever-cookie-collection.com/fortune-cookie-sayings.html
    #Author unknown, date unknown
