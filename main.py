import time
import os
list = []

def todo():
    global list
    action = input("What would you like to do with your list?\nView (v) | Edit (e) | Clear (c)\n")
    if action == "v":
        print_list()
        print("-----------------------------------------------------------------------------")
        todo()

    elif action == "e":
        r_or_a = input("Would you like to remove something from your list (remove) or add something to it (add) ?\n")
        if r_or_a.lower() == "add":
            thing_to_add = input("Enter the task you would like to add:\n")
            list.append(thing_to_add)
            print("Your new list: ")
            print_list()
        elif r_or_a.lower() == "remove":
            print_list()
            element = int(input("This is your list, which element would you like to remove?\n"))
            list.pop(element - 2)
            print("Here is your new list:")
            print_list()
            todo()

    elif action == "c":
        clear = input("WARNING This will clear your list!\nWould you still like to go on?\n")
        if clear == "yes":
            list = []
            print("List Cleared Succesfully\n----------------------------------------------------------")
            new_person()
        else:
            todo()

    else:
        print("Invalid")
        todo()
def print_list():
    for i, v in enumerate(list):
        num = i + 1
        print(f"{num}: {v}")

def new_person():
    add_things = input("It seems that you do not have anything on your To Do list.\nWould you like to add things to it? \n")
    time.sleep(1)
    if add_things.lower() == "yes":
        items = int(input("How many tasks would you like to add to the list? "))
        print("Enter them here:")
        for i in range(items):
            task = input()
            list.append(task)
        print("Here is your new list:")
        print_list()
        todo()



if len(list) > 0:
    todo()
else:
    new_person()
