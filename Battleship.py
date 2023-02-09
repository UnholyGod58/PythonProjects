#By : Joshua Hodder
#Date started : 2023-02-08
#A Two Player Game Of Battleship

import os
import msvcrt
os.system('cls')
print("Welcome to battleship\nPress any key to continue")
msvcrt.getch()
os.system('cls')
Vaild_Position = " "
P1_Boat1b = ""
P1_Boat2b = ""
P2_Boat1b = ""
P2_Boat2b = ""
P1_Pickb = []
P2_Pickb = []
P1_Score = 0
P2_Score = 0

grid = []
for i in range(5): # makes 5 sections to the grid list
    grid.append(['-' for i in range(5)]) #adds 5 empty spaces to the grid list

#sets up the grid

def display_grid(grid):
    print('  1 2 3 4 5')
    print('a ' + ' '.join(grid[0]))
    print('b ' + ' '.join(grid[1]))
    print('c ' + ' '.join(grid[2]))
    print('d ' + ' '.join(grid[3]))
    print('e ' + ' '.join(grid[4]))

def convert_input(input_string):
    row = ord(input_string[0].upper()) - 65 # converts letter to number for row  (A -> 0 B-> 1 C-> 2 D-> 3 E-> 4)
    col = int(input_string[1]) - 1 # gets column number from 0 to 4
    return row, col

def pick_boat(Boata, Boatb):
    global Vaild_Position
    Position_1 = int(Boata[1]) - 1
    Position_2 = int(Boata[1]) + 1
    #Sets the second position of the boat part 1
    if Boata[0] == "a":
        Direction1 = "b"
    elif Boata[0] == "e":
        Direction1 = "d"
    elif Boata[0] == "b":
        Direction1 = "a"
        Direction2 = "c"
    elif Boata[0] == "c":
        Direction1 = "b"
        Direction2 = "d"
    elif Boata[0] == "d":
        Direction1 = "c"
        Direction2 = "e"
    #Sets the second position of the boat part 2
    
    if Boata[0] in "ae":
        if Boata[1] == "1":
            Boatb = (input(f"Select boat second position ({Direction1}1 or {Boata[0]}2): ")).lower()
            Vaild_Position = [f"{Direction1}1", f"{Boata[0]}2"]
        elif Boata[1] == "5":
            Boatb = (input(f"Select boat second position ({Direction1}5 or {Boata[0]}4): ")).lower()
            Vaild_Position = [f"{Direction1}5", f"{Boata[0]}4"]
        else:
            Boatb = (input(f"Select boat second position ({Boata[0]}{Position_1}, {Direction1}{Boata[1]}, {Boata[0]}{Position_2}): ")).lower()
            Vaild_Position = [f"{Boata[0]}{Position_1}", f"{Direction1}{Boata[1]}", f"{Boata[0]}{Position_2}"]
    #Next position for the boat in row a or c and checks if it is valid
    else:
        if Boata[1] == "1":
            Boatb = (input(f"Select boat second position ({Direction1}1, {Boata[0]}2, {Direction2}1): ")).lower()
            Vaild_Position = [f"{Direction1}1", f"{Boata[0]}2", f"{Direction2}1"]
        elif Boata[1] == "5":
            Boatb = (input(f"Select boat second position ({Direction1}5, {Boata[0]}4, {Direction2}5): ")).lower()
            Vaild_Position = [f"{Direction1}5", f"{Boata[0]}4", f"{Direction2}5"]
        else:
            Boatb = (input(f"Select boat second position ({Direction1}{Boata[1]}, {Boata[0]}{Position_1}, {Direction2}{Boata[1]}, {Boata[0]}{Position_2}): ")).lower()
            Vaild_Position = [f"{Direction1}{Boata[1]}", f"{Boata[0]}{Position_1}", f"{Direction2}{Boata[1]}", f"{Boata[0]}{Position_2}"]
    #Next position for the boat in all other positions and checks if it is valid
    return Boata, Boatb

def pick_boat2(BoatA, BoatB, BoatA1, BoatB1):
    BoatA, BoatB = pick_boat(BoatA, BoatB)
    while not BoatB in Vaild_Position:
        BoatB = (input("Please enter a valid position: ")).lower()
    while BoatB == BoatA1 or BoatB == BoatB1:
        BoatB = (input("That position is already in use. Please enter a valid position: ")).lower()
    #ensures that the second position of the boat is valid
    return BoatA, BoatB

def check_in(boat):
    while not boat[0] in "abcde" or not boat[1] in "12345" or len(boat) != 2:
        boat = (input("Please enter a valid position (a1 - e5): ")).lower()
    return boat
#Gets the first position of the boat and makes sure it is valid

