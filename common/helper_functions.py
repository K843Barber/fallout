import sys  # noqa: D100
from time import sleep

def typewriting(word_input, sleep_time):
    """A small function to begin the page with.
    
    Args:
        word_input: The words that are printed at the start of each page.#
        sleep_time: Pace of printing.
    """
    for char in word_input:
        sleep(sleep_time)
        sys.stdout.write(char)
        sys.stdout.flush()
