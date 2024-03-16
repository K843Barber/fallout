import os  # noqa: D100
from numpy.random import choice, rand
from numpy import floor, setdiff1d, unique

from common.helper_functions import typewriting

def hex_generator(N):
    """A function to generate the main output.
    
    Args:
        N: A value, undetermined what exactly it is for yet.
    """
    logs = []
    for i in range(N):
        if 0 < rand(N)[0] <= 0.25:
            logs.append(f'0xF{choice(setdiff1d(range(600, 800),1))}')

        elif 0.25 < rand(N)[0] <= 0.5:
            if rand(N)[0] < 0.5:
                logs.append(f'0xF{choice(setdiff1d(range(60, 80),1))}C')
            else:
                logs.append(f'0xF{choice(setdiff1d(range(60, 80),1))}A')

        elif 0.5 < rand(N)[0] <=0.75:
            if rand(N)[0] < 0.5:
                logs.append(f'0xF{choice(setdiff1d(range(6, 8),1))}E'
                            f'{choice(setdiff1d(range(0, 10),1))}')
            else:
                logs.append(f'0xF{choice(setdiff1d(range(6, 8),1))}B'
                            f'{choice(setdiff1d(range(0, 10),1))}')        

        else:
                logs.append(f'0xF{choice(setdiff1d(range(6, 8),1))}D'
                            f'{choice(setdiff1d(range(0, 10),1))}')        
    return logs


# Needs a rewrite
def screen_printout(arr_left, arr_right, w0, w1, w2, N, logs, spacejam):
    """A prinout of the entire screen.
    
    Args:
        arr_left: The left side of the screen.
        arr_right: The right side of the screen.
        w0: Word line zero.
        w1: Word line one.
        w2: Word line two.
        N: Number of lines...I think.
        logs: The output.
        spacejam: Space creator.
    """
    typewriting(w0, 0.01)
    print()
    typewriting(w1, 0.01)
    print('\n')
    typewriting(w2, 0.01)
    print('\n')

    linebreaker = 30

    for i, j in zip(range(0, len(arr_left)-linebreaker, linebreaker), range(0, N-2, 2)):
        print(f'{logs[j]} {arr_left[i:i+linebreaker]}{spacejam}{logs[j+1]} '
              f'{arr_right[i:i+linebreaker]}')
    print(f'{logs[-2]} {arr_left[-linebreaker:]}{spacejam}{logs[-1]} '
          f'{arr_right[-linebreaker:]}   ', end='')


def header(countdown, correct, w0, w1, w2):
    """Section of the screen that deals with the countdown of correct answers.
    
    Args:
        countdown: A counter to check number of attempts.
        correct: A boolean to return if access is granted or not.
        w0: First line of text found in word_vars.
        w1: Second line of text found in word_vars.
        w2: Guess countdown.
    """
    os.system('clear')

    if correct is False: # Better way to do this statement

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


# has to be a nicer way to write this
def failure(fail_vars, left, right, logs, spacejam, N):
    """A function that returns the failed output.
    
    Args:
        fail_vars: An array of failed inputs.
        left: Left side of panel split.
        right: Right side of panel split.
        logs: The logged input.
        spacejam: A space var.
        N: Number of lines (I think).
    """
    for i, j in zip(range(0, len(left)-150, 30), range(0, N-10, 2)):
        print(f'{logs[j]} {left[i:i+30]}{spacejam}{logs[j+1]} {right[i:i+30]}')

    for i, j, k in zip(range(len(left)-150, len(left)-60, 30), 
                       range(N-10, N-4, 2), 
                       range(3)):
        print(f'{logs[j]} {left[i:i+30]}{spacejam}{logs[j+1]} '
              f'{right[i:i+30]}   {fail_vars[k]}')

    print(f'{logs[-4]} {left[-60:-30]}{spacejam}{logs[-3]} {right[-60:-30]}   ')
    print(f'{logs[-2]} {left[-30:]}{spacejam}{logs[-1]} {right[-30:]}   ', end='')

# perhaps merge with above function to minimise DRY
def success(vars_include, left, right, logs, spacejam, N):
    """A function that returns the success output.
    
    Args:
        vars_include: Output on success.
        left: Left side of panel split.
        right: Right side of panel split.
        logs: The logged input.
        spacejam: A space var.
        N: Number of lines (I think).
    """
    for i, j in zip(range(0, len(left)-210, 30), range(0, N-14, 2)):
        print(f'{logs[j]} {left[i:i+30]}{spacejam}{logs[j+1]} {right[i:i+30]}')

    for i, j, k in zip(range(len(left)-210, len(left)-60, 30), 
                       range(N-14, N-4, 2), 
                       range(5)):
        print(f'{logs[j]} {left[i:i+30]}{spacejam}{logs[j+1]} '
              f'{right[i:i+30]}   {vars_include[k]}')

    print(f'{logs[-4]} {left[-60:-30]}{spacejam}{logs[-3]} {right[-60:-30]}   ')
    print(f'{logs[-2]} {left[-30:]}{spacejam}{logs[-1]} {right[-30:]}   ')


def guess_selection(the_words, Keyword):
    """A function that collects the words for guessing.
    
    Args:
        the_words: A list of words for input.
        Keyword: The given word for gaining access.
        
    Returns:
        potential_matches: Potential matches to password.
        Keyword: The password
        other: Unsure as of now
        subset_to_not_match: A list of words that don't match (I think).
    """
    potential_matches, other = [], []
    length_match = 0

    for i in the_words:
        for j, k in zip(i, range(0,len(i))):
            if j == Keyword[k]:
                length_match+=1
        if length_match>=floor(len(Keyword)/2):
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
    """Collect the keywords and whichever subset.

    Args:
        wordlist: The entire wordlist.
        letter_length: Letters of particular length we want.
    
    Returns:
        Keyword: The keyword we are after.
        L7_subset: The subset of words we want on given length.
    """
    L7 = [i for i in wordlist if len(i) == letter_length]
    L7_subset = [i for i in L7 if "'" not in i]
    L7_subset = [i.upper() for i in L7_subset]
    Keyword = choice(L7_subset, 1)[0]
    L7_subset = unique(L7_subset)
    
    return Keyword, L7_subset
