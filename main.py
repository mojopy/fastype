# main.py

import curses
import sys
from game_logic import game

if __name__ == "__main__":
    level = None
    practice = False

    if len(sys.argv) > 1:
        if sys.argv[1] == "practice":
            practice = True
            if len(sys.argv) > 2:
                level = sys.argv[2]
        else:
            level = sys.argv[1]

    curses.wrapper(game, level=level, practice=practice)
