# -*- coding: utf-8 -*-
"""
Created on Tue Feb 20 01:15:04 2024

@author: antho
"welcome to coding"
- "if you made any comments please do so by ending the comment with
(intial)" for example:
"""
#moduels 
import numpy as np
import matplotlib.pyplot as plt
import sys 
from matplotlib import colors

# other files
import mainmap
import enemyarmy as ea

#field variables:
gamemap = mainmap.game_map
#class
class text:
    def __init__(self, message):
        self.message = message
#Constant
a = 11

#lists 

#arrays 
# arrayy(infantry, archers, cavalry, general, arty)
user_army = np.array([[0],
                     [0],
                     [0],
                     [0],
                     [0]])

#Creates individul cohort in np.array 
cohort_num = 0
user_cohort = np.zeros((cohort_num,7), dtype = int)

#array for enemy army
enemy_army = np.array([[0],
                     [0],
                     [0],
                     [0],
                     [0]])

#objects
display_text = text("start game?") #text

#colormap. Based on the number on the mainmap array, paint the color of the tiles
#0 = grass(green)
#1-5 = friendly troops (cyan)
#6-10 = enemy (red)
cmap = colors.ListedColormap(['green','cyan', 'cyan', 'cyan', 'cyan', 'cyan','red', 'red', 'red', 'red', 'red'])


#unit creation
#in the array [Movement,HP,Attack range, Attack damage, morale ]

    #creation of infantry
infantry = np.array([2,10,1,1,10])
        
    #creation of arhcers
archers = np.array([3,5,3,1,5])
    
    #creation of cavalry
cavalry = np.array([4,10,1,3,15])
    
    #creation of general
general = np.array([4,15,1,2,10]) #same movement as cavalary
    
    #creation of artillery
arty = np.array([1,5,5,5,5])

#Unit list
#stores the units and their stats in to an array, used for movement and combat
unit_list = np.array([infantry,
                     archers, 
                     cavalry, 
                     general, 
                     arty])



#player selects thier units
def unit_selection(infantry, archers, cavalry, general, arty):
    
    #displays unit information
    print('-'*50, "\nYou have a maximum of 10 units plus a general!\nThe Stats for each unit are sorted accordingly: --> [Movement,Health Pits ,Attack Range, Attack damage, Morale ]",'-'*50)
    
    print("1. Infantry:", infantry)
    print("2. Archers:", archers)
    print("3. Cavalry:", cavalry)
    print("4. Artillery:", arty)
        #Since you add a general automatically I removed this so that the player doesn't add in an extra
        
        #user picks units
    for i in range(0,5):
        choice = int(input(f"\nYou are chosing your unit {i+1}.\nEnter the corresponding number for the unit you want:"))
        #I change it into ints own function so that i can make the error check easier
        unitpick(choice)

        #user_army adds a general
    user_army[4] = user_army[4]+1
        
        # This is where the user gets to see the army they picked
        
    showarmy()
        
    print("Are you done making your army?")
    choice = check()
    if choice == True:
        unit_placement()
    elif choice == False and i == 9: #this will check if they have the total number of units or not
        input("You already have the maximum amount of units.")
        #sends player to a place where they can delete units 
    else:
            #currently not working (A)
        np.delete(user_army, 1)

def unitpick(choice):
    if choice == 1:
        user_army[0] = user_army[0]+1

    elif choice == 2:
        user_army[1] = user_army[1]+1
        
    elif choice == 3:
        user_army[2] = user_army[2]+1
        
    elif choice == 4:
        user_army[3] = user_army[3]+1
    else:
        input("that is not a valid unit number...\nPress any button to try again...")
        user_army[0] = [0]
        user_army[1] = [0]
        user_army[2] = [0]
        user_army[3] = [0]
        #sets the users army back to zero and sends them back to unit selection
        unit_selection(infantry, archers, cavalry, general, arty)

#unit placement(A)
def unit_placement():
    
    #prompts the user to select the dimension of a portion of their army (axb), 
    #then asks to user to pick a tiles representing the top left corner of that
    # army, then draw. 
    
    #user picks units
           
    choice_type = int(input("\nWhat unit would you like to place?.\nEnter the corresponding unit class number you want: "))
                                    #checks if the player has units of that type left to be placed
    if choice_type == 1 and user_army[choice_type-1][0] > 0:
        armysize(choice_type)
    
    elif choice_type == 2 and user_army[choice_type-1][0] > 0:
        armysize(choice_type)
                
    elif choice_type == 3 and user_army[choice_type-1][0] > 0:
        armysize(choice_type)
                
    elif choice_type == 4 and user_army[choice_type-1][0] > 0:
        armysize(choice_type)
                
    elif choice_type == 5 and user_army[choice_type-1][0] > 0:
        armysize(choice_type)
        
    else:
        print("You no longer have that unit avliable in your reserves.\nPress any button to place another unit...")
        unit_placement()

    



