import random
options=("rock","paper","scissors")
running= True
while running:
    player_choice=None
    system_choice=random.choice(options)
    while player_choice not in options:
        player_choice=input("enter a choice(rock,paper,scissors):")
    print(f"player_choice:{player_choice}")
    print(f"system_choice:{system_choice}")
    if system_choice==player_choice:
        print("it's a tie.")
    elif system_choice=="scissors" and player_choice=="rock":
        print("you win.")
    elif system_choice=="rock" and player_choice=="paper":
        print("you win.")
    elif system_choice == "paper" and player_choice == "scissors":
        print("you win.")
    else:
        print("you lose.")
    play_again=input(" do you want to play again? (y/n):").lower()
    if play_again == ("n"):
        running=False
print("thanks for playing")

