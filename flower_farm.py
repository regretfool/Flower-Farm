import time #for sleep function
#do it with objects&classes instead
#threading for multiple flower plots?
inventory: dict = {"🌷":"Tulip seeds","🌼":"Daisy seeds", "🌹":"Rose seeds"}
wait_timers: dict = {"🌷":3,"🌼":5, "🌹":10}
plant: str = "🟫"
money: int = 0

def plant_seeds(seed: str) -> None: # returns nothing
    global plant
    seed_map = {
        "tulip": "🌷",
        "daisy": "🌼",
        "rose": "🌹"
    }
    if seed in seed_map:
        plant = seed_map[seed]
        print(f"You planted {seed_map[seed]} seeds.") #shows value (emoji)
    else:
        print("Invalid seed choice.")

def harvest_crops() -> str:
    plant = ("🟫") # reset to empty soil
    # add flower to inventory
    return plant 

while True:
    print(f"\n_______________\n[ {plant} ]\n", flush=True)
    print(f"What do you want to do? \n[1] Plant seeds \n[2] Pick flowers \n[3] Go to the market")
    case : str = input("Choose an action:")

    if case == "1":
        print("Choose a seed to plant:")
        seed: str = input("pick tulip/daisy/rose: ")
        plant_seeds(seed)
        print(f"Wait for your seeds to grow \n[ 🌱 ]")
        # print(plant)
        wait_time = wait_timers.get(plant)
        # print(wait_time)
        for x in range(0, wait_time):   #wait time depending on seed
            print(".", end=" ", flush=True) #change newline for a space so the dots print in line #flush to refresh
            time.sleep(1)
    if case == "2": #harvest, add to inventory, return to empty soil, 
        plant = harvest_crops() #reset plant to empty
    
    if case == "3":
        print("You're at the market. What do you want to do?")
    #add coins
    