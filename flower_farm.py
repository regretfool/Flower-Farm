import time  # for sleep function

# do it with objects&classes instead
# threading for multiple flower plots?
# You should generate a requirements.txt file with all your dependencies listed on it and put that in your git.
# "requirements.txt" is the Python convention for naming your dependencies file).
# Then when someone wants to recreate your exact venv environment, they can do so from using "pip install -r requirements.txt"


# With your venv activated, run this in the terminal:

# pip freeze > requirements.txt

# The resulting file outputs a list of all your project's dependencies and allows another user (or you) to set up your project quickly on another #computer.

# The user just needs to clone the repository on another computer, create a venv and then run pip install -r 'requirements.txt' and it will install all #the dependencies for the cloned repository.

inventory: dict = {"🌷": "Tulip seeds", "🌼": "Daisy seeds", "🌹": "Rose seeds"}
wait_timers: dict = {"🌷": 3, "🌼": 5, "🌹": 10}
plant: str = "🟫"
money: int = 0


def plant_seeds(seed: str) -> None:  # returns nothing
    global plant
    seed_map = {"tulip": "🌷", "daisy": "🌼", "rose": "🌹"}
    if seed in seed_map:
        plant = seed_map[seed]
        print(f"You planted {seed_map[seed]} seeds.")  # shows value (emoji)
    else:
        print("Invalid seed choice.")


def harvest_crops() -> str:
    plant = "🟫"  # reset to empty soil
    # add flower to inventory
    return plant


while True:
    print(f"\n_______________\n[ {plant} ]\n", flush=True)
    print(
        "What do you want to do? \n[1] Plant seeds \n[2] Pick flowers \n[3] Go to the market"
    )
    case: str = input("Choose an action:")

    if case == "1":
        print("Choose a seed to plant:")
        seed: str = input("pick tulip/daisy/rose: ")
        plant_seeds(seed)
        print("Wait for your seeds to grow \n[ 🌱 ]")
        # print(plant)
        wait_time = wait_timers.get(plant)
        # print(wait_time)
        for x in range(0, wait_time):  # wait time depending on seed
            print(
                ".", end=" ", flush=True
            )  # change newline for a space so the dots print in line #flush to refresh
            time.sleep(1)
    if case == "2":  # harvest, add to inventory, return to empty soil,
        plant = harvest_crops()  # reset plant to empty

    if case == "3":
        print("You're at the market. What do you want to do?")
# add coins
# add flower bouquet deliveries
# add option to sell flowers
# add option to buy seeds
# add flowers to inventory
# add option to plant more seeds
# add sprinkler to speed up growth (change timer to variable)
# add extra plots