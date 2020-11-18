import turtle
import random
p_one=turtle.Turtle()
turtle.bgcolor("black")
p_one.color("green")
p_one.shape("turtle")
p_one.penup()
p_one.goto(-200,100)
p_two = p_one.clone()
p_two.color("red")
p_two.penup()
p_two.goto(-200,-100)
p_one.goto(300,60)
p_one.pendown()
p_one.circle(45)
p_one.penup()
p_one.goto(-200,100)
p_two.goto(300,-140)
p_two.pendown()
p_two.circle(45)
p_two.penup()
p_two.goto(-200,-100)
dice=[1,2,3,4,5,6]
for i in range(20):
	if p_one.pos()>=(300,100):
		print("Player 1 Wins !!!")
		break
	elif p_two.pos()>=(300,-100):
		print("Player 2 Wins !!!")
		break
	else:
		p_one_turn=input("Press 'Enter' to roll the dice :")
		dice_outcome=random.choice(dice)
		print("The result of the dice roll is : ",dice_outcome)
		print("No. of steps will be : ", 20*dice_outcome)
		p_one.fd(20*dice_outcome)
		p_two_turn=input("Press 'Enter' to roll the dice :")
		dice_outcome=random.choice(dice)
		print("The result of the dice roll is : ",dice_outcome)
		print("No. of steps will be : ", 20*dice_outcome)
		p_two.fd(20*dice_outcome)