#player 1 placing first boat

display_grid(grid)
P1_Boat1a = (input("Player 1, Select boat position (a1 - e5): ")).lower()
P1_Boat1a = check_in(P1_Boat1a)

os.system('cls')
row, col = convert_input(P1_Boat1a) #gets the row and column to dtermine what segement of the grid list and where in the list to place the boat
grid[row][col] = 'X' #takes the boat position and places it in the grid list
display_grid(grid) #displays the grid list

P1_Boat1a, P1_Boat1b = pick_boat(P1_Boat1a, P1_Boat1b)

while not P1_Boat1b in Vaild_Position:
        P1_Boat1b = (input("Please enter a valid position: ")).lower()

os.system('cls')
row, col = convert_input(P1_Boat1b)
grid[row][col] = 'X'
display_grid(grid)

#player 1 placing second boat

P1_Boat2a = (input("Select position of second boat (a1 - e5): ")).lower()

P1_Boat2a = check_in(P1_Boat2a)
while P1_Boat2a == P1_Boat1a or P1_Boat2a == P1_Boat1b:
    P1_Boat2a = (input("That position is already in use. Please enter a valid position (a1 - e5): ")).lower()

os.system('cls')
row, col = convert_input(P1_Boat2a)
grid[row][col] = 'X'
display_grid(grid)

P1_Boat2a, P1_Boat2b = pick_boat2(P1_Boat2a, P1_Boat2b, P1_Boat1a, P1_Boat1b)

os.system('cls')
row, col = convert_input(P1_Boat2b)
grid[row][col] = 'X'
display_grid(grid)

print("Player 1 complete, pass to player 2\nPress any key to continue")
msvcrt.getch()

#player 2 placing first boat

os.system('cls') 

grid = []
for i in range(5):
    grid.append(['-' for i in range(5)])
display_grid(grid)
#resets the grid

P2_Boat1a = (input("Player 2, Select boat position (a1 - e5): ")).lower()
P2_Boat1a = check_in(P2_Boat1a)

os.system('cls')
row, col = convert_input(P2_Boat1a)
grid[row][col] = 'X'
display_grid(grid)

P2_Boat1a, P2_Boat1b = pick_boat(P2_Boat1a, P2_Boat1b)

while not P2_Boat1b in Vaild_Position:
    P2_Boat1b = (input("Please enter a valid position: ")).lower()
    
os.system('cls')
row, col = convert_input(P2_Boat1b)
grid[row][col] = 'X'
display_grid(grid)

#Player 2 placing second boat

P2_Boat2a = (input("Select position of second boat (a1 - e5): ")).lower()
P2_Boat2a = check_in(P2_Boat2a)
while P2_Boat2a == P2_Boat1a or P2_Boat2a == P2_Boat1b:
    P2_Boat2a = (input("That position is already in use. Please enter a valid position (a1 - e5): ")).lower()
    
os.system('cls')
row, col = convert_input(P2_Boat2a)
grid[row][col] = 'X'
display_grid(grid)

P2_Boat2a, P2_Boat2b = pick_boat2(P2_Boat2a, P2_Boat2b, P2_Boat1a, P2_Boat1b)

os.system('cls')
row, col = convert_input(P2_Boat2b)
grid[row][col] = 'X'
display_grid(grid)

os.system('cls' if os.name == 'nt' else 'clear') 
print("Player 2 complete")
Play = True

while Play:
    P1_Picka = input("Player 1, choose a position to shoot: ")
    while  P1_Picka in P1_Pickb:
        P1_Picka = input("You've already tired that, try again: ")
    P1_Picka = check_in(P1_Picka)
    P1_Pickb.append(P1_Picka)
    if P1_Picka == P2_Boat1a or P1_Picka == P2_Boat1b or P1_Picka == P2_Boat2a or P1_Picka == P2_Boat2b:
        print("Hit! Player 2's turn")
        P1_Score += 1
        if P1_Score == 4:
            Play = False
            print("Player 1 Wins!\n Good Job")
    else:
        print("Miss. Player 2's turn")
    P2_Picka = input("Player 2, choose a position to shoot: ")
    while  P2_Picka in P2_Pickb:
        P2_Picka = input("You've already tired that, try again: ")
    P2_Picka = check_in(P2_Picka)
    P2_Pickb.append(P2_Picka)
    if P2_Picka == P1_Boat1a or P2_Picka == P1_Boat1b or P2_Picka == P1_Boat2a or P2_Picka == P1_Boat2b:
        print("Hit! Player 1's turn")
        P2_Score += 1
        if P2_Score == 4:
            Play = False
            print("Player 2 Wins!\n Good Job")
    else:
        print("Miss. Player 1's turn")
