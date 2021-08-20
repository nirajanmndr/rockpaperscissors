import random

user_wins = 0
computer_wins = 0
options = ["rock", "paper", "scissors"]

while True:
    user_input = input("Type Rock/Paper/Scissors or Q or Q to quit: ").lower()
    if user_input == "q": 
        break
    
    if user_input not in options:
        continue
    
    # Randomly choose an argument in the list options
    computer_pick = random.choice(options)

    print("Computer picked", computer_pick + ".")

    if user_input == "rock" and computer_pick == "scissors":
        print("You Won!")
        user_wins += 1
        continue

    elif user_input == "paper" and computer_pick == "rock":
        print("You Won!")
        user_wins += 1
        continue

    elif user_input == "scissors" and computer_pick == "rock":
        print("You Won!")
        user_wins += 1
        continue
    
    else:
        print("You lost!")
        computer_wins += 1
        continue

print("Number of times you won: ", user_wins)
print("Number of times computer won: ", computer_wins)


print("Goodbye!")
