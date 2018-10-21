#!/usr/bin/python3

from map import *
from player import *
from utilities import *
from gameparser import *
from characters import *


def list_of_items(items):
    # Returns a comma-separated string from a list of items.
    result = ''
    count = len(items)
    for item in items:
        count -= 1
        result += (str(item['name']))
        if count > 0:
            result += ', '
    return result

def print_people(current_room):
    #Prints people in room
    s = "TALK"
    s += " to "
    s += str(current_room["people"])
    s += current_room.upper
    print(s)
    #Pretty sure this is wrong, confused myself

def print_room_items(room):
    # Prints items in a room.
    items = room['items']
    count = len(items)
    if count != 0:
        result = 'There is '
        result += list_of_items(items)
        result += ' here.\n'
        print(result)


def print_inventory_items(items):
    # Prints items in the inventory.
    print('INVENTORY')
    print('')
    result = 'You have '
    count = len(items)
    for item in items:
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


def print_status_bar(hp, r, s):
    # Prints the status bar.
    status = "HP: [{0}/100]   ROUNDS: [{1}/6]   STEPS: [{2}]"
    status_bar = status.format(str(hp), str(r), str(s))
    print(status_bar)


def print_room(room):
    # Prints room information.
    print_status_bar(health_points, rounds, player_steps)
    print('')
    print(room["name"].upper())
    print('')
    print_description(room)
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


def exit_leads_to(exits, direction):
    # Returns the name of the room into which an exit leads.
    return rooms[exits[direction]]["name"]


def print_exit(direction, leads_to):
    # Prints a line of a menu of exits.
    direction_upper = direction.upper()
    direction_equivalent = "({0}){1}".format(direction_upper[0], direction_upper[1:])
    print("GO " + direction_equivalent + " to " + leads_to + ".")


def print_menu(exits, room_items, inv_items):
    # Prints a list of exits and items triggers.
    print("You can:")
    for direction in exits:
        print_exit(direction, exit_leads_to(exits, direction))
    for item in room_items:
        print_room_item(item)
    for item in inv_items:
        print_inventory_item(item)
    print("What do you want to do?")


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
    return direction

def execute_talkto():

    return
def execute_evidence():
    global evidence
    if evidence:
        string_evidence = "Evidence: your evidence includes "
        item_names = []
        for item in evidence:
            item_names.append(item["name"])
        string_evidence += (", ".join(item_names))
        string_evidence += (".\n")
        return string_evidence
    else:
        return "Evidence: you don't have any evidence.\n"

def execute_inspect(evidence_name):
    global current_room
    global evidence
    if current_room["evidence"]:
        for evidence_item in current_room["evidence"]:
            if evidence_name == evidence_item["name"]:
                evidence.append(evidence_item)
                current_room["evidence"].remove(evidence_item)
                return "Inspect: " + evidence_item["description"] + "\n"

    if evidence:
        for evidence_item in evidence:
            if evidence_name == evidence_item["name"]:
                return "Inspect: " + evidence_item["description"] + "\n"
                
    return "Inspect: there's nothing to see.\n"
            

def execute_go(direction, current):
    # Move player or print error text.
    equivalent = equivalent_direction(direction)
    if is_valid_exit(current["exits"], equivalent):
        global current_room
        current_room = rooms[current["exits"][equivalent]]
    else:
        return "You cannot go there.\n"


def execute_take(item_id1, current):
    # Take object or print error text.
    item = pop_room_item(item_id1, current['name'])
    #print('we get here')
    if item:
        inventory.append(item)
    else:
        return "You cannot take that.\n"


def execute_drop(item_id1, current):
    # Drop object or print error text.
    item = pop_inventory_item(item_id1)
    if item:
        current['items'].append(item)
    else:
        return "You cannot drop that.\n"


def execute_command(command, current):
    # Executes command.
    if 0 == len(command):
        return
    if command[0] == "go":
        if len(command) > 1:
            execute_go(command[1], current)
        else:
            return "Go where?\n"
    elif command[0] == "take":
        if len(command) > 1:
            return execute_take(command[1], current)
        else:
            return "Take what?\n"
    elif command[0] == "drop":
        if len(command) > 1:
            return execute_drop(command[1], current)
        else:
            return "Drop what?\n"
    elif command[0] == "inspect":
        if len(command) > 1:
            return execute_inspect(command[1])
        else:
            return "Inspect what?\n"
    elif command[0] == "evidence":
        return execute_evidence()
    else:
        return "This makes no sense.\n"


def menu(exits, room_items, inv_items):
    # Prints menu and accepts input.
    print_menu(exits, room_items, inv_items)
    user_input = input("> ")
    normalised_user_input = normalise_input(user_input)
    return normalised_user_input


# Entry point.
def main():
    # Main loop.
    output = ""
    while True:
        clear_console()
        # Render.
        print_people(current_room["people"])
        print_room(current_room)
        print_inventory_items(inventory)
        if output: print(output)
        # Input.
        command = menu(current_room["exits"], current_room["items"], inventory)
        # Update.
        output = execute_command(command, current_room)



# Are we being run as a script? If so, run main().
# '__main__' is the name of the scope in which top-level code executes.
# See https://docs.python.org/3.4/library/__main__.html for explanation
if __name__ == "__main__":
    main()

