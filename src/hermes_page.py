'''
TODO:
Add more details here (check what Fallout has)
'''

import os, shutil, sys
from time import sleep

screen_size_mid = int(shutil.get_terminal_size((80, 20))[0]/2) # Terminal size


def typewriting(word_input):
    for char in word_input:
        sleep(0.005)
        sys.stdout.write(char)
        sys.stdout.flush()

def starting_point(w):
    if len(w)%2 == 0:
        start_location = int(screen_size_mid - len(w)/2)
    elif len(w)%2 == 1:
        start_location = int(screen_size_mid - (len(w)+1)/2)
    blank_spaces = " "*start_location
    
    return blank_spaces


def hermes_granted():
    os.system("clear")

    words = "ROBCO INDUSTRIES UNIFIED OPERATING SYSTEM"
    words1 = "COPYRIGHT 2075-2077 ROBCO INDUSTRIES"
    words2 = "-Server 6-"

    blank_spaces1 = starting_point(words)
    blank_spaces2 = starting_point(words1)
    blank_spaces3 = starting_point(words2)

    first_line = blank_spaces1 + words + blank_spaces1
    second_line = blank_spaces2 + words1 + blank_spaces2
    third_line = blank_spaces3 + words2 + blank_spaces3

    typewriting(first_line)
    typewriting(second_line)
    typewriting(third_line)

    hermes_terminal0 = 'Hermes Communications, Inc.'
    hermes_terminal1 = 'Black Mountain Submatrix'
    hermes_terminal2 = 'System Online'
    fourth_line = '_'*len(hermes_terminal0)
    print(f'\n{hermes_terminal0}\n{hermes_terminal1}\n{hermes_terminal2}')
    print(fourth_line)
 
    print(f'\n> Marcus made me type this')
    print(f"> It's a radio station!")
    print("> On the air!")
    print("> The elite!")
    print("> Alone at last")
    print("> Safe!")
    print("> Lucky!")
 