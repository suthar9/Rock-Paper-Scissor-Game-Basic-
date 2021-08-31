from random import randint

list = ["Rock", "Paper", "Scissor"]


computer = list[randint(0,2)]

player = False

while player == False:

    player = input ("Rock, Paper, Scissors?")

    if player == computer:
        print("tie game!")
    
    elif player == "Rock":
        if computer == "Paper":
            print ("You lose!" , computer, "covers rock!")
        else:
            print ("You win", player ,  "smashes scissors!")

    elif player == "Paper":
        if computer == "Scissor":
            print ("you lose!", computer ,"Cut Paper")
        else:  
            print("You win", player , "covers rock!")
    elif player == "Scissors":
        if computer == "Rock":
            print ("You lose!" , computer , "Smashes Scissors!")
        else:
            print("you win" , player, "Cuts Paper!")
    else:
        print("Not a valid input: Please input: Rock, Paper, Scissors!!")

    player = False
    computer = list[randint(0,2)]





    





