#!/usr/bin/env python  # noqa: D100


#TODO: Fix order of 0xF
#TODO: Add extra guesses at the bottom
#TODO: Fix the counter thing so > leaves after counter zero or match
#TODO: Tidy code to be more readable

########################## Imports ##########################
from numpy import array, loadtxt, setdiff1d, sort
from numpy.random import choice, random
from random import shuffle
import os
from time import sleep

from src.access_page import access_granted
from src.hermes_page import hermes_granted
from src.output_function import (
    collect_subset, 
    guess_selection, 
    header, 
    failure, 
    screen_printout, 
    success
    )
from src.words_vars import (
    logs,
    N,
    random_characters,
    spacejam,
    words,
    words1,
    words2
    )

########################## Load file ##########################
microsoft_word = loadtxt('data/words.txt', dtype='str')

######################### words that are length 7. Check how many ######################
########################################################################################
Keyword, L7_subset = collect_subset(microsoft_word, 7)
potential_matches, Keyword, other, subb = guess_selection(L7_subset, Keyword)

guess_words = [choice(potential_matches, 8), choice(L7_subset,2), [Keyword]]
guess_words = [i.upper() for g in guess_words for i in g]
shuffle(guess_words)

######################## Randomly place words ########################
######################################################################
array_insert_random_index = choice(setdiff1d(range(50, 1600),1), 11)
sorted_array_insert_random_index = array(sort(array_insert_random_index))

template_ = []
cycle_through_list = 0
for i in range(0, 1800):
    if i == sorted_array_insert_random_index[cycle_through_list]:
        template_.append(guess_words[cycle_through_list])
        if cycle_through_list==10:
            pass
        else:
            cycle_through_list+=1
    else:
        template_.append(random_characters[choice(len(random_characters),1)[0]])

printout = "".join(template_)
splitter = int((len(printout)+1)/2)
left, right = printout[:splitter], printout[splitter-1:]

left, right = left[:900], right[:900]

########################### Main feature running ############################
#############################################################################

def main_loop():
    """Main loop where majority game play is played out."""
    #### Preset conditions
    correct = False
    while_breaker = True
    guess_counter = 4

    while (while_breaker is True) and (guess_counter != 0):

        guess = input(">").upper()

        if len(guess) != len(Keyword):
            matching = 0
            the_fail_guess = f">{guess}"
            how_many_match = f">{matching}/{len(Keyword)} correct"

            fail_vars = [
                         the_fail_guess, 
                         ">Entry denied", 
                         how_many_match
                         ]
            guess_counter-=1

            header(guess_counter, correct, words, words1, words2)
            failure(fail_vars, left, right, logs, spacejam, N)
        
        elif guess != Keyword :
            matching = 0
            for i in range(len(Keyword)):
                if guess[i] == Keyword[i]:
                    matching += 1
                else:
                    pass

            the_fail_guess = f">{guess}"
            how_many_match = f">{matching}/{len(Keyword)} correct"
            fail_vars = [
                         the_fail_guess, 
                         ">Entry denied", 
                         how_many_match
                         ]
            guess_counter-=1

            header(guess_counter, correct, words, words1, words2)
            failure(fail_vars, left, right, logs, spacejam, N)

        if guess == Keyword:
            the_guess = ">" + guess
            vars_include = [
                            the_guess, 
                            ">Exact match!", 
                            ">Please wait", 
                            ">while system", 
                            ">is accessed."
                            ]

            correct = True
            header(guess_counter, correct, words, words1, words2)
            success(vars_include, left, right, logs, spacejam, N)
            while_breaker = False

            sleep(3)
            os.system("clear")

            if random() < 0.5:
                access_granted()
            else:
                hermes_granted()


if __name__ == '__main__':
    os.system('clear')
    screen_printout(left, right, words, words1, words2, N, logs, spacejam)
    main_loop()
