'''
TODO:
Fix order of 0xF
Make sure all words are included                                CHECK
Add > on last line to the right                                 CHECK
Add extra guesses at the bottom
Implement it so that the screen refreshes after each guess      CHECK
Remove a guess counter                                          CHECK
print blocks instead of numbers                                 CHECK
Fix the counter thing so > leaves after counter zero or match
Make sure keyword isn't repeated                                CHECK
Make dynamic with new words                                     CHECK
Tidy code to be more readable
'''

########################## Imports ##########################
import numpy as np
import pandas as pd
import shutil, sys, os, random
from time import sleep

from src.access_page import access_granted
from src.output_function import *
from src.words_vars import *


########################## Load file ##########################
microsoft_word = np.loadtxt('data/words.txt', dtype='str')

######################### words that are length 7. Check how many ##########################
############################################################################################
L7 = [i for i in microsoft_word if len(i) == 7]
L7_subset = [i for i in L7 if "'" not in i]
Keyword = np.random.choice(L7_subset, 1)[0]

######################## Collect the 7 letter words ending in 'ing' ########################
############################################################################################
L7_subset = np.unique(L7_subset)

################################### Sample correct word ########################################
################################################################################################
##### Collect potential matches
potential_matches = []
length_match = 0

for i in L7_subset:
    for j, k in zip(i, range(0,len(i))):
        if j == Keyword[k]:
            length_match+=1
    if length_match>=np.floor(len(Keyword)/2):
        potential_matches.append(i.upper())
    length_match=0

Keyword = Keyword.upper()

######################### collect all guess words (11 in all) #########################
#######################################################################################
# guess_words = np.unique(guess_words)

guess_words = [np.random.choice(potential_matches, 8), np.random.choice(L7_subset,2), [Keyword]]
guess_words = [i.upper() for g in guess_words for i in g]
random.shuffle(guess_words)


######################## Randomly place words ########################
######################################################################
#### I think this is where the fine-tuning of the output will be ####
array_insert_random_index = np.random.choice(np.setdiff1d(range(50, 1600),1), 11)
sorted_array_insert_random_index = np.array(np.sort(array_insert_random_index))


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
        template_.append(random_characters[np.random.choice(len(random_characters),1)[0]])


printout = "".join(template_)
splitter = int((len(printout)+1)/2)
left, right = printout[:splitter], printout[splitter-1:]

left, right = left[:900], right[:900]




########################### Main feature running ############################
#############################################################################

def main_loop():
    #### Preset conditions
    correct = False
    while_breaker = True
    guess_counter = 4

    while (while_breaker == True) and (guess_counter != 0):

        guess = input(">")
        guess = guess.upper()

        if len(guess) != len(Keyword):
            matching = 0
            the_fail_guess = ">" + guess
            how_many_match = ">"+str(matching)+"/"+str(len(Keyword))+" correct"
            fail_vars = [the_fail_guess, ">Entry denied", how_many_match]
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

            the_fail_guess = ">" + guess
            how_many_match = ">"+str(matching)+"/"+str(len(Keyword))+" correct"
            fail_vars = [the_fail_guess, ">Entry denied", how_many_match]
            guess_counter-=1
            header(guess_counter, correct, words, words1, words2)

            failure(fail_vars, left, right, logs, spacejam, N)



        if guess == Keyword:
            the_guess = ">" + guess
            vars_include = [the_guess, ">Exact match!", ">Please wait", ">while system", ">is accessed."]

            correct = True
            header(guess_counter, correct, words, words1, words2)
            success(vars_include, left, right, logs, spacejam, N)
            while_breaker = False

            sleep(3)
            os.system("clear")
            access_granted()







if __name__ == '__main__':
    os.system('clear')
    screen_printout(left, right, words, words1, words2, N, logs, spacejam)
    main_loop()





























# print()
            # sleep(5)

            # os.system('clear')

# [print(i) for i in range(0, 900, 30)]


    #     if guess_counter==4:
    #         break

    #     # print(guess_counter)
#############################################################################



# left, right = left[:900], right[:900]




# for i, j in zip(range(0, len(left)-30, 30), range(0, N-2, 2)):
#     print(f'{logs[j]} {left[i:i+30]}{spacejam}{logs[j+1]} {right[i:i+30]} {i,j}')
# print(f'{logs[-2]} {left[-30:]}{spacejam}{logs[-1]} {right[-30:]}   ', end='')

# print('\n\n')



# guess='heading'
# the_guess = ">" + guess
# vars_include = [the_guess, ">Exact match!", ">Please wait", ">while system", ">is accessed."]


