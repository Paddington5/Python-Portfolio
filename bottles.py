#Helena
#99 Bottles - print lyrics to 99 bottles of milk on the wall song
count = 99
for i in range(98):
    print(str(count) + " bottles of milk on the wall")
    print(str(count) + " bottles of milk")
    print("Take one down pass it around")
    count = count - 1
    if count>1:
        print(str(count) +" bottles of milk on the wall")
    else:
        print("One bottle of milk on the wall")
    print(" ")
print("One bottle of milk on the wall")
print("One bottle of milk")
print("Take it down pass it around")
print("No more bottles of milk on the wall")
print("Boo Hoo!")
