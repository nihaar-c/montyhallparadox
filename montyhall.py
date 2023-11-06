import random

#case that user switches
winSim1 = 0

#case that user stays
winSim2 = 0

n = random.randint(3,100)

# n = 3. can use this to check percentages

for i in range(5000):
    carIdx = random.randint(0,n-1)
    choice = random.randint(0,n-1)


    #choose a door to eliminate
    doors = [j for j in range(n)]
    del doors[choice]
    if carIdx in doors:
        doors.remove(carIdx)
    removedIdx = random.choice(doors)

    doors = [j for j in range(n)]
    del doors[removedIdx]
    # one door removed

    if choice == carIdx:
        #no switching
        winSim2 += 1
        
    else:
        #switch.. so remove user's choice and randomly choose from remaining
        doors.remove(choice)
        choice = random.choice(doors)
        if carIdx == choice:
            winSim1 += 1
    

print (str(n) + " doors")

#prints a value close to 2/3
print("Odds that switching doors wins: " + str(100*float(winSim1/5000)) + "%.")
    
#prints a value close to 1/3
print("Odds that not switching doors wins: " + str(100*float(winSim2/5000)) + "%.")
