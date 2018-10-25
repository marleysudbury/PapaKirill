import sys
from time import sleep

max_length = 50
char_counter = 0


def write_word(w):
    for c in w:
        sys.stdout.write(c)
        sys.stdout.flush()
        sleep(0.04)


def type_write(line_for_printing, line_max_length):
    word_list = line_for_printing.split(' ')
    for word in word_list:
        word_length = len(word)
        if word_length < line_max_length:
            write_word(word + ' ')
            line_max_length -= word_length + 1
        else:
            write_word("\n")
            write_word(word + ' ')
            line_max_length = 50
            line_max_length -= word_length + 1
