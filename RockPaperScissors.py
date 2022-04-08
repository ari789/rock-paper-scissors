##This program demonstrates random numbers using a rock, paper, scissors game.

#imports
from random import randint

#declare win counters
uWins = 0
cWins = 0
ties = 0   

#print game instructions
print("Rock, Paper, Scissors!\n1 = Rock\n2 = Paper\n3 = Scissors\n")


##This function calculates the winner of rock, paper, scissors
def winner(u, c):
    winner = 0
    if(u == c):
        print("It's a tie!")
        winner = 0
    elif(u == 1 and c == 2):
        print("Paper wraps rock, computer wins!")
        winner = 2
    elif(u == 2 and c == 1):
        print("Paper wraps rock, user wins!")
        winner = 1
    elif(u == 1 and c == 3):
        print("Rock smashes scissors, user wins!")
        winner = 1
    elif(u == 3 and c == 1):
        print("Rock smashes scissors, computer wins!")
        winner = 2
    elif(u == 2 and c == 3):
        print("Scissors cut paper, computer wins!")
        winner = 2
    elif(u == 3 and c == 2):
        print("Scissors cut paper, user wins!")
        winner = 1
    return winner
 

#gameplay
again = 'y'
while(again.lower() == 'y'):
    #get choices
    userChoice = int(input("Enter your choice: "))
    compChoice = randint(1, 3)

    #calulate wins
    result = winner(userChoice, compChoice)
    if(result == 0): ties += 1
    elif(result == 1): uWins += 1
    elif(result == 2): cWins += 1

    #print scoreboard
    print("Ties: " + str(ties))
    print("User wins: " + str(uWins))
    print("Computer wins: " + str(cWins))

    #ask if continue
    again = str(input("\nPlay again? (y/n) "))

print("Bye!")
          
    
