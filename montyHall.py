import matplotlib.pyplot as plt
import numpy as np
import random

#testing purposes 

plt.style.use('fivethirtyeight')

#run games that tally wins/losses and if there was a user choice swap
def monty_hall(sim_nums, doors_input, swap_door):
    no_swap_wins= 0
    swap_wins= 0 
    swap_losses = 0
    no_swap_losses = 0

#update later for more doors
 
    for i in range(0, sim_nums):
        car_door = random.randrange(0, doors_input)
        user_choice = random.randrange(0, doors_input)
        monty_choice = car_door
        opened_doorsList = open_goat_door(user_choice, monty_choice, doors_input)

#swap the user's choice to a new door
        if swap_door == True:
            new_user_choice = swap_user_choice(user_choice, opened_doorsList, doors_input)

#Possible game scenarios 
        if not swap_door and user_choice == car_door:
            no_swap_wins +=1
            #print("User chose door#", user_choice, "\tmonty opened goat doors#", opened_doorsList, "\tcar door#", car_door, "\tWINNER!")
        
        elif not swap_door and user_choice != car_door:
            no_swap_losses +=1
            #print("User chose door#", user_choice, "\tmonty opened goat doors#", opened_doorsList,"\tcar door#", car_door )

        elif swap_door and new_user_choice == car_door:
            swap_wins +=1
            #print("User chose door#",user_choice, "\tmonty opened goat doors#", opened_doorsList, "swapped to doors#", new_user_choice, "\tcar door#", car_door, "\tWINNER!")

        elif swap_door and new_user_choice != car_door:
            swap_losses +=1
            #print("User chose door#", user_choice,"\tmonty opened goat doors#", opened_doorsList,  "swapped to doors#", new_user_choice,"\tcar door#", car_door )
                    
        else: print("error")

    return   no_swap_wins, swap_wins, swap_losses, no_swap_losses, sim_nums

#open a goat door
def open_goat_door(user_choice, monty_choice, doorsNum):
    open_goat_doorList=[]
    
    #add all doors to the list, remove the user's door and the winning door
    for i in range(0, doorsNum):
        open_goat_doorList.append(i)

    #if the user happens to choose the winning door, one goat door must be left closed for them to swap to
    if (user_choice == monty_choice):
        open_goat_doorList.remove(user_choice)
        open_goat_doorList.pop(random.randrange(len(open_goat_doorList))) 
    else:
        open_goat_doorList.remove(user_choice)
        open_goat_doorList.remove(monty_choice)
    
    return open_goat_doorList
   

#allows user to swap their choice after the host opens goat_doors. New door can't be one that is already open nor the user's current choice
def swap_user_choice(user_choice, opened_doorsList, doorsNum ):
    new_user_door = random.randrange(0, doorsNum)
    while(new_user_door in opened_doorsList or new_user_door == user_choice):
        new_user_door = random.randrange(0, doorsNum)
    return new_user_door



tests = 1000
doors = 3
sim_swap_results = monty_hall(tests, doors, True) 
sim_no_swap_results = monty_hall(tests, doors, False)
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
    y = monty_hall(i, doors, True)
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
plt.show()

    








    
        
       


