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

#class
class text:
    def __init__(self, message):
        self.message = message

#objects
display_text = text("start game?") #text
cmap = colors.ListedColormap(['green','blue']) #colormap

#unit creation
    #creation of infantry
infantry = np.array([2,10,1,1,10])
        #in the array [Movement,HP,Attack range, Attack damage, morale ]
        
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
    print('-'*50, "\nYou have a maximum of 10 uinits plus a general!\nThe Stats for each unit are sorted accordingly: --> [Movement,Health Pits ,Attack Range, Attack damage, Morale ]",'-'*50)
    picking = 1
    user_army = np.array([" "," "," "," "," "," "," "," "," "," "])
    while picking != 'y':
        #user picks units
        for i in range(0,10):
            print("1. Infantry:", infantry)
            print("2. Archers:", archers)
            print("3. Cavalry:", cavalry)
            print("4. Artillery:", arty)
            choice = input(f"You are chosing your {i+1} unit.\nEnter the corresponding number for the unit you want:")

            if choice == 1:
                user_army[i] = "Infantry"

            elif choice == 2:
                user_army[i] = "Archers"
                
            elif choice == 3:
                user_army[i] = "Cavalry"
                
            elif choice == 4:
                user_army[i] = "Artillery"
            
        # displays user army
        print(user_army[3])
        
        choice = input("If you are done selecting your army press y:")
        
        '''
        if choice == 'y':
            picking = 'y'
        else:
            #sends player to placement area
            '''

    
    
#Main Menu
def Game_menu():
    #Creats a figure of the axes object (A)
    fig, ax = plt.subplots(figsize=(20,20))
    
    #use cmp object to draw the map of the game(A)
    plt.pcolor(mainmap.game_map[::-1],cmap=cmap,edgecolors='black', linewidths=1)
    
    # Add text box(A)
    plt.text(25, 25, display_text.message, fontsize=22, ha='center', va='center', bbox=dict(facecolor='white', alpha=0.5))

    plt.show()
    
    #enables user to press a button to move on from the menu, otherwise exit(A)
    startgame = input("Press y to start game: ")
    if(startgame == "y"):
        display_text.message = None
        unit_selection(infantry, archers, cavalry, general, arty)
    else:
        sys.exit("Exiting game")
        
Game_menu()