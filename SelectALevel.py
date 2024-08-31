#First page player sees. Prompt them to select a level

#Grab the player's level
usersLevel = input("\nWAR OF WORDS\n\nPlease choose your level: \n")

#Create function to play Level 1
import SmartAss

def L1():
    
    with open(SmartAss) as f:
        exec(f.read())
        
#Create function to play level 2
import SA_level2

def L2():
        
    with open(SA_level2) as f:
        exec(f.read())
        


#process user's level input
if usersLevel == 1:
    #move to file SmartAss.py
    #pass
    L1()
        
elif usersLevel == 2:
    #if scoreboard > 500:
        #move to SA_level2.py
        #pass
    
    L2()