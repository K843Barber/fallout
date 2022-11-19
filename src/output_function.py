import sys, os
from time import sleep
import numpy as np


def hex_generator(N):
    logs = []
    for i in range(N):
        if 0 < np.random.rand(N)[0] <= 0.25:
            logs.append(f'0xF{np.random.choice(np.setdiff1d(range(600, 800),1))}')

        elif 0.25 < np.random.rand(N)[0] <= 0.5:
            if np.random.rand(N)[0] < 0.5:
                logs.append(f'0xF{np.random.choice(np.setdiff1d(range(60, 80),1))}C')
            else:
                logs.append(f'0xF{np.random.choice(np.setdiff1d(range(60, 80),1))}A')

        elif 0.5 < np.random.rand(N)[0] <=0.75:
            if np.random.rand(N)[0] < 0.5:
                logs.append(f'0xF{np.random.choice(np.setdiff1d(range(6, 8),1))}E{np.random.choice(np.setdiff1d(range(0, 10),1))}')
            else:
                logs.append(f'0xF{np.random.choice(np.setdiff1d(range(6, 8),1))}B{np.random.choice(np.setdiff1d(range(0, 10),1))}')        

        else:
                logs.append(f'0xF{np.random.choice(np.setdiff1d(range(6, 8),1))}D{np.random.choice(np.setdiff1d(range(0, 10),1))}')        
    return logs


def typewriting(word_input):
    for char in word_input:
        sleep(0.01)
        sys.stdout.write(char)
        sys.stdout.flush()


def screen_printout(arr_left, arr_right, w0, w1, w2, N, logs, spacejam):
    typewriting(w0)
    print()
    typewriting(w1)
    print('\n')
    typewriting(w2)
    print('\n')

    linebreaker = 30

    for i, j in zip(range(0, len(arr_left)-linebreaker, linebreaker), range(0, N-2, 2)):
        print(f'{logs[j]} {arr_left[i:i+linebreaker]}{spacejam}{logs[j+1]} {arr_right[i:i+linebreaker]}')
    print(f'{logs[-2]} {arr_left[-linebreaker:]}{spacejam}{logs[-1]} {arr_right[-linebreaker:]}   ', end='')


def header(countdown, correct, w0, w1, w2):
    os.system('clear')

    if correct == False:

        if countdown == 4:
            w2 = "4 ATTEMPT(S) LEFT: \u2585 \u2585 \u2585 \u2585"
        elif countdown == 3:
            w2 = "3 ATTEMPT(S) LEFT: \u2585 \u2585 \u2585"
        elif countdown == 2:
            w2 = "2 ATTEMPT(S) LEFT: \u2585 \u2585"
        elif countdown == 1:
            w2 = "1 ATTEMPT(S) LEFT: \u2585"
        else:
            w2 = "NO ATTEMPTS LEFT!"
    else:
        w2 = "ACCESS GRANTED!"

    print(f'{w0}\n{w1}\n\n{w2}\n')


def failure(fail_vars, left, right, logs, spacejam, N):
    for i, j in zip(range(0, len(left)-150, 30), range(0, N-10, 2)):
        print(f'{logs[j]} {left[i:i+30]}{spacejam}{logs[j+1]} {right[i:i+30]}')

    for i, j, k in zip(range(len(left)-150, len(left)-60, 30), range(N-10, N-4, 2), range(3)):
        print(f'{logs[j]} {left[i:i+30]}{spacejam}{logs[j+1]} {right[i:i+30]}   {fail_vars[k]}')

    print(f'{logs[-4]} {left[-60:-30]}{spacejam}{logs[-3]} {right[-60:-30]}   ')
    print(f'{logs[-2]} {left[-30:]}{spacejam}{logs[-1]} {right[-30:]}   ', end='')

def success(vars_include, left, right, logs, spacejam, N):
    for i, j in zip(range(0, len(left)-210, 30), range(0, N-14, 2)):
        print(f'{logs[j]} {left[i:i+30]}{spacejam}{logs[j+1]} {right[i:i+30]}')

    for i, j, k in zip(range(len(left)-210, len(left)-60, 30), range(N-14, N-4, 2), range(5)):
        print(f'{logs[j]} {left[i:i+30]}{spacejam}{logs[j+1]} {right[i:i+30]}   {vars_include[k]}')

    print(f'{logs[-4]} {left[-60:-30]}{spacejam}{logs[-3]} {right[-60:-30]}   ')
    print(f'{logs[-2]} {left[-30:]}{spacejam}{logs[-1]} {right[-30:]}   ')


def guess_selection(the_words, Keyword):

    potential_matches, other = [], []
    length_match = 0

    for i in the_words:
        for j, k in zip(i, range(0,len(i))):
            if j == Keyword[k]:
                length_match+=1
        if length_match>=np.floor(len(Keyword)/2):
            potential_matches.append(i)
        length_match=0

    subset_to_not_match = [potential_matches, Keyword]
    subset_to_not_match = [i for g in subset_to_not_match for i in g]

    for i in the_words:
        if i in subset_to_not_match:
            pass
        else:
            other.append(i)

    return potential_matches, Keyword, other, subset_to_not_match

def collect_subset(wordlist, letter_length):
    L7 = [i for i in wordlist if len(i) == letter_length]
    L7_subset = [i for i in L7 if "'" not in i]
    L7_subset = [i.upper() for i in L7_subset]
    Keyword = np.random.choice(L7_subset, 1)[0]
    L7_subset = np.unique(L7_subset)
    
    return Keyword, L7_subset
