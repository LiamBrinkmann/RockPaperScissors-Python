from random import randint # importing to get a random input for the computers move

Moves = ["Rock", "Paper", "Scissors"] # possible moves

Play = True #while loop prerequisite 

while Play == True:
    compMove = Moves[randint(0,2)]
    Play = False #Will stop the while from repeating if user does not select to play again.
    
    try: #exception handling, if user enters a non number then yea.
        #Asks for user input on which move and changes it into rock paper or scissors
        player = Moves[1-int(input("Please select a move: 1 for rock, 2 for paper, 3 for scissors\n"))]

        if player == compMove: # if both used the same move then draw
            print("It's a draw!")

        elif player == "Rock": #checks if comp beats the player or if player won
            if compMove == "Paper":
                print("Your rock was covered by some paper. You Lose")
            else:
                print("You crushed the scissors of your oponent. You Win")

        elif player == "Paper": #checks if comp beats the player or if player won
            if compMove == "Scissors":
                print("Your paper was cut. You Lose")
            else:
                print("You covered the rock. You Win")

        elif player == "Scissors": #checks if comp beats the player or if player won
            if compMove == "Rock":
                print("A rock destroyed your scissors. You Lose")
            else:
                print("You cut that paper to pieces. You Win")

        else: #user entered a invalid digit
            print("Incorrect input, please ensure you enter only 1,2 or 3 as your option")

        playAgain = input("Would you like to play again? Y/N\n") #if user wishes to play again it'll keep running the loop
        if playAgain == "Y" or playAgain == "y":
            Play = True
        else:
            print("See you again next time!")
    except:
        print("Incorrect input, please ensure you enter only 1,2 or 3 as your option")
        Play = True