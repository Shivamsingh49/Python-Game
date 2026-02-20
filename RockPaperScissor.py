# Rock Paper Scissor
import random 

def check(comp, user):
    if (comp == user):
        return 0
    if(comp == 0 and user == 1):
        return -1
    if(comp == 1 and user == 2):
        return -1
    if(comp == 2 and user == 0):
        return -1
    return 1
        

comp = random.randint(0, 2)
user = int(input("Choose 0 for Rock, 1 for Paper and 2 for Scissor: "))

score = check(comp, user)

print("You ", user)
print("Computer: ", comp)

if(score == 0):
    print("Its Draw")
elif(score == -1):
    print("You loss")
elif(score == 1):
    print("You win")



# Another method to print this game
import random

def game():
    choices = ['r', 'p', 's']  # r = Rock, p = Paper, s = Scissor
    user = input("Choose Rock (r), Paper (p), or Scissor (s): ").lower()
    computer = random.choice(choices)

    print(f"You chose: {user}")
    print(f"Computer chose: {computer}")

    if user == computer:
        print("It's a tie!")
    elif (user == 'r' and computer == 's') or \
         (user == 'p' and computer == 'r') or \
         (user == 's' and computer == 'p'):
        print("You win!")
    else:
        print("Computer wins!")

# Run the game
game()
