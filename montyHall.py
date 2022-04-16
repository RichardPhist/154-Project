import matplotlib.pyplot as plt
import numpy as np
import random

plt.style.use('fivethirtyeight')

#open a goat door
def open_goat_door(user_choice, host_choice, doorsNum,  ):
    goat_door = 1
    while(goat_door == host_choice or goat_door == user_choice):
        goat_door = (goat_door+1)%(doorsNum)
    return goat_door

#allows user to swap their choice after the host opens a goat_door
def swap_user_choice(user_choice1, opened_door, doorsNum ):
    new_user_door = 1
    while( new_user_door == opened_door or new_user_door  == user_choice1):
        new_user_door = ( new_user_door +1)%(doorsNum)
    return new_user_door

#run games that tally wins/losses and if there was a user choice swap
def monty_hall( sim_nums, swap_door):
    no_swap_wins= 0
    swap_wins= 0 
    swap_losses = 0
    no_swap_losses = 0
    print(swap_losses)

#update later for more doors
    doors =[0,1,2]
    doorsNum = len(doors)
    for i in range(0, sim_nums):
        car_door = random.randint(0, doorsNum-1)
        user_choice = random.randint(0, doorsNum-1)
        host_choice = car_door
        opened_door = open_goat_door(user_choice, host_choice, doorsNum)

#swap the user's choice to a new door
        if swap_door == True:
            new_user_choice = swap_user_choice(user_choice, opened_door, doorsNum)
        
#Possible game scenarios 
        if not swap_door and user_choice == car_door:
            no_swap_wins +=1
            print("\nUser kept their winner door#", user_choice,"|car door was #", car_door, "|monty opened goat door#", opened_door)
        
        elif swap_door and new_user_choice == car_door:
            swap_wins +=1
            print("\nUser swapped to winner door#", new_user_choice,"|car door was#", car_door, "|monty opened goat door#", opened_door)

        elif swap_door and new_user_choice != car_door:
            swap_losses +=1
            print("\nUser swapped to losing door#", new_user_choice, "|car door was#", car_door, "|monty opened goat door#", opened_door)
                    
        elif not swap_door and user_choice != car_door:
            no_swap_losses +=1
            print("\nUser kept their losing door#", user_choice,"|car door was#", car_door, "|monty opened goat door#", opened_door)
        else: print("error")

    return   no_swap_wins, swap_wins, swap_losses, no_swap_losses, sim_nums


sim_results = monty_hall(10, True) 





    
        
       



