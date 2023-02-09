#By : Joshua Hodder
#Date started : 2023-02-08
#A Two Player Game Of Battleship

import os

print("Welcome to battleship")
Vaild_Position = " "
P1_Boat1b = ""
P1_Boat2b = ""
P2_Boat1b = ""
P2_Boat2b = ""
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

def check_boat(boat):
    while len(boat) != 2:
        boat = (input("Please enter a valid position (a1 - e5): ")).lower()
    while not boat[0] in "abcde" or not boat[1] in "12345":
        boat = (input("Please enter a valid position (a1 - e5): ")).lower()
    return boat
#Gets the first position of the boat and makes sure it is valid

#player 1 placing first boat

P1_Boat1a = (input("Player 1, Select boat position (a1 - e5): ")).lower()
P1_Boat1a = check_boat(P1_Boat1a)
P1_Boat1a, P1_Boat1b = pick_boat(P1_Boat1a, P1_Boat1b)

while not P1_Boat1b in Vaild_Position:
        P1_Boat1b = (input("Please enter a valid position: ")).lower()

#player 1 placing second boat

P1_Boat2a = (input("Select position of second boat (a1 - e5): ")).lower()
P1_Boat2a = check_boat(P1_Boat2a)
while P1_Boat2a == P1_Boat1a or P1_Boat2a == P1_Boat1b:
    P1_Boat2a = (input("That position is already in use. Please enter a valid position (a1 - e5): ")).lower()

P1_Boat2a, P1_Boat2b = pick_boat2(P1_Boat2a, P1_Boat2b, P1_Boat1a, P1_Boat1b)

#player 2 placing first boat

os.system('cls' if os.name == 'nt' else 'clear') # i googled this, it clears the console
print("Player 1 complete, pass to player 2")

P2_Boat1a = (input("Player 2, Select boat position (a1 - e5): ")).lower()
P2_Boat1a = check_boat(P2_Boat1a)
P2_Boat1a, P2_Boat1b = pick_boat(P2_Boat1a, P2_Boat1b)

while not P2_Boat1b in Vaild_Position:
    P2_Boat1b = (input("Please enter a valid position: ")).lower()

#Player 2 placing second boat

P2_Boat2a = (input("Select position of second boat (a1 - e5): ")).lower()
P2_Boat2a = check_boat(P2_Boat2a)
while P2_Boat2a == P2_Boat1a or P2_Boat2a == P2_Boat1b:
    P2_Boat2a = (input("That position is already in use. Please enter a valid position (a1 - e5): ")).lower()

P2_Boat2a, P2_Boat2b = pick_boat2(P2_Boat2a, P2_Boat2b, P2_Boat1a, P2_Boat1b)

os.system('cls' if os.name == 'nt' else 'clear') 
print("Player 2 complete")