"""TODO: Add more details here (check what Fallout has)."""

import os
from shutil import get_terminal_size

from common.helper_functions import typewriting

screen_size_mid = int(get_terminal_size((80, 20))[0]/2) # Terminal size


def starting_point(w):
    """Where to start printing on each line.
    
    Args:
        w: Width of screen.
    """
    if len(w)%2 == 0:
        start_location = int(screen_size_mid - len(w)/2)
    elif len(w)%2 == 1:
        start_location = int(screen_size_mid - (len(w)+1)/2)
    blank_spaces = " "*start_location
    
    return blank_spaces


def access_granted():
    """Function to output the Access granted screen."""
    os.system("clear")

    words = "ROBCO INDUSTRIES UNIFIED OPERATING SYSTEM"
    words1 = "COPYRIGHT 2075-2077 ROBCO INDUSTRIES"
    words2 = "-Server 1-"

    blank_spaces1 = starting_point(words)
    blank_spaces2 = starting_point(words1)
    blank_spaces3 = starting_point(words2)

    first_line = blank_spaces1 + words + blank_spaces1
    second_line = blank_spaces2 + words1 + blank_spaces2
    third_line = blank_spaces3 + words2 + blank_spaces3

    typewriting(first_line, 0.05)
    typewriting(second_line, 0.05)
    typewriting(third_line, 0.05)

    personal_terminal = 'Personal Terminal "Proto-Boy" Manufactured by RobCo"'
    print('\n')
    print(personal_terminal)
    print('_'*len(personal_terminal))
    print()
    print(" > New Canaan Branch Proposal")
    print(" > Re: Henry Jamison")

