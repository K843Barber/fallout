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


def access_granted():
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

    # print(len(words))
    typewriting(first_line)
    typewriting(second_line)
    typewriting(third_line)
    # print(words)
    personal_terminal = 'Personal Terminal "Proto-Boy" Manufactured by RobCo"'
    print('\n')
    print('Personal Terminal "Proto-Boy" Manufactured by RobCo"')
    print('_'*len(personal_terminal))
    print()



# access_granted()
