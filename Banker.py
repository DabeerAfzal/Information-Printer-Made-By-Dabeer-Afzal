import random

greeting_intro = ['Hello!', "Welcome!", "Hola!", "Hey!"]
greetings = random.choice(greeting_intro)
print(greetings + " What Type Of Information Do you want About our Client?")
	
while True:
	info = str(input())
	if "Name" in info:
		print("\nDabeer Afzal")

	elif "Age" in info:
		print("\n12")

	elif "Net Worth" in info:
		print("\n$1 Billion")

	elif "Credit Card" in info:
		print("\n0001-214123-7245")

	elif "Account Pin" in info:
		print("\n00021")
	
	elif "Quit" in info:
		print("\nOk Bye I Hope You Had A Great Time Using Me!")
		quit()

	else:
		print("\nSorry But We Dont Have That Kind Of Information! Please Try Again!\n")