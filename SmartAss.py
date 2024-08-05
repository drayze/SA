#Sarcasm Empire
#Providing a battle field for a war of words

#get Random
import random

Response = ["I'm rubber you're glue. What you say bounces off me and sticks to you.", "I know you are but what am I?", "Is that your face or your underwear?",
            "That uni-brow keeps the Sun out of your eyes, doesn't it?", "Your so ugly, your parents got divorced.", "I hear your Momma calling!", 
            "You're just like your father, short in height and intellect.", "Was that it? Are a vegetable?", "Wait let me dumb it down for you.....DUMB-ASS.",
            "Is that your breath or did someone fart?"]

#opening header
print("\nWelcome to your demise, Loser.\n==================\nPrepare for a war of words.\n---------------------\n")

scoreboard = 0

while True:
    
    print(f"Your Score: {scoreboard}")

#the function of the program
    first_try = input("\nWell don't leave us waiting forever Genius. ")

#scoring model
    check_for_points = len(first_try)

    if check_for_points < 15:
        scoreboard += 3
        print(f"Your Score: {scoreboard}")
    elif check_for_points >=16 and check_for_points <= 29:
        scoreboard += 10
        print(f"Your Score: {scoreboard}")
    elif check_for_points >= 30:
        scoreboard += 20
        print(f"Your Score: {scoreboard}")
        
#over the top response
    #for i in first_try:
        #print("You lose!\n")
        
    if "z" in first_try:
        print("YOU WIN, FUCKFACE!")
        break
    else:
        print("YOU LOSE!\n")
        
    print(random.choice(Response))
    play_again = input("Want to try again? Y or N \n====================\n")
#Make play_again uppercase
    play_again = play_again.upper()    
    
    if play_again == "N":
        break
    
#return data
#print(first_try)
