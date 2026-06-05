#Project 3: Password Generator Objective
import random

print("WELCOME TO PASSWORD GENERATOR!")
length=int(input("ENTER THE LENGTH OF PASSWORD: "))

uppercase="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lowercase="abcdefghijklmnopqrstuvwxyz"
numbers="0123456789"
special="!@#$%^&*()_+-=[]{}|;:,.<>?/"

all_char=uppercase+lowercase+numbers+special

password=""
for i in range(length):
	password+=random.choice(all_char)

print("GENERATED PASSWORD: ",password)

