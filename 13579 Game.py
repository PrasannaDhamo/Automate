import random

die = [1,3,5,7,9]
Player1_name = input("Enter Player1 name : ")
Player2_name = input("Enter Player2 name : ")

for x in range (35):
        input(Player1_name+" turn")
        d1 = random.choice(die)
        die1 = d1
        print(die1)
        input(Player2_name+" turn")
        d2 = random.choice(die)
        die2 = d2
        print(die2)
