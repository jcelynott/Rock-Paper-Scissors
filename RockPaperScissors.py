
#File: RockPaperScissors.py
import random

#keep track of scores
playScore = 0
oppScore = 0

print("Welcome to rock, paper, scissors!\n")

#This function is called after every game to keep track of scores and ask the player if they want to play a new game
def Rematch():

    if playScore == 1:
        print("\nSo far, you have won ",playScore, "game, while The AI has won ",oppScore)
    
    else:
        print("\nSo far, you have won ",playScore, "games, while The AI has won ",oppScore)
    
    contGame = input("\nIf you wish to play again, type REMATCH. If you wish to exit, type EXIT.\n")

    contGame = contGame.upper()

    if contGame == "REMATCH":
        Game()
    elif contGame == "EXIT":
        print("Ta-ra human! :)")
    else:
        Rematch()       
    

#This function handles the actual mechanics of the game
def Game():
    
    global playScore
    global oppScore
    
    choiceOne = input("Please input: ROCK, PAPER, or SCISSORS\n")

    choiceOne = choiceOne.upper()

    choiceArray = ["ROCK", "PAPER", "SCISSORS"]

    if choiceOne not in choiceArray:
        print("That wasn't really any of the choices. Want to try again?")
        Game()
        
    else:
        opponentOne = random.choice(choiceArray)

        print("You chose:", choiceOne,"\nThe AI chose:", opponentOne)

        if choiceOne == opponentOne:
            print("\nThe game was a DRAW. Your objects impotently collide to no effect")
        else:
            
            if choiceOne == "ROCK":
                if opponentOne == "PAPER":
                    print("You LOSE. The AI crushes your ROCK with PAPER. Somehow...")
                    oppScore += 1
                elif opponentOne == "SCISSORS":
                    print("You WIN. You grind the scissors of The AI under your mighty ROCK.")
                    playScore += 1
            elif choiceOne == "PAPER":
                if opponentOne == "ROCK":
                    print("You WIN. You crush The AI's ROCK with your PAPER. Somehow...")
                    playScore += 1
                else:
                    print("You LOSE. The AI cuts your paper to ribbons")
                    oppScore += 1
            else:
                if opponentOne == "ROCK":
                    print("You LOSE. The AI grinds your scissors under its mighty ROCK")
                    oppScore +=1
                else:
                    print("You WIN. You cut The AI's PAPER to ribbons")
                    playScore += 1


         
        Rematch()                
            

Game()

