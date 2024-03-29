#Joshua Hodder
#Redo of da Listy
#25/4/'23


import os, msvcrt, sqlite3


student_list = [["dawson", 100, 98, 95, 95], ["dylan", 96, 99, 94, 95,  95], ["lemburger", 23, 45, 12, 2], ["dequiriuse", 78, 69, 65, 82]]
options = [0,1,2,3,4,5]

def create_connection(db_file):
    #create a database connection to the SQLite database
    #return: Connection object or None
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except Exception as e:
        print(e)
    return conn

def create_table(conn,table, columns):
    col = ",".join(columns)
    sql = f'''CREATE TABLE IF NOT EXISTS {table}( id INTEGER PRIMARY KEY, {col});'''
    conn.execute(sql)

def insert_db(conn,table, columns,data):
    sql=f'''INSERT INTO {table} {tuple(columns)} VALUES {tuple(data)};'''
    conn.execute(sql)
    conn.commit()

def select_db(conn,table,columns_and_data=None):
    if not columns_and_data==None:
        col = " AND ".join(columns_and_data)
        sql=f'''SELECT * FROM {table} WHERE {col}'''
        return conn.execute(sql)
    else:
        sql =f"SELECT * from {table}"
        return conn.execute(sql)

def update_db(conn,table,columns_and_data,where_to_update):
    col = ",".join(columns_and_data)
    sql = f"UPDATE {table} set {col} where {where_to_update}"
    conn.execute(sql)
    conn.commit()  

def delete_db(conn,table,column,what_to_remove):
    sql=f'''DELETE FROM {table} WHERE {column} = {what_to_remove}'''
    conn.execute(sql)
    conn.commit()  

def student_add():
    #add a student to the array
    for i in student_list:
        name = input("Input Student Name:\n").strip().lower()
        if name.count != 0:
            if not name in i:
                if not name.replace(" ", "").isalpha():
                        os.system("cls")
                        print("Student's Name Should Only Contain Letters and Spaces\n")
                        
                else:
                    student_list.append[name]
                    print("Student Added to the List\nPress any key to continue")
                    msvcrt.getch()
                    break
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
    name = input("Enter the Student you Would Like to Remove:\n").strip().lower()
    for i in student_list:
        if name in i:
            os.system("cls")
            student_list.remove(i)
            print("Student Removed\nPress any key to Continue")
            msvcrt.getch()
            break
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
    name = input("Enter the Student you'd Like to Grade:\n").strip().lower()
    for i in student_list:
        if name in i:
            if i.count != 4:
                os.system("cls")
                while True:
                    print("Student Grades:\n" + i[1:])
                    try:
                        grade = int(input("Enter the Grade you Would Like to Add:\n"))
                        if grade < 0 or grade > 100:
                            print("Enter a Grade 0 - 100")
                        else: 
                            os.system("cls")
                            student_list[i].append(grade)
                            print("Grade Added to Student\nPress Any Key to Continue")
                            msvcrt.getch()
                            break
                    except ValueError:
                        os.system("cls")
                        print("Enter a Grade 0 - 100") 
        else:
            print("That Student Already has Their Grades\nPress any key to Continue")
            msvcrt.getch()
            os.system("cls")
            continue 
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
    print("Students:")
    for i in student_list:
        print(i[0])
    student = input("Enter the Student Name:\n").strip().lower()
    for i in student:
        if i in student_list:
            os.system("cls")
            while True:
                    print("Student Grades:\n" + i[1:])
                    try:
                        grade = int(input("Enter the Grade you Would Like to Remove:\n"))
                        if grade < 0 or grade > 100:
                            print("Enter a Grade 0 - 100")
                        else: 
                            if grade in i:
                                os.system("cls")
                                student_list[i].remove(grade)
                                print("Grade Removed from Student\nPress Any Key to Continue")
                                msvcrt.getch()
                                break
                            else:
                                os.system("cls")
                                print("Student Does Not Have This Grade")
                                continue
                    except ValueError:
                        os.system("cls")
                        print("Enter a Grade 0 - 100")
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

def average():
    summ = 0
    count = 0
    print("Students Average:")
    for i in student_list:
        if len(i) != 1:
            avg = sum(i[1:]) / (len(i) - 1)
            print(i[0] + " Average: " + avg)
        else: 
            print(i[0] + " Average: N/A")
        summ += sum(i[1:])
        count += (len(i) - 1)
    print("\nClass Average: " + (summ/count) + "\nPress any key to Continue")
    msvcrt.getch()
    os.system("cls")
    
def exit():
    quit()    

menus = dict({0:student_add, 1:student_remove, 2:grade_add, 3:grade_remove, 4:average, 5:exit})

menu = True
while menu == True:
    try:
        choice = int(input("Select an Option:\n0: Add a Student\n1: Remove a Student\n2: Add a Grade\n3: Remove a Grade\n4: List CLass and Average\n5: Exit\n"))
        if choice in options:
            os.system("cls")
            menus[choice]()
            menu = False
        else:
            os.system("cls")
            print("Enter a Valid Option")
    except:
        os.system("cls")
        print("Enter a Valid Option-")
        