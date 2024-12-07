# game_logic.py

import curses
import random
import time
from data_manager import load_words, save_high_scores, load_high_scores, save_last_level, load_last_level
from high_scores import display_high_scores
from constants import BASE_SPEED, MILESTONES, MILESTONE_SPEED_INCREMENT

def game(stdscr, level=None, practice=False):
    curses.curs_set(0)
    stdscr.nodelay(1)

    words_data = load_words("words.json")
    levels = sorted(words_data.keys())
    if level is None:
        level = load_last_level() or levels[0]  # Default to last level or Level 1

    if level not in words_data:
        stdscr.addstr(0, 0, f"Invalid level: {level}. Available levels: {', '.join(levels)}")
        stdscr.getch()
        return

    save_last_level(level)

    height, width = stdscr.getmaxyx()
    score = 0
    lives = 3
    falling_speed = BASE_SPEED
    user_input = ""
    word_y = 0
    falling_word = random.choice(words_data[level])
    word_x = (width - len(falling_word)) // 2

    high_scores = load_high_scores()
    next_milestone_index = 0
    last_fall_time = time.time()

    while lives > 0:
        stdscr.clear()

        # Draw falling word
        stdscr.addstr(word_y, word_x, falling_word)

        # Draw user input, score, and lives
        stdscr.addstr(height - 2, 0, f"Type: {user_input}")
        stdscr.addstr(0, 0, f"Score: {score}  Lives: {lives}  Level: {level}")

        try:
            key = stdscr.getkey()
            if key == " ":
                if user_input == falling_word:
                    score += len(falling_word) * (levels.index(level) + 1)
                    falling_word = random.choice(words_data[level])
                    word_x = (width - len(falling_word)) // 2
                    word_y = 0
                    user_input = ""

                    if next_milestone_index < len(MILESTONES) and score >= MILESTONES[next_milestone_index]:
                        falling_speed = max(50, falling_speed - MILESTONE_SPEED_INCREMENT)
                        next_milestone_index += 1
                else:
                    lives -= 1
                    falling_word = random.choice(words_data[level])
                    word_x = (width - len(falling_word)) // 2
                    word_y = 0
                    user_input = ""
            elif key == "\x1b":
                break
            elif key == "\b" or key == "\x7f":
                user_input = user_input[:-1]
            else:
                user_input += key
        except curses.error:
            pass

        if time.time() - last_fall_time > falling_speed / 1000:
            word_y += 1
            last_fall_time = time.time()

        if word_y >= height - 2:
            lives -= 1
            falling_word = random.choice(words_data[level])
            word_x = (width - len(falling_word)) // 2
            word_y = 0
            user_input = ""

        stdscr.refresh()

    high_scores.append(score)
    high_scores.sort(reverse=True)
    save_high_scores(high_scores)

    action = display_high_scores(stdscr, high_scores, score, width, height)
    if action == "restart":
        game(stdscr, level=level, practice=practice)
