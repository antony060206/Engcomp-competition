# -*- coding: utf-8 -*-
"""
Created on Sun Mar 17 17:06:14 2024

@author: clare
"""
import random

def enemy_selection(infantry, archers, cavalry, general, arty, enemy_army):
    units = [1,2,3,4] #list of units to chose from (same numbers as the players)
    for i in range(0,10): #choses units at random
        choice = random.choice(units)
        if choice == 1:
            enemy_army[0] += [1]
            
        elif choice == 2:
            enemy_army[1] += [1]
            
        elif choice == 3:
            enemy_army[2] += [1]
            
        elif choice == 4:
            enemy_army[3] += [1]

        
    enemy_army[4] = enemy_army[4]+1
    
    
    
def showarmy(enemy_army):
    print("This is your army:" 
          ,"\nInfantry:",  enemy_army[0]
          ,"\nArchers:",   enemy_army[1]
          ,"\nCavalry:",   enemy_army[2]
          ,"\nArtillery:", enemy_army[3]
          ,"\ngeneral:",   enemy_army[4]
          )