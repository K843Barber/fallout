'''
TODO:
Fix order of 0xF
Make sure all words are included                                TENTATIVE
Add > on last line to the right                                 CHECK
Add extra guesses at the bottom
Implement it so that the screen refreshes after each guess      CHECK
Remove a guess counter
print blocks instead of numbers
Fix the counter thing so > leaves after counter zero or match
'''

########################## Imports ##########################
import numpy as np
import pandas as pd
import shutil, sys, os
from time import sleep
from hex_gen import hex_generator
from access_page import access_granted

########################## Load file ##########################
microsoft_word = np.loadtxt('words.txt', dtype='str')

########################## Terminal size ##########################
# print(shutil.get_terminal_size((80, 20))) # Terminal size
########################## Text ##########################
words = "ROBCO INDUSTRIES (TM) TERMLINK PROTOCOL"
words1 = "ENTER PASSWORD NOW"
words2 = "4 ATTEMPT(S) LEFT: \u2585 \u2585 \u2585 \u2585"
random_characters = '!@#$%^&*()_<>'
Keyword = 'Heading'

spacejam = ' '*10

########################## Variables ##########################
N = 60

########################## Functions ##########################
def typewriting(word_input):
    for char in word_input:
        sleep(0.01)
        sys.stdout.write(char)
        sys.stdout.flush()


def screen_printout():
    typewriting(words)
    print()
    typewriting(words1)
    print('\n')
    typewriting(words2)
    print('\n')

    for i, j in zip(range(0, len(left)-30, 30), range(0, N-2, 2)):
        print(f'{logs[j]} {left[i:i+30]}{spacejam}{logs[j+1]} {right[i:i+30]}')
    print(f'{logs[-2]} {left[-30:]}{spacejam}{logs[-1]} {right[-30:]}   ', end='')

def header(countdown, correct):
    os.system('clear')

    if correct == False:

        if countdown == 4:
            words2 = "4 ATTEMPT(S) LEFT: \u2585 \u2585 \u2585 \u2585"
        elif countdown == 3:
            words2 = "3 ATTEMPT(S) LEFT: \u2585 \u2585 \u2585"
        elif countdown == 2:
            words2 = "2 ATTEMPT(S) LEFT: \u2585 \u2585"
        elif countdown == 1:
            words2 = "1 ATTEMPT(S) LEFT: \u2585"
        else:
            words2 = "NO ATTEMPTS LEFT!"
    else:
        words2 = "ACCESS GRANTED!"


    print(words)
    print(words1)
    print()
    print(words2)
    print()



##### words that are length 7. Check how many
L7 = [i for i in microsoft_word if len(i) == 7]
L7_count = 0
for i in microsoft_word:
    if len(i) == 7:
        L7_count += 1

L7_count=0
L7 = [i for i in L7 if "'" not in i]



######################## Collect the 7 letter words ending in 'ing' ########################
############################################################################################
L7_subset = []
for i in L7:
    if i[-3:] == 'ing':
        L7_subset.append(i)



######################### Sample correct word ##################################################
################################################################################################

##### Collect potential matches
potential_matches = []
length_match = 0

for i in L7_subset[:]:
    for j, k in zip(i, range(0,len(i))):
        if j == Keyword[k]:
            length_match+=1
    if length_match>=5:
        potential_matches.append(i.upper())
    length_match=0

Keyword = Keyword.upper()

######################### collect all guess words (11 in all) #########################
#######################################################################################
guess_words = [np.random.choice(potential_matches, 8), np.random.choice(L7,2), [Keyword]]
guess_words = [i.upper() for g in guess_words for i in g]





######################## Randomly place words ########################
######################################################################
template_ = []
array_insert_random_index = np.random.choice(np.setdiff1d(range(50, 850),1), 11)
sorted_array_insert_random_index = np.array(np.sort(array_insert_random_index))


cycle_through_list = 0
for i in range(1, 870):
    if i == sorted_array_insert_random_index[cycle_through_list]:
        template_.append(guess_words[cycle_through_list])
        if cycle_through_list==10:
            pass
        else:
            cycle_through_list+=1
    else:
        template_.append(random_characters[np.random.choice(len(random_characters),1)[0]])


printout = " ".join(template_)
splitter = int((len(printout)+1)/2)
left, right = printout[:splitter], printout[splitter:]
some_array = [left, right]

############################## Generate hex tags ################################


#################################################################################
logs = hex_generator()
logs1 = []
spacer = [' '*65]*32
for i, j in zip(logs, spacer):
    logs1.append(i)
    logs1.append(j)


left, right = left[:900], right[:900]

def failure(fail_vars):
    for i, j in zip(range(0, len(left)-150, 30), range(0, N-10, 2)):
        print(f'{logs[j]} {left[i:i+30]}{spacejam}{logs[j+1]} {right[i:i+30]}')

    for i, j, k in zip(range(len(left)-150, len(left)-60, 30), range(N-10, N-4, 2), range(3)):
        print(f'{logs[j]} {left[i:i+30]}{spacejam}{logs[j+1]} {right[i:i+30]}   {fail_vars[k]}')

    print(f'{logs[-2]} {left[-60:-30]}{spacejam}{logs[-2]} {right[-60:-30]}   ')
    print(f'{logs[-1]} {left[-30:]}{spacejam}{logs[-1]} {right[-30:]}   ', end='')



def success(vars_include):
    for i, j in zip(range(0, len(left)-210, 30), range(0, N-14, 2)):
        print(f'{logs[j]} {left[i:i+30]}{spacejam}{logs[j+1]} {right[i:i+30]}')

    for i, j, k in zip(range(len(left)-210, len(left)-60, 30), range(N-14, N-4, 2), range(5)):
        print(f'{logs[j]} {left[i:i+30]}{spacejam}{logs[j+1]} {right[i:i+30]}   {vars_include[k]}')


    print(f'{logs[-4]} {left[-60:-30]}{spacejam}{logs[-3]} {right[-60:-30]}   ')
    print(f'{logs[-2]} {left[-30:]}{spacejam}{logs[-1]} {right[-30:]}   ')



########################### Main feature running ############################
#############################################################################
os.system('clear')
screen_printout()

def main_loop():
    correct = False
    while_breaker = True

    guess_counter = 4
    while (while_breaker == True) and (guess_counter != 0):
        guess = input(">")

        guess = guess.upper()
        
        if guess != Keyword:
            matching = 0
            for i in range(7):
                if guess[i] == Keyword[i]:
                    matching += 1
                else:
                    pass

            the_fail_guess = ">" + guess
            how_many_match = ">"+str(matching)+"/7 correct"
            fail_vars = [the_fail_guess, ">Entry denied", how_many_match]
            guess_counter-=1
            header(guess_counter, correct)

            failure(fail_vars)


        if guess == Keyword:
            the_guess = ">" + guess
            vars_include = [the_guess, ">Exact match!", ">Please wait", ">while system", ">is accessed."]
            guess_counter-=1

            correct = True
            header(guess_counter, correct)
            success(vars_include)
            while_breaker = False

            sleep(3)
            os.system("clear")
            access_granted()







if __name__ == '__main__':
    main_loop()
# main_loop()





























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
