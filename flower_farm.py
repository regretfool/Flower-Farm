import time  # for sleep function

# Flower Farm Game
# This is a simple text-based game where you can plant flowers, wait for them to grow,
# deliver them in bouquets and sell them at the market. You can also buy tools to help
# you farming and sell more efficiently.

# inventory: dict = {"🌷🌱 Tulip seed": 0, "🌼🌱 Daisy seed": 1, "🌹🌱 Rose seed": 0, "🌷 Tulip": 0, "🌼 Daisy": 0, "🌹 Rose": 0}
inventory: dict = {"🌷🌱 Tulip seed": 1, "🌷 Tulip": 2, "🌹 Rose": 4}
flower_map: dict = {"🌷": "🌷 Tulip", "🌼": "🌼 Daisy", "🌹": "🌹 Rose"}
seed_map: dict = {"1": "🌷🌱 Tulip seed", "2": "🌼🌱 Daisy seed", "3": "🌹🌱 Rose seed"}
wait_timers: dict = {"🌷": 3, "🌼": 5, "🌹": 10}
wait_time: int = 0
# We shouldn't be able to change prices in game hence tuple
item_prices: dict = {"🌷 Tulip": 5, "🌼 Daisy": 10,  "🌹 Rose": 15}
plot: str = "🟫"
money: int = 0
has_seeds: bool = False


def plant_seeds(seed: str, plot: str) -> str:  # returns updated plant plot emoji
    # Loop through the dictionary
    for key, value in seed_map.items():
        # Find the key matching the passed value (seed)
        if key == seed:
            # Strip the string to get just the emoji
            # >strip makes a new list where each element is a word from the previous string
            # Set plot emoji to the new (flower) emoji
            # >removes the seedling and splits the strings ['🌷', ' Tulip seed']
            # >chooses string at index 0 for the emoji
            plot = value.split("🌱")[0]
            print(f"You planted a {plot}.")
            # Get seed name from seed map
            seed_name: str = seed_map[seed]
            # Deduct seed from inventory
            inventory[seed_name] -= 1  # could put into function maybe
            # Remove item from inventory if necessary
            remove_from_inventory(seed_name)
            # Get out of loop once planted the seed
            break
    return plot


def grow_flower(plot: str) -> None:
    print("Wait for your seeds to grow \n[ 🌱 ]")  # >can put animations here later
    wait_time = wait_timers[plot]  # >same as wait_timers.get(plot)
    for x in range(0, wait_time):  # wait time depending on seed
        # change newline for a space so the dots print in line #flush to refresh
        print(".", end=" ", flush=True)
        time.sleep(1)


def remove_from_inventory(item: str) -> None:
    if inventory[item] == 0:
        inventory.pop(item)


def add_to_inventory(item: str):
    # Checking if item already exists in inventory, if it does, it returns the current value
    # if it doesn't, then it returns the default value 0. After this it adds +1
    # "Give me the current number of this flower (or 0 if it's not there), and add 1 to it"
    inventory[item] = inventory.get(item, 0) +1
    print(f"Added [{item}] to your inventory.")


def harvest_flowers(plot: str) -> str:
    # Get the right flower name from flower_map
    flower: str = flower_map[plot]
    # Inform user about picked flower
    print(f"You picked up a {flower}!")
    # Add flower to inventory
    add_to_inventory(flower)
    # Get rid of the emoji
    #print(f"Added a {flower.split( )[2]} to your inventory")
    # Reset to empty soil
    plot = "🟫"
    return plot

def sell_flowers():
    # Show inventory (only harvested flowers)(do not hardcode)
    counter: int = 1
    for item in inventory:
        if item in item_prices:
            print(f"[{counter}] | ${item_prices[item]} : {item} | x{inventory[item]}")
            counter += 1
        
    # Make player choose which ones to sell (1, x, all) or sell all flowers from inventory)
    # go by flower name like previously [1]
    # Remove them from inventory
    # Add their money value to money 

# Main game loop
while True:
    # Show initial plot icon (empty soil)
    print(f"\n_______________\n[ {plot} ]\n", flush=True)

    print(
        "What do you want to do? \n[1] Plant seeds \n[2] Pick flowers \n[3] Go to the market \n[4] Show inventory"
    )
    menu_case: str = input("Choose an action (Enter a number):\n")

    if menu_case not in ["1", "2", "3", "4"]:
        print("Invalid action choice. Please try again (Enter a number):")
        continue  # skip the rest of the loop and start over

    # [1] Plant seeds
    if menu_case == "1" and plot == "🟫":
        # Check if there are ANY seeds in inventory (only working if item gets removed from inventory if 0)
        if any("🌱" in key for key in inventory):
            print("Choose a seed to plant:")
            seed: str = input(
                "Type '1' for 🌷 Tulip seeds, '2' for 🌼 Daisy seeds, '3' for 🌹 Rose seeds: "
            )  # put values here instead of hardcode
            # Check if it's a valid seed number by looking up seed_map keys
            if seed not in seed_map.keys():
                print("Invalid seed choice")
            # Check if any seeds are in inventory
            elif seed_map.get(seed) not in inventory:
                print(f"You don't have any {seed_map.get(seed)}s!")
            # Plant a seed if correct number
            else:
                # Set plot emoji to the new seed
                plot = plant_seeds(seed, plot)

            # Growth timer
            if plot != "🟫":
                grow_flower(plot)
        else:
            print("You have no seeds in your inventory! Go to the market to buy some.")
    elif menu_case == "1" and plot != "🟫":
        print("Pick your flower first!")

    # [2] Pick flowers
    if menu_case == "2":  # inform user, add to inventory, return to empty soil
        # Reset plot emoji to empty
        if plot == "🟫":
            print("There are no flowers to pick up! Plant some seeds first 🌱")
        else:
            plot = harvest_flowers(plot)
            
    # [3] Go to the market
    market_exit: bool = False  # Market value to exit loop
    
    if menu_case == "3":
        # Loop to stay in market
        while not market_exit:
            print("You're at the market. What do you want to do?")
            print(f"Money: {money}")
            print(
                "[1] Sell flowers \n[2] Buy seeds \n[3] Buy tools \n[4] Deliver bouquets"
                "\n[5] Go back to farm"
            )
            # market_case is the action in the market
            market_case: str = input("Choose an action: (Enter a number)")
            if market_case == "1":
                print("Choose which one to sell ([a] for all):")
                sell_flowers()
                #  add money
                # remove flowers from inventory
            elif market_case == "2":
                print(">buy seeds")
                #  Prompt if money = 0
                # add seeds to inventory
            elif market_case == "3":
                print(">buy tools")
                #  Prompt if money = 0
                # add tools to inventory
            elif market_case == "4":
                print(">deliver bouquets")
                # remove flowers from inventory if met requirements
                # add money
            elif market_case == "5":
                print(">go back to farm")
                market_exit = True
    # [4] Open Inventory
    if menu_case == "4":
        # Show everything in inventory (can categorize later)
        print(inventory)
        # Go back to menu
