import turtle
import random
import os

s = turtle.getscreen()
turtle.bgcolor("#A3D0F0")
p1 = turtle.Turtle()
p2 = p1.clone()
die = [0,1,2,3,4,5,6]



p1.color("#00154F")
p1.shape("turtle")
p1.penup()
p1.goto(-300,100)

p2.color("#D5950C")
p2.shape("turtle")
p2.penup()
p2.goto(-300,-100)

p1.goto(300,60)
p1.pendown()
p1.circle(40)
p1.penup()
p1.goto(-300,100)
p2.goto(300,-140)
p2.pendown()
p2.circle(40)
p2.penup()
p2.goto(-300,-100)


player1_name = input("Enter Player1 name : ")
player2_name = input("Enter Player2 name : ")


for i in range(20):
     if p1.pos() >= (300,100):
             print("\n\n")
             print(player1_name + " Wins!")
             print("\n\n")
             break
     elif p2.pos() >= (300,-100):
             print("\n\n")
             print(player2_name + " Wins!")
             print("\n\n")
             break
     else:
             p1_turn = input(player1_name + " press 'Enter' to roll the die ")
             d1 = random.choice(die)
             die1 = d1
             print("The result of the die roll is: ")
             print(die1)
             print("The number of steps will be: ")
             print(20*die1)
             p1.fd(20*die1)

             
             p2_turn = input(player2_name + " press 'Enter' to roll the die ")
             d2 = random.choice(die)
             die2 = d2
             print("The result of the die roll is: ")
             print(die2)
             print("The number of steps will be: ")
             print(20*die2)
             p2.fd(20*die2)
             
             
os.system("pause")