#army size
def armysize(choice_type):
    
    print("Here you will place your units. \nAll units are in a square formation. \nTo create a Formation, pick how long it will be (Rows) and how deep (columns).\nThe max rows you can place is 24 and the max columns you can place is 49")
                
    number_rows = int(input("please input a number representing how many rows you want to put down: "))
            
    number_columns = int(input("please input a number representing how many column you want to put down: "))
            
    number_rowlocation = int(input("please input a number representing the row of the top left location of that group: "))
            
    number_columnlocation = int(input("please input a number representing the column of the top left location of that group: "))
            
    #checks if the amount of units can be put into the the players wanted formation
    if number_rows*number_columns > user_army[choice_type-1][0]:
        input("You don't have enough units for this formation.\nPress any button to try again...")
        unit_placement()
                
        #Checks if the number of rows and columns are within the limit
    elif (number_rows <= 24 and number_rows > 0) and (number_columns <= 49 and number_columns > 0):
        if(number_rows*number_columns <= user_army[choice_type-1][0]):
            for i in range(number_rows):
                for j in range(number_columns):
                    gamemap[50-number_rowlocation-i][number_columnlocation-j] = choice_type
                    
            #adds this squadron of army into a source cohort_num as an instance variable
            global cohort_num 
            global user_cohort
            cohort_num += 1
            user_cohort = np.resize(user_cohort, (cohort_num,7))
            user_cohort[cohort_num-1][0] = cohort_num
            user_cohort[cohort_num-1][1] = choice_type
            user_cohort[cohort_num-1][2] = number_rowlocation
            user_cohort[cohort_num-1][3] = number_columnlocation
            user_cohort[cohort_num-1][4] = number_rows
            user_cohort[cohort_num-1][5] = number_columns
            user_cohort[cohort_num-1][6] = unit_list[choice_type-1,0]
        
    user_army[choice_type-1][0] = user_army[choice_type-1][0] - number_rows*number_columns
    mapdraw()
    showarmy()
        
    #if the user continues to place an army this will check if he has any troops left
    if user_army[0][0] == 0 and user_army[1][0] == 0 and user_army[2][0] == 0 and user_army[3][0] == 0 and user_army[4][0] == 0:
        nomore_units = True
    else:
        nomore_units = False
    
    print("Would you like to continue placing your Army?")
    answer = check() 
    if answer == True and nomore_units == True:
        #no more units to place moves to 
        print("You have no more units left to place. You will now be sent to the battle field") #temporary
    
    elif answer == True and nomore_units == False:
        unit_placement()
        
    elif answer == False and nomore_units == False:
        #you still have units to place
        print("You still have units to place")#temporary
        unit_placement()
    
    elif answer == False and nomore_units == True:
        #goes to battle field
        print("\033[H\033[J")#clears the console
        print("Welcome to the battle field! \nYour army has been prepared General!\nEach cohort will be represented by their " 
                ,"\n[cohort number, type, left top row, left top colomun, length, width, movement point]\n")
        gameplay()

    
    
#Gameplay, where the player makes all the important decisions on where the move the unit, and how the enemy ai moves
def gameplay():
    
    print(user_cohort)
    cohort_selection = int(input("\nSelect a cohort (The first number on the matrix) with movements left (last number on the matrix)"))
    if(user_cohort[cohort_selection-1][6] != 0):
        
        input_movement = int(input(f"select movement amount, this cohort has {user_cohort[cohort_selection-1][6]} left: "))
        input_direction = str(input("which direction shall this cohort move: up, down, left, right?: "))

        if(input_direction == "up"):
            movement = user_cohort[cohort_selection-1][2]+input_movement
            tile_movement(cohort_selection,movement,input_direction)
            
        elif(input_direction == "down"):
            movement = user_cohort[cohort_selection-1][2]-input_movement
            tile_movement(cohort_selection,movement,input_direction)
            
        elif(input_direction == "left"):
            movement = user_cohort[cohort_selection-1][3]-input_movement
            tile_movement(cohort_selection,movement,input_direction)
            
        elif(input_direction == "right"):
            movement = user_cohort[cohort_selection-1][3]+input_movement
            tile_movement(cohort_selection,movement,input_direction)
        
        user_cohort[cohort_selection-1][6] = user_cohort[cohort_selection-1][6] - input_movement
        
        print("Do you want to continue to move your cohorts?")
        more_movement = check()
        if more_movement == True:
            gameplay()
        else:
            reset_movement(cohort_selection)
            
            global a
            a = ea.enemy_tile_movement(enemy_army, gamemap, a)
            mapdraw()
            gameplay()
            
    elif(user_cohort[cohort_selection-1][6] == 0):
        print("\n this cohort is out of moves, please select another cohort")
        gameplay()


