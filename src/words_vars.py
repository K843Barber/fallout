from .output_function import *

########################## Text ##########################
words = "ROBCO INDUSTRIES (TM) TERMLINK PROTOCOL"
words1 = "ENTER PASSWORD NOW"
words2 = "4 ATTEMPT(S) LEFT: \u2585 \u2585 \u2585 \u2585"
random_characters = '!@#$%^&*()_<>'
spacejam = ' '*10

N=60

logs = hex_generator(N)
# logs1, spacer = [], [' '*65]*30

# for i, j in zip(logs, spacer):
#     logs1.append(i)
#     logs1.append(j)
