


import os 
student_list = [["dawson", 100, 98, 95, 95], ["dylan", 96, 99, 94, 95,  95], ["lemburger", 23, 45, 12, 2], ["dequiriuse", 78, 69, 65, 82]]

def student_add():
    #add a student to the array
    for i in student_list:
        name = input("Input Student Name:\n").trim().lower()
        if name.count != 0:
            if not name in i:
                if not name.replace(" ", "").isalpha():
                        os.system("cls")
                        print("Student's Name Should Only Contain Letters and Spaces\n")
                        
                else:
                    student_list.append[name]
                    print("Student Added to the List\nPress any key to continue")
    else:
        temp = input("That Student Already Exists\nWould you Like to Add Another Student\n[y/n]")
        while True:
            if temp == "y":
                os.system("cls")
                student_add()
                break
            elif temp == "n":
                os.system("cls")
                break
            else:
                temp = input("Enter y or n")
        
def student_remove():
    print("Students:")
    for i in student_list:
        print(i[0])
    name = input("Enter the Student you Would Like to Remove:\n").trim().lower()
    for i in student_list:
        if name in i:
            student_list.remove(i)
    else:
        os.system("cls")
        temp = input("That Student Does Not Exist\nWould you Like to Try Again\n[y/n]")
        while True:
            if temp == "y":
                os.system("cls")
                student_remove()
                break  
            elif temp == "n":
                os.system("cls")
                break
            else:
                temp = input("Enter y or  n")

def grade_add():
    print("Students:")
    for i in student_list:
        print(i[0])
    name = input("Enter the Student you'd Like to Grade:\n").trim().lower()
    for i in student_list:
        if name in i:
            if i.count == 4:
                pass
        else:
            temp = input("That Student Does Not Exist\nWould you Like to Try Again\n[y/n]")
            while True:
                if temp == "y":
                    os.system("cls")
                    grade_add()
                    break  
                elif temp == "n":
                    os.system("cls")
                    break
                else:
                    temp = input("Enter y or  n")

def grade_remove():
    pass

def student_average():
    pass

def class_average():
    pass

def list_class():
    pass

student_remove()