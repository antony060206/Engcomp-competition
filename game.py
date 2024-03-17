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

#field variables:
gamemap = mainmap.game_map
#class
class text:
    def __init__(self, message):
        self.message = message

#lists 

#arrays 
# arrayy(infantry, archers, cavalry, general, arty)
user_army = np.array([[0],
                     [0],
                     [0],
                     [0],
                     [0]])

#objects
display_text = text("start game?") #text

#colormap. Based on the number on the mainmap array, paint the color of the tiles
#0 = grass(green)
#1-5 = friendly troops (cyan)
#6 = river (blue)
cmap = colors.ListedColormap(['green','cyan', 'cyan', 'cyan', 'cyan', 'cyan','blue'])


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





#player selects thier units
def unit_selection(infantry, archers, cavalry, general, arty):
    
    #displays unit information
    print('-'*50, "\nYou have a maximum of 10 units plus a general!\nThe Stats for each unit are sorted accordingly: --> [Movement,Health Pits ,Attack Range, Attack damage, Morale ]",'-'*50)
    picking = 1
    
    while picking != 'y':
        
        print("1. Infantry:", infantry)
        print("2. Archers:", archers)
        print("3. Cavalry:", cavalry)
        print("4. Artillery:", arty)
        print("5. general:", general)
        
        #user picks units
        for i in range(0,10):
            choice = int(input(f"\nYou are chosing your unit {i+1}.\nEnter the corresponding number for the unit you want:"))

            if choice == 1:
                user_army[0] = user_army[0]+1

            elif choice == 2:
                user_army[1] = user_army[1]+1
                
            elif choice == 3:
                user_army[2] = user_army[2]+1
                
            elif choice == 4:
                user_army[3] = user_army[3]+1
            
        #user_army adds a general
        user_army[4] = user_army[4]+1
        
        # This is where the user gets to see the army they picked
        
        print("This is your army:" 
              ,"\nInfantry:",  user_army[0]
              ,"\nArchers:",   user_army[1]
              ,"\nCavalry:",   user_army[2]
              ,"\nArtillery:", user_army[3]
              ,"\ngeneral:",   user_army[4]
              )
        
        
        choice = input("If you are done selecting your army press y:")
        if choice == 'y':
            unit_placement()
            picking = 'y'
            break
        else:
            #currently not working (A)
            np.delete(user_army, 1)
                



#unit placement(A)
def unit_placement():
    
    #prompts the user to select the dimension of a portion of their army (axb), 
    #then asks to user to pick a tiles representing the top left corner of that
    # army, then draw. 
    
    #user picks units
    while True: 
        for i in range(0,10):
            
            #if no troops left to place down exit
            if(sum(user_army) == 0): 
               break
           
            choice_type = int(input("\nYou are chosing your unit you have.\nEnter the corresponding unit class number you want: "))
            
            if choice_type == 1:
                armysize(choice_type)
    
            elif choice_type == 2:
                armysize(choice_type)
                
            elif choice_type == 3:
                armysize(choice_type)
                
            elif choice_type == 4:
                armysize(choice_type)
                
            elif choice_type == 5:
                armysize(choice_type)
                
        print("all done")
        break
    




#army size
def armysize(choice_type):
    #make a condition so that the player can only pick between row 1-24, coloum 1-49 (the the square has to be within boundry) as well as within troops amount
    number_rows = int(input("please input a number representing how many rows you want to put down: "))
    
    number_columns = int(input("please input a number representing how many column you want to put down: "))
    
    number_rowlocation = int(input("please input a number representing the row of the top left location of that group: "))
    
    number_columnlocation = int(input("please input a number representing the column of the top left location of that group: "))
    
    if(number_rows*number_columns <= user_army[choice_type-1][0]):
        for i in range(number_rows):
            for j in range(number_columns):
                gamemap[50-number_rowlocation-i][number_columnlocation-j] = choice_type
    mapdraw()
    user_army[choice_type-1][0] = user_army[choice_type-1][0] - number_rows*number_columns
    print("This is your army reserve:" 
          ,"\nInfantry:",  user_army[0]
          ,"\nArchers:",   user_army[1]
          ,"\nCavalry:",   user_army[2]
          ,"\nArtillery:", user_army[3]
          ,"\ngeneral:",   user_army[4]
          )
    
    




#draws the current map (A)
#This is the function that will be accessed frequently to refresh game map
def mapdraw():
    #Creats a figure of the axes object (A)
    fig, ax = plt.subplots(figsize=(20,20))
    
    #use cmp object to draw the map of the game(A)
    plt.pcolor(gamemap[::-1],cmap=cmap,edgecolors='black', linewidths=1)
    
    #draw army based on their assigned number
    #iterate the array (gamemap), then print out the number of that array onto each tile
    for (i, j), z in np.ndenumerate(gamemap[::-1]): 
        if(z != 0 and z!= 6):
            ax.text(j+(0.5), i+(0.5), '{}'.format(z), ha='center', va='center', size=12)
        
    # Add text box(A)
    plt.text(25, 25, display_text.message, fontsize=22, ha='center', va='center', bbox=dict(facecolor='white', alpha=0.5))

    plt.show()




#Main Menu
def Game_menu():
    mapdraw()
    
    #enables user to press a button to move on from the menu, otherwise exit(A)
    startgame = input("Press y to start game: ")
    if(startgame == "y"):
        display_text.message = None
        mapdraw()
        unit_selection(infantry, archers, cavalry, general, arty)
    else:
        sys.exit("Exiting game")
        
Game_menu()