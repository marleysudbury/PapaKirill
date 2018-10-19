# combat functions
from utilities import *
import random
steps = 0
accuracy = 0.00

enemy = {
    "name": "Octavio",
    "hp": 100,
    "rounds": 1
}


def combat():
    global rounds
    global health_points

    if steps > 50:
        accuracy = 0.50
    else:
        accuracy = steps / 100

    enemy["rounds"] += int(steps / 10)
    if enemy["rounds"] > 6: enemy["rounds"] = 6

    output = ""

    while health_points > 0 and enemy["hp"] > 0 and rounds > 0 and enemy["rounds"] > 0:
        clear_console()
        print("  ____                  ____        _   _   _      ")
        print(" |  _ \                |  _ \      | | | | | |     ")
        print(" | |_) | ___  ___ ___  | |_) | __ _| |_| |_| | ___ ")
        print(" |  _ < / _ \/ __/ __| |  _ < / _` | __| __| |/ _ \\")
        print(" | |_) | (_) \__ \__ \ | |_) | (_| | |_| |_| |  __/")
        print(" |____/ \___/|___/___/ |____/ \__,_|\__|\__|_|\___|\n")
        print("{}: 'So, you found me detective. Well now there's no escape... for you!'".format(enemy["name"]))
        print("He draws his gun.")
        print("You: 'You son of a bitch!'")
        print("You draw your gun.")
        print("\nPress ENTER to fire at {}.\n".format(enemy["name"]))
        print("You:\t HP={} Rounds={}/6".format(health_points, rounds))
        print("{}: HP={} Rounds={}/6\n".format(enemy["name"], enemy["hp"], enemy["rounds"]))
        if output != "": print(output)
        input()
        output = calc_damage()

    clear_console()
    print("   _____                         ____                 ")
    print("  / ____|                       / __ \                ")
    print(" | |  __  __ _ _ __ ___   ___  | |  | |_   _____ _ __ ")
    print(" | | |_ |/ _` | '_ ` _ \ / _ \ | |  | \ \ / / _ \ '__|")
    print(" | |__| | (_| | | | | | |  __/ | |__| |\ V /  __/ |   ")
    print("  \_____|\__,_|_| |_| |_|\___|  \____/  \_/ \___|_|   \n")
    print("{}: 'So, you found me detective. Well now there's no escape... for you!'".format(enemy["name"]))
    print("He draws his gun.")
    print("You: 'You son of a bitch!'")
    print("You draw your gun.")
    print("\nPress ENTER to fire at {}.\n".format(enemy["name"]))
    print("You:\t HP={} Rounds={}/6".format(health_points, rounds))
    print("{}: HP={} Rounds={}/6\n".format(enemy["name"], enemy["hp"], enemy["rounds"]))

    if health_points <= 0 and enemy["hp"] <= 0:
        return "You have killed each other."
    if health_points <= 0:
        return "You were killed by {}.".format(enemy["name"])
    if enemy["hp"] <= 0:
        return "You have killed {}. Papa Kirill is avenged.".format(enemy["name"])
    if rounds == 0 and enemy["rounds"] > 0:
        return "You ran out of rounds. {} notices this and approaches, before shooting you through the head.".format(enemy["name"])
    if enemy["rounds"] == 0:
        return "{} runs out of rounds and flees. He's caught by police officers who were lurking around the corner.".format(enemy["name"])


def calc_damage():
    global rounds
    global health_points

    to_return = ""

    hit = random.random()
    rounds -= 1
    if hit > accuracy:
        enemy["hp"] -= 30
        to_return += "You hit for 30!\n"
    else:
        to_return += "You missed!\n"

    hit = random.random()
    enemy["rounds"] -= 1
    if hit > 0.5:
        health_points -= 30
        to_return += "{} hit for 30!\n".format(enemy["name"])
    else:
        to_return += "{} missed!\n".format(enemy["name"])

    if health_points < 0: health_points = 0
    if enemy["hp"] < 0: enemy["hp"] = 0

    return to_return