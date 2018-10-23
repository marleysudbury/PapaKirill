# combat functions
import utilities
import random
import time

health_points = 0
rounds = 0

accuracy = 0.00

enemy = {
    "name": "Octavio",
    "hp": 100,
    "rounds": 6,
    "accuracy": 1.00
}


def combat(rounds1, health_points1, player_steps):
    global rounds
    rounds = 6
    global health_points
    health_points = health_points1
    player_steps = 50

    if player_steps > 50:
        enemy["accuracy"] -= 0.50
    else:
        enemy["accuracy"] -= player_steps / 100

    enemy["rounds"] += int(player_steps / 10)
    if enemy["rounds"] > 6:
        enemy["rounds"] = 6

    output = ""

    while health_points > 0 and enemy["hp"] > 0 and rounds > 0 and enemy["rounds"] > 0:
        utilities.clear_console()
        print("  _____                         ____        _   _   _      ")
        print(" |  __ \                       |  _ \      | | | | | |     ")
        print(" | |  | | __ _ _ __   ___ ___  | |_) | __ _| |_| |_| | ___ ")
        print(" | |  | |/ _` | '_ \\ / __/ _ \\ |  _ < / _` | __| __| |/ _ \\")
        print(" | |__| | (_| | | | | (_|  __/ | |_) | (_| | |_| |_| |  __/")
        print(" |_____/ \__,_|_| |_|\___\___| |____/ \__,_|\__|\__|_|\___|\n")
        print("{}: 'So, you found me detective. Well now there's no escape... for you!'".format(enemy["name"]))
        print("He starts to dance.")
        print("You: 'You son of a bitch!'")
        print("You start to dance.")
        print("\nPress ENTER to dance at {}.\n".format(enemy["name"]))
        print("You:\t HP={}\tDances={}/6".format(health_points, rounds))
        print("{}: HP={}\tDances={}/6\n".format(enemy["name"], enemy["hp"], enemy["rounds"]))
        if output != "":
            print(output)
        input()
        output = quick_time()

    utilities.clear_console()
    print("   _____                         ____                 ")
    print("  / ____|                       / __ \                ")
    print(" | |  __  __ _ _ __ ___   ___  | |  | |_   _____ _ __ ")
    print(" | | |_ |/ _` | '_ ` _ \ / _ \ | |  | \ \ / / _ \ '__|")
    print(" | |__| | (_| | | | | | |  __/ | |__| |\ V /  __/ |   ")
    print("  \_____|\__,_|_| |_| |_|\___|  \____/  \_/ \___|_|   \n")
    print("{}: 'So, you found me detective. Well now there's no escape... for you!'".format(enemy["name"]))
    print("He starts to dance.")
    print("You: 'You son of a bitch!'")
    print("You start to dance.")
    print("\nPress ENTER to dance at {}.\n".format(enemy["name"]))
    print("You:\t HP={}\tDances={}/6".format(health_points, rounds))
    print("{}: HP={}\tDances={}/6\n".format(enemy["name"], enemy["hp"], enemy["rounds"]))

    print(output)

    if health_points <= 0 and enemy["hp"] <= 0:
        return "You have tied with each other."
    elif health_points <= 0:
        return "You were out-danced by {}.".format(enemy["name"])
    elif enemy["hp"] <= 0:
        return "You have out-danced {}. Papa Kirill is avenged.".format(enemy["name"])
    elif rounds == 0 and enemy["rounds"] > 0:
        return "You ran out of mojo. {} notices this and approaches, before performing a killer dance move.".format(enemy["name"])
    else:  # enemy["rounds"] == 0:
        return "{} runs out of dance points and flees, hiding his shame.".format(enemy["name"])


def calc_damage(accuracy):
    global health_points
    global rounds

    # Quick time event to shoot bad guy!
    to_return = ""

    damage = random.randrange(20, 60)
    hit = random.random()
    rounds -= 1
    if hit > accuracy:
        enemy["hp"] -= damage
        to_return += "You scored {}!\n".format(damage)
    else:
        to_return += "You fell!\n"

    damage = random.randrange(20, 60)
    hit = random.random()
    enemy["rounds"] -= 1
    if hit > 0.5:
        health_points -= damage
        to_return += "{} scored {}!\n".format(enemy["name"], damage)
    else:
        to_return += "{} fell!\n".format(enemy["name"])

    if health_points < 0:
        health_points = 0
    if enemy["hp"] < 0:
        enemy["hp"] = 0

    return to_return


def quick_time():
    # Function to fire at the enemy
    for i in range(5, 0, -1):
        utilities.clear_console()
        print("  _____                         ____        _   _   _      ")
        print(" |  __ \                       |  _ \      | | | | | |     ")
        print(" | |  | | __ _ _ __   ___ ___  | |_) | __ _| |_| |_| | ___ ")
        print(" | |  | |/ _` | '_ \\ / __/ _ \\ |  _ < / _` | __| __| |/ _ \\")
        print(" | |__| | (_| | | | | (_|  __/ | |_) | (_| | |_| |_| |  __/")
        print(" |_____/ \__,_|_| |_|\___\___| |____/ \__,_|\__|\__|_|\___|\n")
        print("{}: 'So, you found me detective. Well now there's no escape... for you!'".format(enemy["name"]))
        print("He starts to dance.")
        print("You: 'You son of a bitch!'")
        print("You start to dance.")
        print("\nPress ENTER to dance at {}.\n".format(enemy["name"]))
        print("You:\t HP={}\tDances={}/6".format(health_points, rounds))
        print("{}: HP={}\tDances={}/6\n".format(enemy["name"], enemy["hp"], enemy["rounds"]))
        print(i)
        time.sleep(1)

    utilities.clear_console()
    print("  _____                         ____        _   _   _      ")
    print(" |  __ \                       |  _ \      | | | | | |     ")
    print(" | |  | | __ _ _ __   ___ ___  | |_) | __ _| |_| |_| | ___ ")
    print(" | |  | |/ _` | '_ \\ / __/ _ \\ |  _ < / _` | __| __| |/ _ \\")
    print(" | |__| | (_| | | | | (_|  __/ | |_) | (_| | |_| |_| |  __/")
    print(" |_____/ \__,_|_| |_|\___\___| |____/ \__,_|\__|\__|_|\___|\n")
    print("{}: 'So, you found me detective. Well now there's no escape... for you!'".format(enemy["name"]))
    print("He starts to dance.")
    print("You: 'You son of a bitch!'")
    print("You start to dance.")
    print("\nPress ENTER to dance at {}.\n".format(enemy["name"]))
    print("You:\t HP={}\tDances={}/6".format(health_points, rounds))
    print("{}: HP={}\tDances={}/6\n".format(enemy["name"], enemy["hp"], enemy["rounds"]))
    print("PRESS ENTER")
    start = time.time()
    input()
    end = time.time()
    difference = end - start
    if difference > 1:
        accuracy = 1
    else:
        accuracy = difference
    return calc_damage(accuracy)

    return