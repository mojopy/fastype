import curses
import random
import time

# Word list for the game
words = ["python", "linux", "terminal", "curses", "keyboard", "game", "falling", "type"]

def main(stdscr):
    curses.curs_set(0)  # Hide the cursor
    stdscr.nodelay(1)   # Make getch() non-blocking
    stdscr.timeout(100) # Refresh every 100ms

    height, width = stdscr.getmaxyx()  # Get terminal size
    score = 0
    lives = 3
    falling_word = random.choice(words)
    word_x = (width - len(falling_word)) // 2  # Always center horizontally
    word_y = 0
    user_input = ""

    while lives > 0:
        stdscr.clear()

        # Draw the word falling
        stdscr.addstr(word_y, word_x, falling_word)

        # Draw the user input
        stdscr.addstr(height - 2, 0, f"Type: {user_input}")

        # Draw score and lives
        stdscr.addstr(0, 0, f"Score: {score}  Lives: {lives}")

        # Check for user input
        try:
            key = stdscr.getkey()
            if key == " ":  # If Enter is pressed, check the word
                if user_input == falling_word:
                    score += 1
                    falling_word = random.choice(words)
                    word_x = (width - len(falling_word)) // 2  # Recalculate for the new word
                    word_y = 0
                user_input = ""
            elif key == "\x1b":  # Exit on ESC key
                break
            elif key == "\b" or key == "\x7f":  # Handle backspace
                user_input = user_input[:-1]
            else:
                user_input += key
        except:
            pass

        # Move the word down
        word_y += 1

        # If the word reaches the bottom
        if word_y >= height - 2:
            lives -= 1
            falling_word = random.choice(words)
            word_x = (width - len(falling_word)) // 2  # Recalculate for the new word
            word_y = 0
            user_input = ""

        # Refresh the screen
        stdscr.refresh()

        time.sleep(0.1)  # Control the speed of the game

    # Game over screen
    stdscr.clear()
    stdscr.addstr(height // 2, width // 2 - 6, "GAME OVER")
    stdscr.addstr(height // 2 + 1, width // 2 - 8, f"Your Score: {score}")
    stdscr.refresh()
    stdscr.getch()

# Run the game
curses.wrapper(main)
