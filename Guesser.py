import random
The_NO = random.randint(1,5)
#### Random Number generated
success = False
Guess = input("Guess the number between (1-5)")
Guess = int(Guess)
if Guess == The_NO:
    print ("Woah, at first chance itself? this is great! Good job!")
    success == True
else:
    print("Oops you got that wrong\n try that again")
    Guess = input("Guess the number between (1-5)")
    Guess = int(Guess)
    if Guess == The_NO:
        print ("Woah, you made it! Good Job!")
        success == True
    else:
        print("you failed.. better luck next time")
        print("the number was",The_NO)
        
    
    

