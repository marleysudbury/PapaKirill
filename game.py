#!/usr/bin/python3

import map
import player
import utilities
import gameparser
import items
import settings
import combat
import art
import dancing
import sfx
import score
import homescreen

win_condition = False


# Utilities.


def equivalent_commands(given, commands):
    # Returns an equivalent direction if one can be found.
    equivalents = {}
    for command in commands:
        first_letter = command[0]
        if first_letter in equivalents:
            is_already_there = True
            length = 1
            while is_already_there:
                equivalent = command[0:length]
                if equivalent in equivalents:
                    length += 1
                else:
                    equivalents[equivalent] = command
        else:
            equivalents[first_letter] = command
    if given in equivalents:
        return equivalents[given]
    elif given in commands:
        return given


def is_valid_exit(exits, chosen_exit):
    # Returns a boolean indicating whether an exit is in a room.
    return chosen_exit in exits


def equivalent_direction(direction):
    # Returns an equivalent direction if one can be found.
    if direction == 'n':
        return 'north'
    if direction == 'e':
        return 'east'
    if direction == 's':
        return 'south'
    if direction == 'w':
        return 'west'
    if direction == 'u':
        return 'up'
    if direction == 'd':
        return 'down'
    return direction


def list_of_items(i):
    # Returns a comma-separated string from a list of items.
    result = ''
    count = len(i)
    for item in i:
        count -= 1
        result += (str(item['name']))
        if count > 0:
            result += ', '
    return result


def exit_leads_to(exits, direction):
    # Returns the name of the room into which an exit leads.
    this_room_name = exits[direction]
    room_ver = map.rooms[this_room_name]["version"]
    this_room_object = map.rooms[this_room_name]
    this_rooms = this_room_object["rooms"]
    this_room = this_rooms[room_ver]
    return this_room["name"]


# Printing.


def print_people(character):
    # Prints people in room.
    s = "TALK"
    s += " to "
    s += str(character["name"])
    print(s)


def print_room_items(room):
    # Prints items in a room.
    i = room['items']
    count = len(i)
    if count != 0:
        result = 'There is '
        result += list_of_items(i)
        result += ' here.\n'
        print(result)


def print_inventory_items(i):
    # Prints items in the inventory.
    print('INVENTORY')
    print('')
    result = 'You have '
    count = len(i)
    for item in i:
        count -= 1
        result += (str(item['name']))
        if count > 0:
            result += ', '
    result += '.\n'
    print(result)


def print_inventory_item(item):
    # Prints an inventory item.
    s = 'DROP '
    name = item['id']
    s += name.upper()
    s += ' to drop your '
    s += name
    print(s)


def print_status_bar():
    # Prints the status bar.
    # global health_points, rounds, player_steps, inventory
    round_count = '   ROUNDS: [{0}/6]'.format(str(player.rounds)) if items.item_revolver in player.inventory else (' ' * 13)
    status = "STEPS: [{2}]   HP: [{0}/100]{1}"
    status_bar = status.format(str(player.health_points), str(round_count), str(player.player_steps))
    print(status_bar)


def print_room(room):
    # Prints room information.
    print_status_bar()
    print('')
    print(room["name"].upper())
    if not player.current_room['visited']:
        print('')
        art.ascii(player.current_room['name'])
        player.current_room['visited'] = True
    print('')
    utilities.print_description(room)
    print('')
    print_room_items(room)


def print_room_item(item):
    # Prints an room item.
    s = 'TAKE '
    name = item['id']
    s += name.upper()
    s += ' to take a '
    s += name
    print(s)


def print_exit(direction, leads_to):
    # Prints a line of a menu of exits.
    direction_upper = direction.upper()
    direction_equivalent = "({0}){1}".format(direction_upper[0], direction_upper[1:])
    print("GO " + direction_equivalent + " to " + leads_to + ".")


def print_menu(exits, room_items, inv_items, room_characters):
    # Prints a list of exits and items triggers.
    print("You can:")
    for direction in exits:
        print_exit(direction, exit_leads_to(exits, direction))
    for item in room_items:
        print_room_item(item)
    for item in inv_items:
        print_inventory_item(item)
    for character in room_characters:
        print_people(character)
    print("What do you want to do?")


# Execution commands.


def execute_evidence():
    if player.evidence:
        string_evidence = "Evidence: your evidence includes "
        item_names = []
        for item in player.evidence:
            item_names.append(item["name"])
        string_evidence += (", ".join(item_names))
        string_evidence += ".\n"
        return "You have {0} pieces of evidence: {1}".format(len(player.evidence), string_evidence)
    else:
        return "Evidence: you don't have any evidence yet.\n"


