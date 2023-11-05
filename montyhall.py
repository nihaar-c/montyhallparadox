import random

#case that user switches
winSim1 = 0

#case that user stays
winSim2 = 0

for i in range(5000):
    carIdx = random.randint(0,2)
    choice = random.randint(0,2)


    #choose a door to eliminate
    doors = [0,1,2]
    del doors[choice]
    if carIdx in doors:
        doors.remove(carIdx)
    removedIdx = random.choice(doors)

    doors = [0,1,2]
    del doors[removedIdx]
    # 2 doors remaining

    if choice == carIdx:
        winSim2 += 1
    else:
        doors.remove(choice)
        choice = doors[0]
        if carIdx == choice:
            winSim1 += 1
    


#prints a value close to 2/3
print("Odds that switching doors wins: " + str(100*float(winSim1/5000)) + "%.")
    
#prints a value close to 1/3
print("Odds that not switching doors wins: " + str(100*float(winSim2/5000)) + "%.")




