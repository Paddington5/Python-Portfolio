#Helena
#calculator
#main
def main():
    print("Welcome to this simple calculator!")

    num1 = int(input("Please enter your first number:  "))
    operator = input("Which operation do you want to perform(+,-,*,/):  ")
    num2 = int(input("Please enter your second number:  "))

    if operator == "+":
        print(calc_sum(num1, num2))
    elif operator == "-":
        print(calc_difference(num1, num2))
    elif operator == "*":
        print(calc_product(num1, num2))
    elif operator == "/":
        print(calc_quotient(num1, num2))
    else:
        print("That does not make sense, sorry.")

#function to add x + y  and return the sum
def calc_sum(x,y):
    return x + y
#function to subtract x-y and return the difference
def calc_difference(x,y):
    return x - y
#function to multiply x*y and return the product
def calc_product(x,y):
    return x*y
#function to divide x/y and return the quotient
def calc_quotient(x,y):
    return x/y
#main
main()