def execute_speech():
    if player.speech:
        string_speech = "Evidence: your evidence includes "
        item_names = []
        for item in player.speech:
            item_names.append(item["name"])
        string_speech += (", ".join(item_names))
        string_speech += ".\n"
        return string_speech
    else:
        return "Speech: you haven't spoken to anyone yet.\n"


def execute_inspect(evidence_name):
    room_ver = player.current_room["version"]
    evidence = player.current_room["rooms"][room_ver]["evidence"]
    if evidence:
        for evidence_item in evidence:
            # print(evidence_item)
            if evidence_name == evidence_item["id"]:
                player.evidence.append(evidence_item)
                room_name = player.current_room['rooms'][room_ver]['name']
                map.pop_room_evidence(evidence_name, room_name)
                return "Inspecting " + evidence_item["name"] + ": " + evidence_item["description"] + "\n"

    return "Inspect: there's nothing to see.\n"


def execute_go(direction):
    # Move player or print error text.
    room_ver = player.current_room["version"]
    cardinals = ['north', 'east', 'south', 'west', 'up', 'down']
    equivalent = equivalent_commands(direction, cardinals)
    if is_valid_exit(player.current_room["rooms"][room_ver]["exits"], equivalent):
        player.current_room = map.rooms[player.current_room["rooms"][room_ver]["exits"][equivalent]]
        player.player_steps += 1
    else:
        return "You cannot go '{0}'.\n".format(direction)


def execute_take(item_id1):
    # Take object or print error text.
    room_ver = player.current_room["version"]
    item = map.pop_room_item(item_id1, player.current_room["rooms"][room_ver]['name'])
    if item == items.item_bullet:
        if player.rounds < 6:
            player.rounds += 1
        else:
            return "You're already carrying the maximum number of rounds."
    elif item:
        player.inventory.append(item)
    else:
        return "You cannot take '{0}'.\n".format(item_id1)


def execute_toggle(c):
    if c == 'menu':
        settings.toggle_menu()


def execute_drop(item_id1):
    # Drop object or print error text.
    room_ver = player.current_room["version"]
    item = player.pop_inventory_item(item_id1)
    if item:
        player.current_room["rooms"][room_ver]['items'].append(item)
    else:
        return "You cannot drop '{0}'.\n".format(item_id1)


def execute_talk():
    room_ver = player.current_room["version"]
    people = player.current_room["rooms"][room_ver]["characters"]
    if len(people) > 0:
        person = people[0]
        player.speech.append(person)
        room_name = player.current_room['rooms'][room_ver]['name']
        map.pop_room_character(room_name)
        return "{0}: '{1}'".format(person["name"], person["speech"])

    return "Speech: there's nobody to speak to.\n"


def execute_command(command):
    # Executes command.
    if 0 == len(command):
        return
    if command[0] == "toggle" or command[0] == "tog":
        if len(command) > 1:
            return execute_toggle(command[1])
        else:
            return "Toggle what?\n"
    if command[0] == "talk" or command[0] == "ta":
        if len(command) > 1:
            return execute_talk()
        else:
            return "Talk to whom?\n"
    elif command[0] == "go" or command[0] == "g":
        if len(command) > 1:
            return execute_go(command[1])
        else:
            return "Go where?\n"
    elif command[0] == "take" or command[0] == "t":
        if len(command) > 1:
            return execute_take(command[1])
        else:
            return "Take what?\n"
    elif command[0] == "drop" or command[0] == "d":
        if len(command) > 1:
            return execute_drop(command[1])
        else:
            return "Drop what?\n"
    elif command[0] == "inspect" or command[0] == "ins":
        if len(command) > 1:
            return execute_inspect(command[1])
        else:
            return "Inspect what?\n"
    elif command[0] == "evidence" or command[0] == "ev":
        return execute_evidence()
    elif command[0] == "speech" or command[0] == "sp":
        return execute_speech()
    elif command[0] == "exit" or command[0] == "ex":
        return "exit"
    else:
        return "'{0}' makes no sense.\n".format(command)


# Input


def menu(exits, room_items, inv_items, room_characters):
    # Prints menu and accepts input.
    if settings.menu_should_show:
        print_menu(exits, room_items, inv_items, room_characters)
    user_input = input("> ")
    normalised_user_input = gameparser.normalise_input(user_input)
    return normalised_user_input


