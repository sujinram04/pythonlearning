print("Hello from VS Code!")
print("Hi \n" * 3) 

'''
make a rock paper scissors game
''' 
import random

user_choice = input("Enter rock, paper, or scissors: ").lower()
options = ["rock", "paper", "scissors"]
computer_choice = random.choice(options)

print(f"Computer chose: {computer_choice}")




