# Rock, Paper, Scissorss!

import random

computer = random.randint(1, 3)

print("Choose your weapon!:")
print(" 1) Rock")
print(" 2) Paper")
print(" 3) Scissors")
print(" ")

player = int(input("(1) (2) (3)   "))

if player == 1 and computer == 3 or \
    player == 2 and computer == 1 or \
    player == 3 and computer == 2:
    print(" ")
    input("Player wins! 🙆‍♂️, press any key to close.")
elif player == 1 and computer == 2 or \
    player == 2 and computer == 3 or \
    player == 3 and computer == 1:
    print(" ")
    input("Computer wins! 🖥️, press 'Enter' key to close.")
else:
    input("It's a tie! 🤝, press 'Enter' key to close.")
