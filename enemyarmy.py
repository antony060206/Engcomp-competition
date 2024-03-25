# -*- coding: utf-8 -*-
"""
Created on Sun Mar 17 17:06:14 2024

@author: clare
"""
import random


#defines the army by randomaly selection a number for each class 
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
    
    
#shows the size of enemy army 
def showarmy(enemy_army):
    print("This is enemy army:" 
          ,"\nInfantry:",  enemy_army[0]
          ,"\nArchers:",   enemy_army[1]
          ,"\nCavalry:",   enemy_army[2]
          ,"\nArtillery:", enemy_army[3]
          ,"\ngeneral:",   enemy_army[4]
          )

#draws the enemy formation upon beginning of the game
def enemy_formation1(enemy_army, gamemap):
    for i in range(len(enemy_army)):
        for x in range (enemy_army[i][0]):
             gamemap[10-i][20+x] = i+6
    
#enemy movment, as of this stage the enemy can only move down one at a time.     
def enemy_tile_movement(enemy_army, gamemap,a):
    #change all units tile back to grass or terrain
    for i in range(len(enemy_army)):
        for x in range (enemy_army[i][0]):
             gamemap[10-i][20+x] = 0
    
    #reimplement units onto gamemap with movement
    for i in range(len(enemy_army)):
        for x in range (enemy_army[i][0]):
             gamemap[a-i][20+x] = i+6
    a += 1
    return a