# a sequence of if statements and loops. First remove the friendly units on the map, and based on the direction and 
#movement speed, repaind the map
def tile_movement(cohort_selection,movement,input_direction):
    
    #change all units tile back to grass or terrain
    for i in range(user_cohort[cohort_selection-1][4]):
        for j in range(user_cohort[cohort_selection-1][5]):
            gamemap[50-user_cohort[cohort_selection-1][2]-i][user_cohort[cohort_selection-1][3]-j] = 0

    #reimplement units onto gamemap with movement
    if(input_direction == "up"):
        for i in range(user_cohort[cohort_selection-1][4]):
            for j in range(user_cohort[cohort_selection-1][5]):
                gamemap[50-movement-i][user_cohort[cohort_selection-1][3]-j] = user_cohort[cohort_selection-1][1] 
                
        user_cohort[cohort_selection-1][2] = movement
        
    elif(input_direction == "down"):
        for i in range(user_cohort[cohort_selection-1][4]):
            for j in range(user_cohort[cohort_selection-1][5]):
                gamemap[50-movement-i][user_cohort[cohort_selection-1][3]-j] = user_cohort[cohort_selection-1][1]
                
        user_cohort[cohort_selection-1][2] = movement
        
    elif(input_direction == "right"):
        for i in range(user_cohort[cohort_selection-1][4]):
            for j in range(user_cohort[cohort_selection-1][5]):
                gamemap[50-user_cohort[cohort_selection-1][2]-i][movement-j] = user_cohort[cohort_selection-1][1]
        user_cohort[cohort_selection-1][3] = movement
    else:
        for i in range(user_cohort[cohort_selection-1][4]):
            for j in range(user_cohort[cohort_selection-1][5]):
                gamemap[50-user_cohort[cohort_selection-1][2]-i][movement-j] = user_cohort[cohort_selection-1][1]
                
        user_cohort[cohort_selection-1][3] = movement
        
    mapdraw()
    #update(cohort_selection,movement,input_direction)    
    

#reset the movements for all cohort on the board
def reset_movement(cohort_selection):
    print(len(user_cohort))
    for i in range (len(user_cohort)):
        user_cohort[i][6] = unit_list[user_cohort[i][1]-1][0]

"""
def update(cohort_selection,movement,input_direction):
    
    #for later purposes when updating the formation of the army after battle
    #user_cohort[cohort_selection-1][4] = number_rows
    #user_cohort[cohort_selection-1][5] = number_columns
"""


def message(message):
    print(message)
    

#draws the current map (A)
#This is the function that will be accessed frequently to refresh game map
def mapdraw():
    #Creats a figure of the axes object (A)
    fig, ax = plt.subplots(figsize=(20,20))
    
    #use cmp object to draw the map of the game(A)
    plt.pcolor(gamemap[::-1],cmap=cmap,edgecolors='black', linewidths=1)
    
    #draw army based on their assigned number
    #iterate the array (gamemap), then print out the number of that array onto each tile
    #!! for z 6-10, z-5 is applied just so that on the map it can be represented by numbers 1-5, but in reality they are 6-10. (enemy)
    for (i, j), z in np.ndenumerate(gamemap[::-1]): 
        if(z == 6 or z == 7 or z == 8 or z == 9 or z == 10):
            ax.text(j+(0.5), i+(0.5), '{}'.format(z-5), ha='center', va='center', size=12)
        elif(z == 1 or z == 2 or z == 3 or z == 4 or z == 5):
            ax.text(j+(0.5), i+(0.5), '{}'.format(z), ha='center', va='center', size=12)
        
    # Add text box(A)
    plt.text(25, 25, display_text.message, fontsize=22, ha='center', va='center', bbox=dict(facecolor='white', alpha=0.5))

    plt.show()




#function to show army we can use it wwhenever we awnt now
def showarmy():
    print("This is your army:" 
          ,"\nInfantry:",  user_army[0]
          ,"\nArchers:",   user_army[1]
          ,"\nCavalry:",   user_army[2]
          ,"\nArtillery:", user_army[3]
          ,"\ngeneral:",   user_army[4]
          )


#this is a check funtion just so we don't have to rewerite the same thing over and over again
#It will return true for yes and false for no so make sure you remeber this when you are using this function
def check():
    check = input("\nEnter y if yes      Enter n if no:\n")
    if check == 'y':
        answer = True #
        return answer
    elif check == 'n':
        answer = False
        return answer
    else:
        input("That is not a valid response...\nPress any button to continue...")
        check()


#Main Menu
def Game_menu():
    
    mapdraw()
    
    #enables user to press a button to move on from the menu, otherwise exit(A)
    print("Welcom to (insert name here). Would you like to play?")
    startgame = check()
    if startgame == True:
        display_text.message = None
        #These are the new functions to create the enemy army
        #To create the enemy army I made a new file for organization sake
        ea.enemy_selection(infantry, archers, cavalry, general, arty, enemy_army)
        ea.enemy_formation1(enemy_army, gamemap)
        mapdraw()
        ea.showarmy(enemy_army)
        
        unit_selection(infantry, archers, cavalry, general, arty)
    elif startgame == False:
        sys.exit("Exiting game")
        
Game_menu()
