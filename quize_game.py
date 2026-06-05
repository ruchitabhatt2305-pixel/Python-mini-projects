#Project 1: Quiz Game Objective
print("WELCOME TO THE QUIZ GAME!!")
score=0
#Q1
answer=input("1.WHAT IS THE CAPITAL OF INDIA?:").upper()
if answer=="NEW DELHI":
	score+=1

#Q2
answer=input("2.WHO IS THE KING OF JUNGLE?").upper()
if answer=="LION":
	score+=1

#Q3
answer=input("3.WHAT PLANET IS CLOSEST TO THE SUN?:").upper()
if answer=="MERCURY":
	score+=1

#Q4
answer=input("4.HOW MANY COLORS ARE THERE IN RAINBOW?:").upper()
if answer=="SEVEN":
	score+=1

#Q5
answer=input("5.WHAT IS THE EVEN PRIME NUMBER?:")
if answer=="2":
	score+=1

print("QUIZ COMPLETED.")
print("YOUR FINAL SCORE IS:",score,"/5")


	

	
