import random


def monty_hall(switch):
    # 3 doors have been created, there is currently nothing behind each door
    doors = {"door1": None, "door2": None, "door3": None}

    # Creating a list of possible prizes
    prize_behind_doors = ["Goat", "Goat", "Car"]

    # shuffling the list of possible prizes, since I entered them manually (not sure if it matters but just added it)
    random.shuffle(prize_behind_doors)

    # after shuffling the list of prizes, we will assign a prize to each door
    for i in range(3):
        doors[f"door{i + 1}"] = prize_behind_doors[i]


    # assigning random door to contestant
    # to use random we have to convert the dictionary to list, the list will only contain keys of the dictionary
    # this is equal to a string value since it will select a random key
    contestant_door = random.choice(list(doors))

    # removable door = any door that does not have a car behind it or a door that was chosen by the user
    removable_doors = [door for door in doors if doors[door] != "Car" and door != contestant_door]

    # if the user decides to switch doors, we will choose any random door from removable_doors and remove it
    # A door is removed so there are only two doors after this is executed
    removable_doors.remove(random.choice(removable_doors))

    # If contestant decides to swap doors after door is revealed
    if switch:
        # user chose the correct door first try since there is one available option to swap with in removable_doors
        if len(removable_doors) == 1:
            # swapping current door with other available door
            contestant_door = removable_doors[0]
            return doors[contestant_door] == "Car"
        # this means user choose either  car or a goat car and has to make final switch
        else:
            # used != to show the opposite sorta like "This is what you would have had IF YOU would've stayed "
            return doors[contestant_door] != "Car"
    # user did not want to swap doors
    else:
        # will return true or false depending on what's behind the door
        return doors[contestant_door] == "Car"


def simulate(num_iterations):
    # counter that will keep track of wins
    wins = 0
    # loop that will run 'num_iterations' of times
    for i in range(num_iterations):
        sol = monty_hall(True)
        # counter for each time a game is won
        if sol:
            wins += 1
    # calculating win percentage
    percentage = (wins / num_iterations) * 100
    # rounds win/loss to two decimal places
    return round(percentage, 2)


if __name__ == "__main__":
    print(simulate(100))
