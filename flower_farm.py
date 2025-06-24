import time  # for sleep function

# Flower Farm Game
# This is a simple text-based game where you can plant flowers, wait for them to grow,
# deliver them in bouquets and sell them at the market. You can also buy tools to help
# you farming and sell more efficiently.
inventory: dict = {"🌷🌱 Tulip seed": "", "🌼🌱 Daisy seed": "", "🌹🌱 Rose seed": "",
                   "Tulip": 0, "Daisy": 0, "Rose": 0}
flower_map: dict = {"🌷 Tulip": "1", "🌼 Daisy": "2", "🌹 Rose": "3"}
seed_map: dict = {"🌷🌱 Tulip seed": "1", "🌼🌱 Daisy seed": "2", "🌹🌱 Rose seed": "3"}
wait_timers: dict = {"🌷": 3, "🌼": 5, "🌹": 10}
wait_time: int = 0
plot: str = "🟫"
money: int = 0


def plant_seeds(seed: str, plot: str) -> str:  # returns updated plant plot emoji
    
    # Check if it's a valid seed number
    if seed not in seed_map.values():
        print("Invalid seed choice")
        # Still needs to return plot (unchanged)
        return plot
    
    # Loop through the dictionary
    for key, value in seed_map.items():
        # Find the key matching the passed value (seed)
        if value == seed:   
            # Strip the string to get just the emoji
            # >strip makes a new list where each element is a word from the previous string
            # Set plot emoji to the new (flower) emoji
            # >removes the seedling and splits the strings ['🌷', ' Tulip seed']
            # >chooses string at index 0 for the emoji
            plot = key.split("🌱")[0]
            print(f"You planted a {plot}.")
    return plot

def grow_flower(plot: str) -> None:
    print("Wait for your seeds to grow \n[ 🌱 ]") # >can put animations here later
    wait_time = wait_timers[plot]  # >same as wait_timers.get(plot)
    for x in range(0, wait_time):  # wait time depending on seed
        # change newline for a space so the dots print in line #flush to refresh
        print(".", end=" ", flush=True)
        time.sleep(1)

def harvest_crops() -> str:
    plot = "🟫"  # reset to empty soil
    # add flower to inventory
    return plot

# Main game loop
while True:
    # Show initial plot icon (empty soil)
    print(f"\n_______________\n[ {plot} ]\n", flush=True)
    
    print(
        "What do you want to do? \n[1] Plant seeds \n[2] Pick flowers \n[3] Go to the market"
    )
    menu_case: str = input("Choose an action (enter 1, 2 or 3):\n")
    
    if menu_case not in ["1", "2", "3"]:
        print("Invalid action choice. Please try again (enter 1, 2 or 3).")
    
    if menu_case == "1" and plot == "🟫":     
        print("Choose a seed to plant:")
        #check if any seeds are in inventory
        seed: str = input("Type '1' for Tulip seeds, '2' for Daisy seeds, '3' for Rose seeds: ")
        # Set plot emoji to the new seed
        plot = plant_seeds(seed, plot)
        
        # Growth timer
        # >should it run from inside plant seeds?
        grow_flower(plot)
    else:
        print("Pick your flower first!")    
        
        
    if menu_case == "2":  # harvest, add to inventory, return to empty soil,
        plot = harvest_crops()  # reset plant to empty
        # add flower to inventory


    if menu_case == "3":
        print("You're at the market. What do you want to do?")
        print("[1] Sell flowers \n[2] Buy seeds \n[3] Buy tools \n[4] Deliver bouquets"
              "\n[5] Go back to farm")
        market_case: str = input("Choose an action: (Enter a number)")   # market_case is the action in the market
    
    
        