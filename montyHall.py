import matplotlib.pyplot as plt
import numpy as np
import random

#testing purposes 

plt.style.use('fivethirtyeight')

#run games that tally wins/losses and if there was a user choice swap
def monty_hall(sim_nums, doors_input, swap_door, variation):
    no_swap_wins= 0
    swap_wins= 0 
    swap_losses = 0
    no_swap_losses = 0

#update later for more doors
 
    for i in range(0, sim_nums):
        car_door = random.randrange(0, doors_input)
        user_choice = random.randrange(0, doors_input)
        monty_choice = car_door
        opened_door_list = open_door(user_choice, monty_choice, doors_input, variation)              

#swap the user's choice to a new door
        if swap_door == True:
            new_user_choice = swap_user_choice(user_choice, opened_door_list, doors_input)

#Possible game scenarios 
        if not swap_door and user_choice == car_door:
            no_swap_wins +=1
            #print("User chose door#", user_choice, "\tmonty opened goat doors#", opened_door_list, "\tcar door#", car_door, "\tWINNER!")
        
        elif not swap_door and user_choice != car_door:
            no_swap_losses +=1
            #print("User chose door#", user_choice, "\tmonty opened goat doors#", opened_door_list,"\tcar door#", car_door )

        elif swap_door and new_user_choice == car_door:
            swap_wins +=1
            #print("User chose door#",user_choice, "\tmonty opened goat doors#", opened_door_list, "swapped to doors#", new_user_choice, "\tcar door#", car_door, "\tWINNER!")

        elif swap_door and new_user_choice != car_door:
            swap_losses +=1
            #print("User chose door#", user_choice,"\tmonty opened goat doors#", opened_door_list,  "swapped to doors#", new_user_choice,"\tcar door#", car_door )
                    
        else: print("error")

    return   no_swap_wins, swap_wins, swap_losses, no_swap_losses, sim_nums

#open a goat door
def open_door(user_choice, monty_choice, doorsNum, variation):
    opened_door_lists=[]
    
    #add all doors to the list, remove the user's door and the winning door
    for i in range(0, doorsNum):
        opened_door_lists.append(i)

    #If the variation is not chosen, the host may only open a goat door
    if(variation == False):

        #if the user chooses the winning door, the host can choose from either leftover door
        #so leave a random door for the host to open
        if (user_choice == monty_choice):
            opened_door_lists.remove(user_choice) #remove the users choice from the hosts list

            remove_door = random.randrange(len(opened_door_lists))
            if(remove_door == user_choice):
                remove_door+=1

            opened_door_lists.remove(remove_door) #remove a random goat door

        #The only goat door the host can open is the door the user did not choose 
        #and the one that does not have a car behind it 
        else:
            opened_door_lists.remove(user_choice) #remove the users choice from the hosts list
            opened_door_lists.remove(monty_choice) #remove the car door from the hosts list
    
    #else - the variation is  chosen: the host may open any door by accident
    #minus two leftover doors 
    else:
        door1 = random.randrange(len(opened_door_lists))

        if(door1==0):
            door2 = door1+1
        else:
            door2=door1-1

        opened_door_lists.remove(door1) #remove a random door
        opened_door_lists.remove(door2) #remove a random door

    return opened_door_lists
   

#allows user to swap their choice after the host opens goat_doors. New door can't be one that is already open nor the user's current choice
def swap_user_choice(user_choice, opened_door_list, doorsNum):
    new_user_door = random.randrange(0, doorsNum)
    while(new_user_door in opened_door_list or new_user_door == user_choice):
        new_user_door = random.randrange(0, doorsNum)
    return new_user_door



tests = 10
doors = 3
swap = False
variation = True #change to run with or without variation

sim_swap_results = monty_hall(tests, doors, swap, variation) 
sim_no_swap_results = monty_hall(tests, doors, swap, variation)

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
    #and True/False as variatoin/no variation

    y = monty_hall(i, doors, swap, variation) 
    percent = (y[1]/y[4]*100)
    winList.append (percent)
    count += percent

# Average win% over 1000 tests
print("average win percentage: ", count/tests)

plt.figsize =((2,5))
plt.plot(testsList, winList)
plt.xlabel('Tests')
plt.ylabel('Percentage of Wins')
plt.title('Monty Hall Win Percentage (swap)')
#plt.show()

    








    
        
       


