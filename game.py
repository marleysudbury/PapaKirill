#!/usr/bin/python3

import map
import player
import utilities
import gameparser
import items
import settings
import narratives
import combat
import dancing

win_condition = False
confrontation = False


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
                return "Inspect " + evidence_item["name"] + ": " + evidence_item["description"] + "\n"

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
        player.rounds += 1
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
        if person == "killer":
            global confrontation
            confrontation = True
        return "{0}: '{1}'".format(person["name"], person["speech"])

    return "Speech: there's nobody to speak to.\n"


def execute_command(command):
    # Executes command.
    if 0 == len(command):
        return
    if command[0] == "toggle":
        if len(command) > 1:
            return execute_toggle(command[1])
        else:
            return "Toggle what?\n"
    if command[0] == "talk":
        if len(command) > 1:
            return execute_talk()
        else:
            return "Talk to whom?\n"
    elif command[0] == "go":
        if len(command) > 1:
            return execute_go(command[1])
        else:
            return "Go where?\n"
    elif command[0] == "take":
        if len(command) > 1:
            return execute_take(command[1])
        else:
            return "Take what?\n"
    elif command[0] == "drop":
        if len(command) > 1:
            return execute_drop(command[1])
        else:
            return "Drop what?\n"
    elif command[0] == "inspect":
        if len(command) > 1:
            return execute_inspect(command[1])
        else:
            return "Inspect what?\n"
    elif command[0] == "evidence":
        return execute_evidence()
    elif command[0] == "speech":
        return execute_speech()
    elif command[0] == "exit":
        return "exit"
    else:
        return "This makes no sense.\n"


# Input


def menu(exits, room_items, inv_items, room_characters):
    # Prints menu and accepts input.
    if settings.menu_should_show:
        print_menu(exits, room_items, inv_items, room_characters)
    user_input = input("> ")
    normalised_user_input = gameparser.normalise_input(user_input)
    return normalised_user_input


def render_screen(r, i, o):
    utilities.clear_console()
    print_room(r)
    # print_inventory_items(i)
    if o:
        print(o)


def demo(room_ver):
    if room_ver == 0 and player.current_room == map.rooms["Papa Kirill's"] and len(player.current_room["rooms"][room_ver]['evidence']) == 0:
        map.rooms["Papa Kirill's"]["version"] = 1
    if room_ver == 0 and player.current_room == map.rooms["Andy's Jazz Club"] and len(player.current_room["rooms"][room_ver]['characters']) == 0:
        map.rooms["Andy's Jazz Club"]["version"] = 1
    if room_ver == 1 and player.current_room == map.rooms["Andy's Jazz Club"] and len(player.current_room["rooms"][room_ver]['evidence']) == 0:
        map.rooms["Alleyway"]["version"] = 1
    if room_ver == 1 and player.current_room == map.rooms["Alleyway"] and len(player.current_room["rooms"][room_ver]['evidence']) == 0:
        map.rooms["Alleyway"]["version"] = 2
    if player.current_room == map.rooms["Sewers"]:
        map.rooms["Papa Kirill's"]["version"] = 2
    global confrontation
    if confrontation:
        choice = input("> ")
        if choice == "fight":
            print(combat.combat(player.rounds, player.health_points, player.player_steps))
        else:
            print(dancing.combat(player.rounds, player.health_points, player.player_steps))

        global win_condition
        win_condition = True


def game_director(room_ver):
    demo(room_ver)


# Entry point.
def main():
    # Main loop.
    game_running = True
    # Track output from command executions.
    output = ""
    # While game is running.
    while game_running:
        room_ver = player.current_room["version"]
        this_room = player.current_room['rooms'][room_ver]
        # Render.
        render_screen(this_room, player.inventory, output)
        # Input.
        command = menu(this_room["exits"], this_room["items"], player.inventory, this_room["characters"])
        # Update.
        # Get output of execution.
        output = execute_command(command)
        # Execute game director.
        game_director(room_ver)
        # Check for end-game.
        if win_condition:
            game_running = False
    utilities.clear_console()

    # This is the win screen.
    print("You've done yourself a win, kiddo.")


# Are we being run as a script? If so, run main().
# '__main__' is the name of the scope in which top-level code executes.
# See https://docs.python.org/3.4/library/__main__.html for explanation
if __name__ == "__main__":
    main()
