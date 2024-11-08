import random


options = ("rock","paper","scissors")

running = True

while running:

    player= None
    computer = random.choice(options)

    while player not in options:
            player = input("Enter a choice(rock,paper,scissors): ")

    print(f"Player: {player}")
    print(f"computer:{computer}")

    if player == computer:
        print("It's a tie")
    elif player == "rock" and computer == "scissors":
        print("You Win!")
    elif player == "paper" and computer == "rock":
        print("You Win!")
    elif player == "Scissors" and computer == "paper":
        print("You Win!")
    else:
        print("You lose!")

    if not input("Play again? (y/n): ").lower() == "y":
        running = False

print("Thanks for playing!")
