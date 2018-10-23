from player import *
import os
from game import room_ver


def shortcut_word(word):
    upper = word.upper()
    string = "({0}){1}"
    return string.format(upper[0], upper[1:])


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
    # line_without_minimap = line_length - len(minimap_lines[line_counter])

    word_counter = 0
    new_desc = description.split(' ')
    two_words = [False, False]
    while word_counter < len(new_desc) - 1:
        new_line = ""
        if two_words[1]:
            new_line += "\n"
            new_line += two_words[1]
            new_line += " "
            two_words = [False, False]
        if line_counter < len(minimap_lines):
            while len(new_line) + len(new_desc[word_counter]) + len(minimap_lines[line_counter]) + 1 < line_length:
                new_line += new_desc[word_counter]
                new_line += " "
                word_counter += 1
            while len(new_line) + len(minimap_lines[line_counter]) < line_length:
                new_line += " "
            new_line += minimap_lines[line_counter]
        else:
            while (word_counter < len(new_desc) -1) and len(new_line) + len(new_desc[word_counter]) + 1 < line_length:
                if "\n\n" in new_desc[word_counter]:
                    two_words = new_desc[word_counter].split("\n\n")
                    # print(two_words)
                    new_line += two_words[0]
                    word_counter += 1
                    # print("BREAKING")
                    break
                new_line += new_desc[word_counter]
                new_line += " "
                word_counter += 1

        print(new_line)
        line_counter += 1

    """        
    for char in description:
        if char == "\n":
            char_counter = 0
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
                description_line += char
                description_line += '\n'
    print(description_line)
    """
