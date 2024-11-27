from turtle import Turtle, Screen
import random

screen=Screen()

screen.setup(width=500, height=400)
user_bet=screen.textinput(title="Make your bet", prompt="Which player will win the race? Enter a color")

colors=["red", "green", "blue", "yellow", "purple", "orange"]
players=[]
space_number=0

for colour in colors:
    turtle=Turtle(shape="circle")
    turtle.penup()
    turtle.color(colour)
    turtle.setpos(-230,-100 + space_number*40)
    players+=[turtle]
    space_number+=1

start_race=False

while user_bet not in colors :
    user_bet=screen.textinput(title="Make your bet", prompt="Which player will win the race? Enter a color")

start_race=True

while start_race :
    for player in players:
        player.forward(random.randint(0,10))
        
        if player.xcor()==250:
            start_race=False
            if user_bet == player.fillcolor():
                print(f"You've won! The {player.fillcolor()} is the winner!")
            else:
                 print(f"You've lost! The {player.fillcolor()} is the winner!")

screen.exitonclick()