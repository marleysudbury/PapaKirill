from player import *
import os


def clear_console():
    # Clears the console.
    os.system('cls' if os.name == 'nt' else 'clear')


def generate_minimap(exits, has_a_weapon):
    # Returns a minimap generated based on a rooms exits.
    minimap_lines = []

    # Minimap line 1.
    minimap_line = '     ┌'
    if 'north' in exits:
        minimap_line += '   '
    else:
        minimap_line += '───'
    minimap_line += '┐'
    minimap_lines.append(minimap_line)

    # Minimap line 2.
    minimap_line = '     '
    if 'west' in exits:
        minimap_line += ' '
    else:
        minimap_line += '│'
    minimap_line += ' '
    minimap_line += 'K' if has_a_weapon else 'k'
    minimap_line += ' '
    if 'east' in exits:
        minimap_line += ' '
    else:
        minimap_line += '│'
    minimap_lines.append(minimap_line)

    # Minimap line 3.
    minimap_line = '     └'
    if 'south' in exits:
        minimap_line += '   '
    else:
        minimap_line += '───'
    minimap_line += '┘'
    minimap_lines.append(minimap_line)
    return minimap_lines


def print_description(room):
    # Prints a room's description.

    description = room['description']
    description_length = len(description)
    line_length = 50
    if description_length < (line_length * 3):
        remainder = (line_length * 3) - description_length
        description += (' ' * remainder)

    has_a_weapon = item_is_in_list('id', 'revolver')
    minimap_lines = generate_minimap(room['exits'], has_a_weapon)

    line_counter = 0
    line_without_minimap = line_length - len(minimap_lines[line_counter])

    char_counter = 0
    description_line = ''
    for char in description:
        if line_counter < len(minimap_lines):
            if char_counter < line_without_minimap:
                char_counter += 1
                description_line += char
            else:
                char_counter = 0
                description_line += char
                description_line += minimap_lines[line_counter] + '\n'
                line_without_minimap = line_length - len(minimap_lines[line_counter])
                line_counter += 1
        else:
            if char_counter < line_length:
                char_counter += 1
                description_line += char
            else:
                char_counter = 0
                line_counter += 1
                description_line += '\n'
    print(description_line)
