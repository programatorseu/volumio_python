#Simple script
from sys import exit

def gold_room():
    print("room full of gold . How much do you take?")
    choice = input("> ")
    if "0" in choice or "1" in choice:
        how_much = int(choice)
    else:
        dead("Man, learn to type a number")    

def bear_room():
    print("There is a bear there")
    print("The bear has a bunch of honey") 
    print("The fat baer is in front of another door")
    print("How are you going to move the bear?")
    bear_moved = False

    while True:
        choice = input("> ")
        if choice == "take honey":
            dead("The Bear looks at you then slaps your face oof")
