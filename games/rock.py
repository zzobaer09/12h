# all import
from random import choice




# logic part
def logic(p , c):
    
    # tie logic
    if p == c:
      print("your choice: ", p)
      print("coumputer have: ", c)
      print("tie!!")
    else: 
        if p == "rock":
          if computer == "scissor":
            print("your choice: ", p)
            print("coumputer have: ", c)
            print("you win!!")
          else:
            print("your choice: ", p)
            print("coumputer have: ", c)
            print("you lose!!")
        elif p == "paper":
          if computer == "rock":
            print("your choice: ", p)
            print("coumputer have: ", c)
            print("you win!!")
          else:
            print("your choice: ", p)
            print("coumputer have: ", c)
            print("you lose!!")
        elif p == "scissor":
          if computer == "paper":
            print("your choice: ", p)
            print("coumputer have: ", c)
            print("you win!!")
          else:
            print("your choice: ", p)
            print("coumputer have: ", c)
            print("you lose!!")



while True:
    # variables
    choices = ["rock" , "paper", "scissor"]
    player = None

    # choice innit
    computer = choice(choices)
    # print(computer)


    # get input 
    while player not in choices:
        player = input("rock , paper  , scissor??: ")
        logic(player, computer)

    play_again = input("wann play again?? [y/n]: ")
    if play_again != "y":
        break