def render_screen(r, o):
    utilities.clear_console()
    print_room(r)
    if o:
        sfx.type_write(o, 50)
        print('')


first_done = True


def game_director(room_ver):
    # Chicago Police Department

    # Progress Chicago Police Department when all items are picked up.
    if room_ver == 0 and player.current_room == map.rooms["Chicago Police Department"] and len(player.current_room["rooms"][room_ver]['items']) == 0:
        map.rooms["Chicago Police Department"]["version"] = 1
    # Spawn last round by dropping all evidence in Chicago Police Department.
    if player.current_room == map.rooms["Chicago Police Department"] and len(player.evidence) == 7:
        map.rooms["Chicago Police Department"]["version"] = 2

    # Car Park and Delivery Station

    # Progress Car Park and Delivery Station when all evidence is picked up.
    if room_ver == 0 and player.current_room == map.rooms["Car Park and Delivery Station"] and len(player.current_room["rooms"][room_ver]['evidence']) == 0:
        map.rooms["Car Park and Delivery Station"]["version"] = 1
    # Progress Sewers when all evidence is picked up.
    if room_ver == 0 and player.current_room == map.rooms["Sewers"] and len(player.current_room["rooms"][room_ver]['evidence']) == 0:
        map.rooms["Sewers"]["version"] = 1

    # Papa Kirill's

    # Progress Papa Kirill's when all evidence is picked up.
    global first_done
    if first_done and room_ver == 0 and player.current_room == map.rooms["Papa Kirill's"] and len(player.current_room["rooms"][room_ver]['evidence']) == 0:
        map.rooms["Papa Kirill's"]["version"] = 1
        first_done = False
    # Progress Papa Kirill's when Sewers is visited.
    if player.current_room == map.rooms["Sewers"]:
        map.rooms["Papa Kirill's"]["version"] = 2
    # Progress Papa Kirill's when all characters have been spoken to.
    if room_ver == 2 and player.current_room == map.rooms["Papa Kirill's"] and len(player.current_room["rooms"][room_ver]['characters']) == 0:
        map.rooms["Papa Kirill's"]["version"] = 3

    # Andy's Jazz Club

    # Progress Andy's Jazz Club when all characters have been spoken to.
    if room_ver == 0 and player.current_room == map.rooms["Andy's Jazz Club"] and len(player.current_room["rooms"][room_ver]['characters']) == 0:
        map.rooms["Andy's Jazz Club"]["version"] = 1
        map.rooms["Alleyway"]["version"] = 1
    # Progress Andy's Jazz Club when all characters have been spoken to.
    if room_ver == 1 and player.current_room == map.rooms["Andy's Jazz Club"] and len(player.current_room["rooms"][room_ver]['evidence']) == 0:
        map.rooms["Andy's Jazz Club"]["version"] = 2

    # Alleyway

    # Progress Alleyway when all evidence is picked up.
    if room_ver == 1 and player.current_room == map.rooms["Alleyway"] and len(player.current_room["rooms"][room_ver]['evidence']) == 0:
        map.rooms["Alleyway"]["version"] = 2
    # Progress win_condition when Papa Kirill's is complete.
    if room_ver == 3 and player.current_room == map.rooms["Papa Kirill's"] and len(player.current_room["rooms"][room_ver]['characters']) == 0:
        global win_condition
        win_condition = True

def nextpage():
    input("""
Next Page """)

def nexclear():
    nextpage()
    utilities.clear_console()


