import random
guess = ["ROCK","PAPER","SCISSOR"]
while True:
    Computer_Guess = random.choice(guess)
    Your_Choice = input(str("Enter what you choose (ROCK,PAPER,SCISSOR) ,Q to quit :- ")).upper()
    if(Your_Choice=="Q"):
        print("Thanks for playing , Good bye....")
        break
    if(Computer_Guess==Your_Choice):
        print("You both coose the same...")
        print("Draw")
    elif(Computer_Guess=="ROCK" and Your_Choice=="PAPER"):
        print("computer choice is :- Rock")
        print ("YOU WIN.......")
    elif(Computer_Guess=="ROCK" and Your_Choice=="SCISSOR"):
        print("computer choice is :- Rock")
        print ("YOU LOOSE.......")
    elif(Computer_Guess=="PAPER" and Your_Choice=="ROCK"):
        print("computer choice is :- PAPER")
        print ("YOU LOOSE.......")   
    elif(Computer_Guess=="PAPER" and Your_Choice=="SCISSOR"):
        print("computer choice is :- PAPER")
        print ("YOU WIN.......")  
    elif(Computer_Guess=="SCISSOR" and Your_Choice=="PAPER"):
        print("computer choice is :- SCISSOR")
        print ("YOU LOOSE.......")   
    elif(Computer_Guess=="SCISSOR" and Your_Choice=="ROCK"):
        print("computer choice is :- SCISSOR")
        print ("YOU Win.......")   
    else:
        print("Invalid input....")  
                  
    
