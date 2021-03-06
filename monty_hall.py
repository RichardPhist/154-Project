# 154 Project - Monty Hall Game

# Julieta Mendez
# Malee Seechan

import matplotlib.pyplot as plt
import numpy as np
import random

#testing purposes 

plt.style.use('fivethirtyeight')

#run games that tally wins/losses and if there was a user choice swap
def monty_hall(sim_nums, doors_input, swap_door, variant):
    no_swap_wins= 0
    swap_wins= 0 
    swap_losses = 0
    no_swap_losses = 0
    other_door = 0

    for i in range(0, sim_nums):
        car_door = random.randrange(0, doors_input)
        user_choice = random.randrange(0, doors_input)
        monty_choice = car_door
        variant_loss, other_door = open_door(other_door, user_choice, monty_choice, doors_input, variant)              

#swap the user's choice to a new door
        if swap_door == True:
            new_user_choice = other_door

#Possible game scenarios 
        if variant_loss == True:
            if(swap_door == True):
                swap_losses+=1
            else: no_swap_losses +=1            
            #VARIANT: the player lost because the host opened the car door

        elif not swap_door and user_choice == car_door:
            no_swap_wins +=1
            #User does not switch and wins
        
        elif not swap_door and user_choice != car_door:
            no_swap_losses +=1
            #User does not switch and loses

        elif swap_door and new_user_choice == car_door:
            swap_wins +=1
            #User switches and wins

        elif swap_door and new_user_choice != car_door:
            swap_losses +=1
            #User switches and loses
                    
        else: print("error")

    return   no_swap_wins, swap_wins, swap_losses, no_swap_losses, sim_nums

#open a goat door
def open_door(other_door, user_choice, monty_choice, doorsNum, variant):
    opened_door_lists=[]
    variant_loss = False
    
    #add all doors to the list, remove the user's door and the winning door
    for i in range(0, doorsNum):
        opened_door_lists.append(i)

    # NO VARIANT: host may only open a goat door
    if(variant == False):

        #if the user chooses the winning door, the host can choose from either leftover door
        #so leave a random door for the host to open
        if (user_choice == monty_choice):
            opened_door_lists.remove(user_choice) #remove the users choice from the hosts list

            other_door = random.randrange(len(opened_door_lists))

            # ensure other_door and user_choice are different
            if(other_door == user_choice and user_choice == len(opened_door_lists)-1):
                other_door -= 1
            else:
                other_door =+ 1

            opened_door_lists.remove(other_door) #remove a random goat door

        #The only goat doors(s) the host can open is the door the user did not choose 
        #and the one that does not have a car behind it 
        else:
            opened_door_lists.remove(user_choice) #remove the users choice from the hosts list
            opened_door_lists.remove(monty_choice) #remove the car door from the hosts list
    
    # VARIANT: host may open car door by accident
    else:
        # pick random door the host will leave closed to give player a chance to switch
        other_door = random.randint(0,len(opened_door_lists)-1)

        # ensure the 2 doors left closed are not the same
        if(other_door == user_choice and user_choice == len(opened_door_lists)-1):
            other_door = other_door - 1
        elif(other_door == user_choice):
            other_door = other_door + 1

        opened_door_lists.remove(user_choice) 
        opened_door_lists.remove(other_door) 

        # if car door was not removed from the list then
        # the host opened the car door, thus the player lost
        if(other_door != monty_choice and user_choice != monty_choice):
            variant_loss = True

    return variant_loss, other_door
   


tests = 1000
doors = 100
swap = True
variant = True #change to run with or without variant

sim_swap_results = monty_hall(tests, doors, swap, variant) 
sim_no_swap_results = monty_hall(tests, doors, swap, variant)

print("\n---------------------------- Monty Hall Simulation Results ----------------------------")
print("Number of tests: ", tests)
print("Number of doors: ", doors)
print("Swap user choice:", "\twins ", sim_swap_results[1]/sim_swap_results[4]*100, "% - losses ", sim_swap_results[2]/sim_swap_results[4]*100,"%" )
print("No Swap user choice:", "\twins ", sim_no_swap_results[0]/sim_no_swap_results[4]*100, "% - losses ", sim_no_swap_results[3]/sim_no_swap_results[4]*100,"%" )

testsList = []
winList=[]
count=0

for i in range(1, tests):
    testsList.append(i)

    #run monty hall simulation  with i as the count of simulations,
    #doors as the count of doors, 
    #True/False as switch/no switch,
    #and True/False as variatoin/no variant

    y = monty_hall(i, doors, swap, variant) 
    percent = (y[1]/y[4]*100)
    winList.append (percent)
    count += percent

# Average win% over 1000 tests
print("average win percentage: ", count/tests)

plt.figsize =((1,3))
plt.plot(testsList, winList)
plt.xlabel('Tests')
plt.ylabel('Percentage of Wins')
plt.title('Win Percentage (no swap/no variant)')
plt.show()