def run_introscript():
    print("Type: 'skip intro' to skip intro or press ENTER to go through intro")
    imp = str(input("Enter what you want to do: "))
    if imp == "":
        utilities.clear_console()
        art.ascii("detective")
        sfx.type_write("""\
Kirill Sidirov was a praised detective who traveled the world tirelessly in the 1950s. His fame came from his atypical ways of tracing the evidence back to the killer and his ebullience on the crime scenes. Kirill rarely took any rest from his job as he got such a thrill from what he did and, as a consequence, he had slowly neglected his family.
        
After he had heard that his aunt had died, he knew it was time to take a break and pay a visit to his uncle back in Chicago which was the only family he had left.
        """, 50)
        nexclear()
        art.ascii("piste")
        nexclear()
        art.ascii("plane")
        sfx.type_write("""
The plane landed at half-past 5 in the evening at Fort Wayne in Indiana. The sunlight was getting dimmer, and it had suddenly started heavily raining so the moment he spotted the Dodge Meadowbrook he swiftly took a seat and gave the cab driver the address. 
        """, 50)
        nexclear()
        art.ascii("taxi2")
        sfx.type_write("""
Travelling is tiring, and he wished he could sleep, but he couldn't help but notice that as they secluded themselves from the city, the Interstate 94 was getting bumpier. The Dodge now scrambled it's way across the unevenly paved roads, whizzing past bare trees and open farmland. Taking a nap now seemed unthinkable so, as if in a trance, he was now staring carelessly outside listening to the radio playing Traveling Mama Blues by Joe Calicott, a song that brought back a myriad of memories from his childhood. As the song played, Kirill started thinking of how delighted his uncle will be to see him after so many years away.  
        """, 50)
        nexclear()
        sfx.type_write("""
He'd fantasized about the way he'd welcome him. He was hoping that things hadn't changed between them and that he would be received similarly from when he was a boy: a big smile and a freshly made pizza with all of his favorite ingredients.
        """, 50)
        art.ascii("boy")
        nexclear()
        art.ascii("taxi3")
        sfx.type_write("""
As he gazed, he barely noticed that the cab driver was looking at him through the rear-view mirror. He must have been intrigued by his apparent stillness and quickly looked away out of politeness. Kirill turned towards him, and they exchanged a look. To be completely honest Kirill hadn't paid too much attention to the cab driver until then because of the many thoughts that were crossing his mind.
""", 50)
        nexclear()
        sfx.type_write("""
He took a look at him. He was a senior man with protruding wrinkles encrusted in his square face. He had pushed the little hair he had left back and smelled of Faberge Brut. He wore a cardigan sweater over a white t-shirt and large grey pants. His dapperness contrasted with his large blistered worn-out hands which held tightly to the steering wheel as if the car was an animal that he had to control.
""", 50)
        nexclear()
        art.ascii("radio")
        sfx.type_write("""
The radio's volume lowered.

'Sir' said the cab driver, 'excuse me for asking this but I'm curious as to why you suddenly started crying? Are you okay?'

He wasn't even aware that tears had made their way down his face until he'd made that comment. The emotion probably led to it. His question had led to a conversation about their lives, what he did, where he was going...

'What do you think is so special about your uncle, Mr. Sidirov?' Mr. Vidal asked.
""", 50)
        nexclear()
        sfx.type_write("""
'Amongst the many memories I have of him,' Kirill answered, 'his smile is what stands out most about him. I remember that every time he smiles, the corners of his mouth spread to such an extent that they tickle his ears, his eyes reduce to pearls, and diverging wrinkles appear around them.' 
""", 50)
        nexclear()
        sfx.type_write("""
As Kirill said this, he smiled. Then his face darkened; he couldn't help but wonder if his uncle would understand his passion for solving murder cases; would he resent him for not paying him visits or would he tolerate the way he became, living from what he loved doing?

Their dialogue came promptly to an end when the car stopped in front of a dark alleyway leading to a very brightly-light restaurant at the end of it. Kirill paid, got out and waved goodbye. 
""", 50)

        nexclear()
        art.ascii("building")
        sfx.type_write("""
He opened his umbrella and checked the address. He didn’t recognize his surroundings but the number propped on the grey wall in front of him confirmed that this was is where his uncle stays. Quite a bit changed since he was a toddler including two large buildings which stood in front of him. The distance separating these two structures created a narrow alleyway. At the end of this passage was a brightly lit construction. His watch indicated half-past 7, perfect! If his memory was correct his uncle should be in the kitchen right now preparing pizza doughs for the locals who would all come for dinner on Saturdays. He walked on the path, zigzagging around garbage and intoxicated men.
""", 50)
        nexclear()
        sfx.type_write("""
When he arrived at the end of the alleyway, the restaurant stood right in front of him: PAPA KIRILL’S; each letter glimmered with the same neon lighting from when it was inaugurated thirty years earlier. He walked towards the entrance and opened the door. To his left was where the customers would sit down and enjoy a meal but, to his surprise, the restaurant was empty. He swerved right towards the kitchen and the most appalling thing stood in front of him.
""", 50)
        nexclear()
        art.ascii("body")
        sfx.type_write("""
A body was on the floor, his uncle’s body. A puddle of blood surrounded him. Cadavers, Kirill had seen thousands of them in his life as a detective. Yet this was the first time he saw the corpse of someone he cherished. A tear dropped. He started sobbing…

He controlled his feelings and got up. On one of the walls of the kitchen was a list of names and phone numbers attached to them. One of them caught his eye: 

Chicago Police Department: (312) 746-6000 

He took his phone out and attempted to dial the number. It took a few attempts to get it right as his hands were trembling.
""", 50)
        nexclear()
        art.ascii("phone")
        sfx.type_write("""
*Telephone Ringing Sound*...

Nothing, no one answered. He dialed the number again.

*Telephone Ringing Sound*...

“Chicago Police Department,” said the police officer, “how can I help you?”

“I’m on 3028 West Armitage Ave, reporting the death of a middle-aged man,” said Kirill in a rush, ”I repeat, I’m on 3028 West Armitage Ave, my uncle’s dead, send someone!’

“Help is on the way,” said the officer in a relaxed voice, “It will take them some time to reach you as they’re having dinner so stay put”.
""", 50)
        nexclear()
        art.ascii("policecar")
        sfx.type_write("""
Once they finally arrived Kirill was very aggravated, the police car had parked in the middle of the road and only one man came out of it, taking his sweet time to make his way to the restaurant. He opened the door.

“Hello there, I am Bob Smith from the CPD how can I help you,” said Bob Smith as he showed his badge proudly.

Kirill channeled his energy. Breath in, breath out. He had waited an hour for this guy to show up and he didn’t even know what he was dealing with. He knew police forces were incompetent but this was the worst he had ever seen them be.

“My uncle was murdered,” declared Kirill, “follow me”.
""", 50)
        nexclear()
        art.ascii("body")
        sfx.type_write("""
Bob saw the body and scribbled things down on a notepad.

“According to the CPD rule-book,” said Bob Smith, “ in the event that an officer finds a corpse on his own he must report the issue to one of his superiors. I have taken notice of this and will now head back to the…”

“...Are you kidding me?!” exclaimed Kirill, “I’ve waited one hour for you to arrive and this is what you do? Unacceptable! Go ahead, leave this restaurant right now.”

Bob Smith was surprised but completely unfazed by the situation, he walked out and rode his car away.
""", 50)
        nexclear()
        sfx.type_write("""
Kirill thought to himself that he was the only one that could change anything from now on. Matters were now in his own hands. Not only did he vow to solve this case but he vowed to avenge his uncle’s death.
""", 50)
        art.ascii("end")
        input("""
CONGRATS! You have read the introduction to this game, go ahead and press ENTER to start the game, good luck!""")


