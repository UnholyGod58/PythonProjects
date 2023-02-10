#By : Joshua Hodder
#Date started : 2023-02-08
#V.1.0 finsihed : 2023-02-09
#A Two Player Game Of Battleship

import os
import msvcrt
import random
os.system('cls')
Start_Try = False
Vaild_Position = " "

def display_grid(grid):
    print('  1 2 3 4 5')
    print('a ' + ' '.join(grid[0]))
    print('b ' + ' '.join(grid[1]))
    print('c ' + ' '.join(grid[2]))
    print('d ' + ' '.join(grid[3]))
    print('e ' + ' '.join(grid[4]))
#code for displaying the grid
def convert_input(input_string):
    row = ord(input_string[0].upper()) - 65 # converts letter to number for row  (A -> 0 B-> 1 C-> 2 D-> 3 E-> 4)
    col = int(input_string[1]) - 1 # gets column number from 0 to 4
    return row, col
#takes the input from the user and converts it to a row and column number
def Update_Grid(Position, Grid, Change):
    global grid
    os.system('cls')
    row, col = convert_input(Position) #gets the row and column to dtermine what segement of the grid list and where in the list to place the boat
    Grid[row][col] = Change #takes the boat position and places it in the grid list
    display_grid(Grid) #displays the grid list
#Updates the grid after user input
def Boat_Direction(boat, direction1, direction2):
    if boat[0] == "a":
        direction1 = "b"
    elif boat[0] == "e":
        direction1 = "d"
    elif boat[0] == "b":
        direction1 = "a"
        direction2 = "c"
    elif boat[0] == "c":
        direction1 = "b"
        direction2 = "d"
    elif boat[0] == "d":
        direction1 = "c"
        direction2 = "e"
    return direction1, direction2

def AI_Pick_Boat(Boata, Boatb):
    global Vaild_Position
    Direction1 = ""
    Direction2 = ""
    Position_1 = int(Boata[1]) - 1
    Position_2 = int(Boata[1]) + 1
    #Sets the second position of the boat part 1
    Direction1, Direction2 = Boat_Direction(Boata, Direction1, Direction2)
    if Boata[0] in "ae":
        if Boata[1] == "1":
            Vaild_Position = [f"{Direction1}1", f"{Boata[0]}2"]
        elif Boata[1] == "5":
            Vaild_Position = [f"{Direction1}5", f"{Boata[0]}4"]
        else:
            Vaild_Position = [f"{Boata[0]}{Position_1}", f"{Direction1}{Boata[1]}", f"{Boata[0]}{Position_2}"]
    else:
        if Boata[1] == "1":
            Vaild_Position = [f"{Direction1}1", f"{Boata[0]}2", f"{Direction2}1"]
        elif Boata[1] == "5":
            Vaild_Position = [f"{Direction1}5", f"{Boata[0]}4", f"{Direction2}5"]
        else:
            Vaild_Position = [f"{Direction1}{Boata[1]}", f"{Boata[0]}{Position_1}", f"{Direction2}{Boata[1]}", f"{Boata[0]}{Position_2}"]
    Boatb = Vaild_Position[random.randrange(0, len(Vaild_Position))]

    return Boatb
def pick_boat(Boata, Boatb):
    global Vaild_Position
    Direction1 = ""
    Direction2 = ""
    Position_1 = int(Boata[1]) - 1
    Position_2 = int(Boata[1]) + 1
    #Sets the second position of the boat part 1
    Direction1, Direction2 = Boat_Direction(Boata, Direction1, Direction2)
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
    return Boatb
#ensures that the first position of the boat is valid and stets up the second position of the boat
def pick_boat2(BoatA, BoatB, BoatA1, BoatB1):
    BoatB = pick_boat(BoatA, BoatB)
    while not BoatB in Vaild_Position:
        BoatB = (input("Please enter a valid position: ")).lower()
    while BoatB == BoatA1 or BoatB == BoatB1:
        BoatB = (input("That position is already in use. Please enter a valid position: ")).lower()
    return BoatB
#ensures that the second position of the boat is valid
def check_in(boat):
    while not (len(boat) == 2 and boat[0] in "abcde" and boat[1] in "12345"):
        boat = (input("Please enter a valid position (a1 - e5): ")).lower()
        if not boat:
            continue #Resets the loop
        if len(boat) != 2:
            continue
    return boat
