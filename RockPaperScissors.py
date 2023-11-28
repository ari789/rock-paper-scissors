##This program demonstrates random numbers using a rock, paper, scissors game.

#imports
from random import randint
from colorama import Fore as Color, Style

#declare win counters
uWins = 0
cWins = 0
ties = 0

##This function calculates the winner of rock, paper, scissors
def winner(u, c):
  winner = 0
  if (u == c):
    print(Color.LIGHTYELLOW_EX + Style.BRIGHT + "\nIt's a tie!")
    winner = 0
  elif (u == 1 and c == 2):
    print(Color.RED + Style.BRIGHT + "\nPaper wraps rock, computer wins!")
    winner = 2
  elif (u == 2 and c == 1):
    print(Color.GREEN + Style.BRIGHT + "\nPaper wraps rock, user wins!")
    winner = 1
  elif (u == 1 and c == 3):
    print(Color.GREEN + Style.BRIGHT + "\nRock smashes scissors, user wins!")
    winner = 1
  elif (u == 3 and c == 1):
    print(Color.RED + Style.BRIGHT + "\nRock smashes scissors, computer wins!")
    winner = 2
  elif (u == 2 and c == 3):
    print(Color.RED + Style.BRIGHT + "Scissors cut paper, computer wins!")
    winner = 2
  elif (u == 3 and c == 2):
    print(Color.GREEN + Style.BRIGHT + "\nScissors cut paper, user wins!")
    winner = 1
  return winner


#gameplay
again = 'y'
while (again.lower() == 'y'):
  #print game instructions
  print(Style.BRIGHT + '''
**********************
Rock, Paper, Scissors!\n
1 = Rock
2 = Paper
3 = Scissors        
''' + Style.RESET_ALL)

  #get choices
  while True:
    i = input("Enter your choice: ")
    if (i == "1" or i == "2" or i == "3"):
      userChoice = int(i)
      break
    else:
      print('Oops! Invalid choice. Try again.')

  compChoice = randint(1, 3)

  #calulate wins
  result = winner(userChoice, compChoice)
  if (result == 0): ties += 1
  elif (result == 1): uWins += 1
  elif (result == 2): cWins += 1

  #print scoreboard
  print(Style.RESET_ALL + "\nTies: " + str(ties))
  print("User wins: " + str(uWins))
  print("Computer wins: " + str(cWins))

  #ask if continue
  again = str(input("\nPlay again? (y/n) "))

print("Bye!")