def run_tutorial():
    # Tutorial.
    utilities.clear_console()
    sfx.type_write("Welcome to Papa Kirill's Pizzeria.", 50)
    print('')
    sfx.type_write("Proudly developed by Team 1.", 50)
    print('')
    input("Press Any Key")
    utilities.clear_console()
    art.ascii('body')
    sfx.type_write("Inspect evidence wherever you see it. Evidence is CAPITALISED so that you can see it.", 50)
    print('')
    sfx.type_write("Inspecting evidence will yield clues about how to progress, and can help you find more ammunition.", 50)
    print('')
    input("Press Any Key")
    utilities.clear_console()


def run_win_screen():
    # This is the win screen.
    sfx.type_write("Ha, try as you might, this is the end.", 50)
    print('')
    sfx.type_write("So, 'detective'.. what will it be? FIGHT or DANCE?", 50)
    print('')
    choice = input("> ")
    if choice == "fight":
        result = combat.combat(player.rounds, player.health_points, player.player_steps)
        sfx.type_write(result, 50)
        print('')
        s = score.calc_score(player.player_steps, player.evidence)
        sfx.type_write(str(s), 50)
    else:
        result = dancing.combat(player.rounds, player.health_points, player.player_steps)
        sfx.type_write(result, 50)
        print('')
        s = score.calc_score(player.player_steps, player.evidence)
        sfx.type_write(str(s), 50)


# Entry point.
def main():
    homescreen.homegame()
    run_introscript()
    run_tutorial()
    game_running = True
    # Track output from command executions.
    output = ""
    # While game is running.
    while game_running:
        room_ver = player.current_room["version"]
        this_room = player.current_room['rooms'][room_ver]
        # Render.
        render_screen(this_room, output)
        # Input.
        command = menu(this_room["exits"], this_room["items"], player.inventory, this_room["characters"])
        # Update.
        # Get output of execution.
        output = execute_command(command)
        # Execute game director.
        game_director(room_ver)
        # Check for end-game.
        global win_condition
        if win_condition:
            game_running = False

    run_win_screen()


# Are we being run as a script? If so, run main().
# '__main__' is the name of the scope in which top-level code executes.
# See https://docs.python.org/3.4/library/__main__.html for explanation
if __name__ == "__main__":
    main()
