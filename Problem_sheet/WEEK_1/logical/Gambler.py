import random
def gamler_simulation(stake, goal, trails):
    wins = 0
    total_bets =0
    for _ in range(trails):
        cash = stake
        bets = 0
        while 0 < cash < goal: 
            bets += 1
            if random.random()<0.5:
                cash -= 1
            else:
                cash += 1
        total_bets += bets
        if cash == goal:
            wins += 1

    print("wins: ", wins)
    print("win percentage: ",(wins/trails)*100)
    print("percentage of losses: ",(trails - wins)/trails*100)
    print("average bets per trails: ", total_bets/trails*100)

stake = int(input("Enter stake: "))
goal = int(input("Enter goal: "))
trails = int(input("Enter number of trails: "))
gamler_simulation(stake, goal, trails)