#Ensures the imput is valid
def Boat_Place(Boat1a, Boat1b, Boat2a, Boat2b, player):
    grid = []
    for i in range(5):
        grid.append(['-' for i in range(5)])
    global Vaild_Position
    display_grid(grid)
    Boat1a = (input(f"Player{player}, Select boat position (a1 - e5): ")).lower()
    Boat1a = check_in(Boat1a)
    Update_Grid(Boat1a, grid, "X")
    Boat1b = pick_boat(Boat1a, Boat1b)
    while not Boat1b in Vaild_Position:
        Boat1b = (input("Please enter a valid position: ")).lower()
    Update_Grid(Boat1b, grid, "X")
    Boat2a = (input("Select position of second boat (a1 - e5): ")).lower()
    Boat2a = check_in(Boat2a)
    while Boat2a == Boat1a or Boat2a == Boat1b:
        Boat2a = (input("That position is already in use. Please enter a valid position (a1 - e5): ")).lower()
    Update_Grid(Boat2a, grid, "X")
    Boat2b = pick_boat2(Boat2a, Boat2b, Boat1a, Boat1b)
    Update_Grid(Boat2b, grid, "X")
    print(f"Player{player} complete\nPress any key to continue")
    msvcrt.getch()
    os.system('cls') 
    return Boat1a, Boat1b, Boat2a, Boat2b
#Allowes the player to pick the boat's position
def Player_Turn(grid, Score, B1a, B2a, B1b, B2b, Picka, Pickb, playerIt, playerNext):
    global Play
    
    display_grid(grid)
    Picka = input(f"Player {playerIt}, choose a position to shoot: ")
    while  Picka in Pickb:
        Picka = input("You've already tired that, try again: ")
    Picka = check_in(Picka)
    Pickb.append(Picka) # tracks geussed positions
    if Picka == B1a or Picka == B1b or Picka == B2a or Picka == B2b:
        Update_Grid(Picka, grid, "X")
        print(f"Hit! Player {playerNext}'s turn\npress any key to continue")
        Score += 1
        if Score == 4:
            os.system('cls')
            display_grid(grid)
            Play = False
            print(f"Player {playerIt} Wins!\n Good Job")
        msvcrt.getch()
        os.system('cls') 
    else:
        Update_Grid(Picka, grid, "O")
        print(f"Miss. Player {playerNext}'s turn\npress any key to continue")
        msvcrt.getch()
        os.system('cls') 
    return grid, Pickb, Score
#Player Gameplay
def Single_Player():
    Boat1a = ""
    Boat1b = ""
    Boat2a = ""
    Boat2b = ""
    AIB1a = ""
    AIB1b = ""
    AIB2a = ""
    AIB2b = ""
    PickA = ""
    AIPickA = ""
    PickB = []
    AIPickB = []
    AIHits = []
    Score = 0
    AIScore = 0
    global Play
    
    Boat1a, Boat1b, Boat2a, Boat2b = Boat_Place(Boat1a, Boat1b, Boat2a, Boat2b, "")
    
    AIB1a = random.choice("abcde") + str(random.randrange(1,5))
    AIB1b = AI_Pick_Boat(AIB1a, AIB1b)
    AIB2a = random.choice("abcde") + str(random.randrange(1,5))
    while AIB2a == AIB1a or AIB2a == AIB1b:
        AIB2a = random.choice("abcde") + str(random.randrange(1,5))
    AIB2b = AI_Pick_Boat(AIB2a, AIB2b)
    while AIB2b == AIB1a or AIB2b == AIB1b:
        AIB2b = AI_Pick_Boat(AIB2a, AIB2b)
        
    gridP = []
    for i in range(5):
        gridP.append(['-' for i in range(5)])
    gridAI = []
    for i in range(5):
        gridAI.append(['-' for i in range(5)])
        
    Play = True
        
    while Play:
        gridP, PickB, Score = Player_Turn(gridP, Score, Boat1a, Boat1b, Boat2a, Boat2b, PickA, PickB, "", "AI")
        if Play:
            if len(AIHits) > 0:
                AIPickA = AI_Pick_Boat(AIHits[-1], AIPickA)
            if len(AIHits) == 1 or len(AIHits) == 3 and not all(item in AIPickB for item in Vaild_Position):
                while AIPickA in AIPickB:
                    AIPickA = Vaild_Position[random.randrange(0, len(Vaild_Position))]
                if not AIPickA in AIPickB:
                    AIPickB.append(AIPickA)
            else:
                AIPickA = random.choice("abcde") + str(random.randrange(1,5))
                while AIPickA in AIPickB:
                    AIPickA = random.choice("abcde") + str(random.randrange(1,5))
                AIPickB.append(AIPickA)
            if AIPickA == Boat1a or AIPickA == Boat1b or AIPickA == Boat2a or AIPickA == Boat2b:
                AIHits.append(AIPickA)
                Update_Grid(AIPickA, gridAI, "X")
                AIScore += 1
                print("AI Hit\nPress any key to continue")
                msvcrt.getch()
                os.system('cls')
            else:
                Update_Grid(AIPickA, gridAI, "O")
                print("AI Missed\nPress any key to continue")
                msvcrt.getch()
                os.system('cls')
            if AIScore == 4:
                display_grid(gridAI)
                print("AI Wins!\nPress any key to continue")
                Play = False
                msvcrt.getch()
                os.system('cls')
    while not Play:
        Exit = input("Would you like to restart [y/n]: ").lower()
        if Exit == "y":
            start()
        elif Exit == "n":
            print("Thanks for playing!\nPress any key to exit")
            msvcrt.getch()
            exit()
        else:
            print("Please enter 'y' or 'n'\nPress any key to try again")
            msvcrt.getch               
