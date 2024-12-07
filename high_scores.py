# high_scores.py

import curses

def display_high_scores(stdscr, high_scores, score, width, height):
    stdscr.clear()
    stdscr.addstr(0, 0, "GAME OVER")
    stdscr.addstr(2, 0, f"Your Score: {score}")
    stdscr.addstr(4, 0, "High Scores:")

    # Dynamically position scores to fit within the screen
    max_scores_to_show = min(10, height - 10)  # Ensure it fits within the terminal
    for i, hs in enumerate(high_scores[:max_scores_to_show]):
        stdscr.addstr(6 + i, 0, f"{i + 1}. {hs}")

    # Adjust the position of the action prompt
    prompt_y = min(height - 2, 6 + max_scores_to_show + 2)
    stdscr.addstr(prompt_y, 0, "Press SPACE to restart or ESC to quit")
    stdscr.refresh()

    # Wait for the user's input
    while True:
        key = stdscr.getch()
        if key in (32, 27):  # SPACE (32) or ESC (27)
            return key