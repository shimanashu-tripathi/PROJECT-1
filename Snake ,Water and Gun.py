import random

# Generate computer choice: Snake (1), Water (-1), Gun (0)
computer = random.choice([1, -1, 0])

youstr = input("Enter your choice (snake, water, gun): ").strip().lower()

# Map user text input to numbers
youDict = {"snake": 1, "water": -1, "gun": 0}
reversedDict = {1: "snake", -1: "water", 0: "gun"}

if youstr not in youDict:
    print("Invalid choice! Please choose snake, water, or gun.")
else:
    you = youDict[youstr]

    print(f"You chose {reversedDict[you]} and computer chose {reversedDict[computer]}")

    if computer == you:
        print("It is a draw")
    else:
        # Winning conditions for 'you'
        if (computer == -1 and you == 1) or \
           (computer == 1 and you == 0) or \
           (computer == 0 and you == -1):
            print("You win!")
            import pyttsx3
            engine=pyttsx3.init()
            engine.say('''🎉 Congratulations! you defeated the Computer!
                            👍 Well played!
                            🤩 Amazing! You beat the computer as its own game.
                            🏆 Victory is yours!
                            🎉 Congratulations! You made the computer fear🤣😹 you!''')
            engine.runAndWait()
        else:
            print("You lose!")
            import pyttsx3
            engine=pyttsx3.init()
            if computer==you:
                print("It's draw!")
            elif (computer==-1 and you==1):
                (computer==1 and you==0)
                (computer==0 and you==-1)
                print("You win!")
               
            else:
                print("you lose!")
                engine.say('''😞Sorry, better luck next time!
                🤦Oops! Look like you need more practice!
                💔 Sorry human! The computer wins this time
                🤕Tough luck! The computer claimed victory over you.''' )
                engine.runAndWait()
                
                

            

           



            

            














        


            

            














        