# high_scores.py

import curses

def display_high_scores(stdscr, high_scores, score, width, height):
    while True:
        stdscr.clear()
        stdscr.addstr(height // 2 - 2, width // 2 - 6, "GAME OVER")
        stdscr.addstr(height // 2, width // 2 - 8, f"Your Score: {score}")
        stdscr.addstr(height // 2 + 2, width // 2 - 10, "High Scores:")
        for i, hs in enumerate(high_scores[:10]):
            stdscr.addstr(height // 2 + 3 + i, width // 2 - 10, f"{i+1}. {hs}")
        stdscr.addstr(height // 2 + 15, width // 2 - 12, "Press SPACE to restart or ESC to quit")
        stdscr.refresh()

        try:
            key = stdscr.getkey()
            if key == " ":
                return "restart"
            elif key == "\x1b":  # ESC to exit
                return "quit"
        except curses.error:
            pass
