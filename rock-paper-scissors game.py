import random
Your_Score = 0
Computer_Score = 0


print("........WELCOME TO THIS GAME........")
print("....ROCK , PAPER , SCISSORS.....")
print("Type either 'rock' or 'paper' or 'scissors' to play game---")
print("If you want to leave this game enter exit.")



while True:

    user_input = input("Enter Your Choice: ").lower()
    if user_input == 'exit':
        break

    if user_input not in ['rock', 'paper', 'scissors']:
        print("Invalid!,Your choice is invalid,Please choose 'rock', 'paper', or 'scissors'.")
        continue

    computer_thinks = random.choice(['rock', 'paper', 'scissors'])


    if user_input == computer_thinks:
        result = "tie"
    elif (user_input == 'rock' and computer_thinks == 'scissors') or \
         (user_input == 'scissors' and computer_thinks == 'paper') or \
         (user_input == 'paper' and computer_thinks == 'rock'):
        result = "user"
    else:
        result = "computer"

    print("Your choice is: ",user_input)
    print("Computer choice is: ",computer_thinks)
    if result=='tie':
        print("The game is tie!")
    elif result=='user':
        print("You win the game.")
        Your_Score += 1
    else:
        print("sorry!,You lose the game.")
        Computer_Score += 1

    print("Scores - Your: ",Your_Score )
    print("Score - Computer: ",Computer_Score)

    play_again = input("Do you want to play again? (yes/no): ").lower()
    if play_again != 'yes':
        break

print("Thak you for play the GAME!")
print("Final Score - Your Score: ",Your_Score )
print( "Computer Score: ",Computer_Score)

        

    

