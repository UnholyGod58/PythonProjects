#Joshua Hodder
#started [13/02/2023]
#works [14/02/2023] - 12:19am
# Seach and Sort Through a List of Names
#listen time: 01:23:31

import os

os.system('cls')

names = ["Ava", "Ethan", "Emma", "Dawson", "Isabelle", "William", "Sophia", "James", "Olivia", "Alexander", "Mia", "Benjamin", "Charlotte", "Daniel", "Abigail"]
sorted_names = names

def input_wait():
    input("Press Enter to Continue...")
    os.system('cls')
    menu()

def add_list():
    print("What Name Would You Like To Add?")
    name = input().lower().capitalize()
    if name.isalpha():
        for i in names:
            if not name in i:
                names.append(name)
                print(f"Added {name} to the List\nNote: You Should Re-Sort the List")
                input_wait()
        else:
            print(name, " Is Already In The List\n1: Try Again\n2: Return to the Menu")
            while True:
                try:
                    choice = int(input())
                except:
                    os.system('cls')
                    print("Enter 1 or 2")
                    continue
                if choice == 1:
                    add_list()
                    break
                elif choice == 2:
                    menu()
                    break
                else:
                    print("Enter 1 or 2")      
    else:
        os.system('cls')
        print("First Name Only\nNo Spaces, Numbers, or Special Characters")
        add_list()
        
def remove_list():
    print("What Name Would You Like To Remove?")
    name = input().lower().capitalize()
    for i in names:
        if name in i:
            names.remove(name)
            print(f"Removed {name} From the List\nNote: You Should Re-Sort the List")
    else:
        print(name, " Is Not in The List\n1: Try Again\n2: Return to the Menu")
        while True:
                try:
                    choice = int(input())
                except:
                    os.system('cls')
                    print("Enter 1 or 2")
                    continue
                if choice == 1:
                    add_list()
                    break
                elif choice == 2:
                    menu()
                    break
                else:
                    print("Enter 1 or 2")
        
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
    
def menu():
    print("What Would you like to do?\n1: Print the List 'as is'\n2: Sort the List\n3: Add to the List\n4: Remove from the List\n5: Exit")
    try:
        choice = int(input())
    except:
        os.system('cls')
        print("Enter an option 1-5")
        menu()
    if choice == 1:
        os.system('cls')
        display_list()
    elif choice == 2:
        os.system('cls')
        choose_sort_list()
    elif choice == 3:
        os.system('cls')
        add_list()
    elif choice == 4:
        os.system('cls')
        remove_list()
    elif choice == 5:
        os.system('cls')
        exit()
    else:
        os.system('cls')
        print("Enter an Option 1-5")
        menu()

menu()