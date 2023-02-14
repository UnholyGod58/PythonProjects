#Joshua Hodder
#started [13/02/2023]
# Seach and Sort Through a List of Names
#listen time: 

import os

os.system('cls')

names = ["Ava", "Ethan", "Emma", "Michael", "Isabelle", "William", "Sophia", "James", "Olivia", "Alexander", "Mia", "Benjamin", "Charlotte", "Daniel", "Abigail"]
sorted_names = names


def input_wait():
    input("Press Enter to Continue...")
    os.system('cls')
    choices()

def display_list():
    print("This is the Current List of Names:")
    for i in names:
        print(i)
    input_wait()
    
def sort_list():
    global sorted_names
    print("How Would You like to Sort The List?\n1: Alphabetically\n2: Reverse Alphabetically\n3: Length Accending\n4: Length Descending")
    try:
        choice = int(input())
    except:
        os.system('cls')
        print("Enter an option 1-4")
        sort_list()
    if choice == 1:
        return sorted(names)
    elif choice == 2:
        return sorted(names, reverse=True)
    elif choice == 3:
        return sorted(names, key=len, reverse=True)
    elif choice == 4:
        return sorted(names, key=len)
    else:
        os.system('cls')
        print("Enter an option 1-4")
        sort_list()

def choose_sort_list():
    global names
    print("What Would You Like to do?\n1: Only Display the List Sorted\n2: Sort the List")
    try:
        choice = int(input())
    except:
        os.system('cls')
        print("Enter 1 or 2")
        choose_sort_list()
    if choice == 1:
        os.system('cls')
        sorted_names = (sort_list())
        print("The Sorted List is:")
        for i in sorted_names:
            print(i)
        input_wait()
    elif choice == 2:
        os.system('cls')
        names = sort_list()
        print("The Sorted List is:")
        for i in names:
            print(i)
        input_wait()
    else:
        os.system('cls')
        print("Enter an Option 1-2")
        choose_sort_list()
    
def choices():
    print("What Would you like to do?\n1: Print the List 'as is'\n2: Sort the List\n3: Add to the List\n4: Remove from the List\n5: Exit")
    try:
        choice = int(input())
    except:
        os.system('cls')
        print("Enter an option 1-5")
        choices()
    if choice == 1:
        os.system('cls')
        display_list()
    elif choice == 2:
        os.system('cls')
        choose_sort_list()
    elif choice == 3:
        os.system('cls')
    elif choice == 4:
        os.system('cls')
    elif choice == 5:
        os.system('cls')
    else:
        os.system('cls')
        print("Enter an Option 1-5")
        choices()
choices()