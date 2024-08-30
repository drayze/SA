#Sarcasm Empire
#Providing a battle field for a war of words


#-------------------------------/////////////////////////////--------------------------------------------
#############  LEVEL TWO  ########################


#get Random
import random

Response = ["I'm rubber you're glue. What you say bounces off me and sticks to you.", "I know you are but what am I?", "Is that your face or your underwear?",
            "That uni-brow keeps the Sun out of your eyes, doesn't it?", "Your so ugly, your parents got divorced.", "I hear your Momma calling!", 
            "You're just like your father, short in height and intellect.", "Was that it? Are a vegetable?", "Wait let me dumb it down for you.....DUMB-ASS.",
            "Is that your breath or did someone fart?", "WHAT!  ARE YOU CRYING? There's no crying in $h*t talking!", 
            "Well I was down at the store yesterday, and guess what I saw...YOur sister working the corner!", "Where did you go to school? The Prestigious Academy of Dumb as a Bag of Hammers?",
            ]

#opening header
print("\nWelcome to Level 2, Loser.\n==================\nPrepare for a war of words.\n---------------------\n")

scoreboard = 0

#Set True variable
#PlayGame = True
#Start loop
while True:
    
    print(f"Your Score: {scoreboard}")

#the function of the program
    first_try = input("\nYou know how this goes.\nOn with it, Dumb-ass\n:: ")

#check if first_try is a repeat
    if first_try in Response:
        print(f"HA! I've heard that before!\nYour Final Score is: {scoreboard}")
        break
        
#scoring model
    check_for_points = len(first_try)

    if check_for_points < 15:
        print(f"Your feeble attempt is too short\n")
        print(random.choice(Response))
        scoreboard -= 10
        print("You lose 10 points!\n")
        pass
        #print(f"Your Score: {scoreboard}")
    elif check_for_points >=16 and check_for_points <= 29:
        scoreboard += 10
        #print(f"Your Score: {scoreboard}")
    elif check_for_points >= 30:
        scoreboard += 15
        #print(f"Your Score: {scoreboard}")
        
#advancing the scoring model
    retest = first_try.lower()
    search_for_points = list(retest)
    
    for i in search_for_points:
        
        if i == "?":
            scoreboard += 12
        elif i == ",":
            scoreboard += 12
        elif i == ".":
            scoreboard += 12
        elif i == "'":
            scoreboard += 12
      
        
    print(f"Your Score: {scoreboard}")
    
#over the top response
    #for i in first_try:
        #print("You lose!\n")
        
    if "z" in first_try:
        print("YOU WIN, FUCKFACE!")
        break
    elif scoreboard >= 501:
        print("You have endured enough abuse to level up!\n")
        print(random.choice(Response))
        print(f"Your score is: {scoreboard}\nYOU WIN FOR NOW.....\n")
        break
    else:
        print(random.choice(Response))
        
    print(random.choice(Response))
    play_again = input("Want to try again? Y or N \n====================\n")
#Make play_again uppercase
    play_again = play_again.upper()
    #play_again = play_again + "."    
    
    if play_again == "N":
        print(f"Your Final Score: {scoreboard}")
        break
    
#return data
#print(first_try)
