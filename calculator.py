#Project 2: Calculator Application Objective
print("CALCULATOR APPLICATION!!")
while True: 
	print("1.ADDITION")
	print("2.SUBTRACTION")
	print("3.MULTIPLICATION")
	print("4.DIVISION")
	print("5.EXIT")
 		
	num1=float(input('ENTER YOUR FIRST NUMBER: '))
	num2=float(input('ENTER YOUR SECOND NUMBER: '))
	choice=int(input("ENTER YOUR CHOICE(1-5): "))
	
	if choice==1:
		print("RESULT(+): ",num1+num2)
	elif choice==2:
		print("RESULT(-): ",num1-num2)
	elif choice==3:
		print("RESULT(*): ",num1*num2)
	elif choice==4:
		if num2!=0:
			print("RESULT(/): ",num1/num2)
		else:
			print("DIVISION BY ZERO IS NOT POSSIBLE")
	elif choice==5:
		print("EXITING PROGRAM")
		break

	else: 
		print("INVALID CHOICE.CHOOSE FROM(1-5)")

