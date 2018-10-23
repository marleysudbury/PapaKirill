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
        print("You:\t HP={}\tRounds={}/6".format(health_points, rounds))
        print("{}: HP={}\tRounds={}/6\n".format(enemy["name"], enemy["hp"], enemy["rounds"]))
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
    print("He draws his gun.")
    print("You: 'You son of a bitch!'")
    print("You draw your gun.")
    print("\nPress ENTER to fire at {}.\n".format(enemy["name"]))
    print("You:\t HP={}\tRounds={}/6".format(health_points, rounds))
    print("{}: HP={}\tRounds={}/6\n".format(enemy["name"], enemy["hp"], enemy["rounds"]))

    print(output)

    if health_points <= 0 and enemy["hp"] <= 0:
        return """
        You have neutralized each other and while you are both on the 
        floor breathing your last breaths Octavio Ricca tells you 
        that he is not the killer.

        In those last moments, you remember about the dough you 
        picked up at the beginning of the game. If you've inspected
        the dough you would know that the hand mark came from someone
        with very large hands. This hand mark didn't match Papa Kirill's 
        or any of the apprentices' hands in the restaurant. You look at 
        Octavio's hands, they are average size.

        "Then why?..." you say before dying.

        You have completed the game but failed. Try again."""
    elif health_points <= 0:
        return """
        You were killed by Octavio Ricca.
        You are dying. As you die your vision gets very blurry. 
        Your uncle appears in front of you.

        "You have disgraced our family by failing to avenge 
        me!" screamed Papa Kirill. "I hope that you go to hell!"

        Octavio Ricca will continue to live on. During the fight, 
        he has lost both of his arms. This injury will prevent him
        from causing any other disasters.

        Congratulations! You are a failure in the eyes of Papa Kirill."""
    elif enemy["hp"] <= 0:
        return """
        You have just killed Octavio Ricca. 

        A rush of adrenaline still rushes through your veins. You walk
        towards Octavio Ricca and spit at his cadaver. You crouch and
        look at his corpse. Every limb is very still. His hands are still
        wrapped around the pistol which lay next to his face. You notice 
        how small they are. 

        This is very weird. When you investigated the pizzeria at the 
        very start you had found some dough which served as evidence 
        that the killer had big hands. It doesn't make sense.

        If Octavio Ricca is not the killer, then who is?

        Congratulations you have completed the game."""
    elif rounds == 0 and enemy["rounds"] > 0:
        return """
        You ran out of rounds. Octavio Ricca notices this and approaches,
        before shooting you through the head.
        
        You were killed by Octavio Ricca.
        You are dying. As you die your vision gets very blurry. 
        Your uncle appears in front of you.

        "You have disgraced our family by failing to avenge 
        me!" screamed Papa Kirill. "I hope that you go to hell!"

        Octavio Ricca will continue to live on. During the fight, 
        he has lost both of his arms. This injury will prevent him
        from causing any other disasters.

        Congratulations! You are a failure in the eyes of Papa Kirill."""
    else:  # enemy["rounds"] == 0:
        return """
        Octavio Ricca runs out of rounds and flees. He's caught by Bob Smith
        who was lurking around the corner. After going through the judicial
        system he is put into a penitentiary in Alaska where he daily picks up
        soap for all of the boys.
        
        Congratulations! You have completed the game."""


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
        to_return += "You hit for {}!\n".format(damage)
    else:
        to_return += "You missed!\n"

    damage = random.randrange(20, 60)
    hit = random.random()
    enemy["rounds"] -= 1
    if hit > 0.5:
        health_points -= damage
        to_return += "{} hit for {}!\n".format(enemy["name"], damage)
    else:
        to_return += "{} missed!\n".format(enemy["name"])

    if health_points < 0:
        health_points = 0
    if enemy["hp"] < 0:
        enemy["hp"] = 0

    return to_return


def quick_time():
    # Function to fire at the enemy
    for i in range(5, 0, -1):
        utilities.clear_console()
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
        print("You:\t HP={}\tRounds={}/6".format(health_points, rounds))
        print("{}: HP={}\tRounds={}/6\n".format(enemy["name"], enemy["hp"], enemy["rounds"]))
        print(i)
        time.sleep(1)

    utilities.clear_console()
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
    print("You:\t HP={}\tRounds={}/6".format(health_points, rounds))
    print("{}: HP={}\tRounds={}/6\n".format(enemy["name"], enemy["hp"], enemy["rounds"]))
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
