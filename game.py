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
        Game_menu()
    else:
        sys.exit("Exiting game")
        
Game_menu()