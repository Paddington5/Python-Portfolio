#Helena
#Todo list app
#init
todo = []
donelist = []
#functions
def main():
    file = open("todolist.txt", "r") #opens file with history of list
    todo = [line.strip() for line in file.readlines()]
    print("Welcome to the To-Do List App!")
    print("You can add new items to the to-do list, and then mark them as done to track your accomplishments.")
    print("You can also remove items from the to-do list, or clear the whole list if you want a fresh start.")
    print("Have fun getting stuff done!(TM)")
    shutdown = 0
    while shutdown == 0:
        print(f"To-do list: {todo}")
        print(f"Done: {donelist}")
        action = input("Would you like to ADD / MARKDONE / REMOVE items from the list, CLEAR the entire list, or EXIT the app?  ").lower()
        if action == "add": #add item to list
            additem = input("What would you like to add to the todo list?  ")
            todo.append(additem)
            print(todo)
        if action == "markdone" or action == "mark done" or action == "mark" or action == "done":
            #remove item from list and add to done list
            markdone = input("What would you like to mark as done? ")
            try:
                todo.remove(markdone)
                donelist.append(markdone)
            except:
                print("Error - That item is NOT in your to-do list! Try again please.")
        if action == "remove": #remove item from list without marking as done
            removed = input("What item would you like to remove from the list?  ")
            try:
                todo.remove(removed)
            except:
                print("Error - That item is NOT in your to-do list! Try again please.")
        if action == "clear": #remove all items from the list
            confirm = input("Are you sure you want to clear the list? This action cannot be undone. (yes/no):  ")
            if confirm == "yes":
                todo.clear()
        if action == "exit": #exit the app
            save = input("Save list? (yes/no):  ").lower()
            if save == "yes" or save == "save":
                print("Saving...")
                file = open("todolist.txt", "w") #adds list to file todolist.txt
                for i in range(len(todo)): #writes each item in list into file
                    file.write(todo[i] + """
""")

            print("Shutting down.")
            shutdown = 1
            exit()
            break
#Main
main()