def Multi_Player():
    P1_Boat1a = ""
    P1_Boat2a = " "
    P1_Boat1b = ""
    P1_Boat2b = ""
    P2_Boat1a = ""
    P2_Boat2a = ""
    P2_Boat1b = ""
    P2_Boat2b = ""
    P1_Picka = ""
    P2_Picka = ""
    P1_Pickb = []
    P2_Pickb = []
    P1_Score = 0
    P2_Score = 0
    global Play
    
    P1_Boat1a, P1_Boat1b, P1_Boat2a, P1_Boat2b = Boat_Place(P1_Boat1a, P1_Boat1b, P1_Boat2a, P1_Boat2b, 1)
    P2_Boat1a, P2_Boat1b, P2_Boat2a, P2_Boat2b = Boat_Place(P2_Boat1a, P2_Boat1b, P2_Boat2a, P2_Boat2b, 2)
               
    gridP1 = []
    for i in range(5):
        gridP1.append(['-' for i in range(5)])
    gridP2 = []
    for i in range(5):
        gridP2.append(['-' for i in range(5)])
        
    Play = True

    while Play:
        gridP1, P1_Pickb, P1_Score = Player_Turn(gridP1, P1_Score, P2_Boat1a, P2_Boat2a, P2_Boat1b, P2_Boat2b, P1_Picka, P1_Pickb, 1, 2)
        if Play:
            gridP2, P2_Pickb, p2_Score = Player_Turn(gridP2, P2_Score, P1_Boat1a, P1_Boat2a, P1_Boat1b, P1_Boat2b, P2_Picka, P2_Pickb, 2, 1)
    
    while not Play:
        Input = input("Would you like to restart [y/n]\n").lower
        if Input == "y":
            start()
        elif Input == "n":
            print("Thanks for playing!\nPress any key to exit")
            msvcrt.getch()
            exit()
        else:
            print("Please enter 'y' or 'n'\nPress any key to try again")
            msvcrt.getch()

#Code for Two Player Version
def start():
    os.system('cls')
    global Start_Try
    if Start_Try:
        print("Enter 1 to play with AI\nEnter 2 to play with another player")
    else:
        print("Welcome to battleship\nEnter 1 to play with AI\nEnter 2 to play with another player")
    try:
        Mode_Select = int(input())
    except ValueError:
        print("Invalid input\nPress any key to continue and try again")
        Start_Try = True
        msvcrt.getch()
        os.system('cls')
        start()
    if Mode_Select == 1:
        print("Welcome")
        os.system('cls')
        print("Playing with AI\nPress any key to continue")
        msvcrt.getch()
        os.system('cls')
        Single_Player()
    elif Mode_Select == 2:
        os.system('cls')
        print("Playing with another player\nPress any key to continue")
        msvcrt.getch()
        os.system('cls')
        Multi_Player()
    else:
        print("Invalid input\nPress any key to continue and try again")
        Start_Try = True
        msvcrt.getch()
        os.system('cls')
        start()
#Code for Starting the Game
start()