#!/usr/bin/env python

from random import randint
import time
from threading import Thread
def prRed(skk): print("\033[91m {}\033[00m" .format(skk))



def say_hi():

    print("\n\n***'dévinette 1.6'***\n")
    

    fail = 0
    player_name = ''

    while player_name == (''):
        ask = "Ton nom?\n$ "
        player_name = input(ask)
        if player_name == (''):
            if fail == 0:
                print("Tu n'a pas dit ton nom......")
            elif fail == 1:
                print("Tu te prend pour un/une trés malin!")
            elif fail == 2:
                print("Désolé tu m'a l'aire pas assez motivé!")
                return ''
            fail = fail +1
    return player_name
            
            

def guess(player_name, life):
    run_count = False
    game_var = randint(1, 100)

    while True:
        
        if run_count == False: 
                create_thread()
                t1 = Thread(target=countdown)
                t1.start()
                
        if  secs == 0:    
            print('\n\nTemps fini! Tu a perdu une vie!\n')
            life -=1
            print("Il te reste",life , "vies\n")            
            return False             
        if secs != 0:
            try:
                p_var_int = int(input("$")) 
            except  ValueError:
                print("\nC'est ne pas une chiffre!\n")
                run_count = True   
                continue        
        if p_var_int == game_var: 
            print('\nGaaagnééé!!!\n')
            run_count = True            
            return True                
        if p_var_int > (100) and secs != 0:
            print("\nc'est ou t'est allé a l'école, " + player_name + ' ?')
            print("Tu a encore ", secs, " secondes!") 
            run_count = True 
            continue 
        if p_var_int < game_var and secs != 0:
            print("\nC'est plus grand!")   
            print("Tu a encore ", secs, " secondes!")
            run_count = True
            continue  
        if p_var_int > game_var and secs != 0:
            print("\nC'est plus petite!")
            print("Tu a encore ", secs, " secondes!") 
            run_count = True 
             

def game(player_name):
    
    global secs
      
    level = 1
    life = 3  
    wait_before_game()
    
    while life > 0:
        
        match level:
            case 1:
                secs = 30
            case 2:
                secs = 25
            case 3:
                secs = 15
            case 4:
                secs = 10
            case 5:
                secs = 5
            case 6:
                secs = 3
            case 7:
                secs = 3                    
        
                
        print("\n" + player_name + ',\ndévinne la chiffre entre 0 et 100!')
        print("Tu a", secs, "secondes et", life, "vies")
        print("Level:", level)
        input("\n*pour commencer appui sur la touche 'entrée'*\n")
        print("La partie commence dans!") 
        secs_play()
             
        win = guess(player_name, life)
            
        if win == True:
            level += 1
        if win == False:
            life -= 1        
        match level:
            case 8:
                print("Tu battu le Jeu!!!!!\r")
                time.sleep(2)
                print("winwinwinwinwinwinwinwinwinwin")        
        if life > 0:
            oui_or_no = input("Est-ce que tu veut continuer?\n\ntappe o pour Oui ou n pour Non\n\n")
        if oui_or_no == ('n'): 
            print('\nau révoir,', (player_name), '!\n\n')            
            return
    
    print("\nPeeeeeeeerdu! Miau miau miau.......")
    time.sleep(5)

def countdown():
    global secs
    while secs > 0:
        #print(secs, end="\r")
        time.sleep(1)
        secs -= 1             

    
def create_thread():
	return Thread(target=countdown)      


def secs_play():
    secs_play = 5 
    while secs_play > 1:
        time.sleep(1)
        secs_play -= 1
        print(secs_play, end=("\r            "))
        if secs_play == 1: 
            prRed("Dévine!!!\n")        
    

def wait_before_game():
        secs_wait = 1 
        while secs_wait > 0:         
            print(" ", end=" \r")   
            time.sleep(0.5)
            print("*", end=" \r")
            time.sleep(0.5)
            print(" ", end="\r")
            secs_wait -= 1

   
player_name = say_hi()

if player_name: 
    game(player_name)
        
      

    
    
               
        

       
 


   
            


    



