# for i, j in zip(range(0, len(left)-240, 30), range(0, N-14, 2)):
#     print(f'{logs[j]} {left[i:i+30]}{spacejam}{logs[j+1]} {right[i:i+30]} {i,j}')

# for i, j, k in zip(range(len(left)-210, len(left)-60, 30), range(N-14, N-4, 2), range(5)):
#     print(f'{logs[j]} {left[i:i+30]}{spacejam}{logs[j+1]} {right[i:i+30]}  {vars_include[k]} {i,j}')


# print(f'{logs[-4]} {left[-60:-30]}{spacejam}{logs[-3]} {right[-60:-30]}   ')

# print(f'{logs[-2]} {left[-30:]}{spacejam}{logs[-1]} {right[-30:]}   ', end='')




# print(len(left), len(right))




# print(spacer)
# logs1 = ''.join(logs)
# spacer = ' '*60
# print(' '*80)

# print(''.join(logs1))
# for K in range(0, len(left), 66):
#     # print(i, i+1)
#     for i, j in enumerate(left[K:K+66]):
#         print( j, end='')
#     for i in range(0, 10):
#         print(' ', end='')
#     for i, j in enumerate(left[K:K+66]):
#         print(j, end='')

# print('\n\n')
# for i, j in zip(range(0, len(left)-30, 30), range(0, N, 2)):
#     # print(i, j)
#     print(f'{logs[j]} {left[i:i+30]}{spacejam}{logs[j+1]} {right[i:i+30]} {i,j}')


# print(Keyword)
#------------ Combine ------------
# for i in range(32):
#     print(np.random.choice(np.setdiff1d(range(100, 999),1)))

# for K in range(0, len(left), 66):
#     # print(i, i+1)
#     for i, j in enumerate(left[K:K+66]):
#         print( j, end='')
#     for i in range(0, 10):
#         print(' ', end='')
#     for i, j in enumerate(left[K:K+66]):
#         print(j, end='')
#------------ Combine ------------

# print(words)
# print(words1)
# print()
# print(words2)
# print()


# # print(len(left)/30)
# for i, j in zip(range(0, len(left)-30, 30), range(0, N, 2)):
#     # print(i, j)
#     print(f'{logs[j]} {left[i:i+30]}{spacejam}{logs[j+1]} {right[i:i+30]} {i,j}')

# print(len(left))


# print(f'{logs[-1]} {left[-30:]}{spacejam}{logs[-1]} {right[-30:]}   ', end='')

# guess = input(">")
# # while True:

# guess = guess.upper()
# the_guess = ">" + guess


# for i in logs:
#     print(i)

# vars_include = [the_guess, ">Exact match!", ">Please wait", ">while system", ">is accessed."]

# for i, j in zip(range(0, len(left)-210, 30), range(18)):
#     print(i, j)


#     print(f'{logs[j]} {left[i:i+30]}{spacejam}{logs[j]} {right[i:i+30]}')
# for i, j, k in zip(range(0, 150, 30), range(18, 28), range(5)):
#     print(f'{logs[j]} {left[i-210:i-210+30]}{spacejam}{logs[j]} {right[i-210:i-210+30]}  {vars_include[k]}')
# print(f'{logs[-2]} {left[-60:-30]}{spacejam}{logs[-2]} {right[-60:-30]}   ')








    # if guess == Keyword:
# the_guess = ">" + guess
# vars_include = [the_guess, ">Exact match!", ">Please wait", ">while system", ">is accessed."]

# for i, j in zip(range(0, len(left)-210, 30), range(18)):
#     print(f'{logs[j]} {left[i:i+30]}{spacejam}{logs[j]} {right[i:i+30]}')
# for i, j, k in zip(range(0, 150, 30), range(18, 28), range(5)):
#     print(f'{logs[j]} {left[i-210:i-210+30]}{spacejam}{logs[j]} {right[i-210:i-210+30]}  {vars_include[k]}')
# print(f'{logs[-2]} {left[-60:-30]}{spacejam}{logs[-2]} {right[-60:-30]}   ')

# print(f'{logs[-1]} {left[-30:]}{spacejam}{logs[-1]} {right[-30:]}   ', end='')
# input(">")
    # else:
    #     matching = 0
    #     for i in range(7):
    #         if guess[i] == Keyword[i]:
    #             matching += 1
    #         else:
    #             pass
    #     print(">" + guess)
    #     print(">Entry Denied")
    #     print(f">{matching}/7 correct.")
# print(right)


# 11 words
# 9 end with 'ing'
# 2 do not
