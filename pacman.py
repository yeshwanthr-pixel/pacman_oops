import random
from termcolor import colored
from ui import *

# ----------------------
# Utility Functions
# ----------------------

def print_board(board, win=False):
    """Render the board with colors."""
    final_color = "green" if win else "red" if not win and game_finished else None

    for row in board:
        for piece in range(4):
            for point in row:
                if point == 'G':
                    print(colored(ui_ghost[piece], final_color or ghost_color), end='')
                elif point in ('|', '-'):
                    print(colored(ui_wall[piece], final_color or wall_color), end='')
                elif point == '@':
                    print(colored(ui_hero[piece], final_color or pacman_color), end='')
                elif point == '.':
                    print(ui_empty[piece] if not final_color else colored(ui_empty[piece], final_color), end='')
                elif point == 'P':
                    print(colored(ui_pill[piece], final_color or pill_color), end='')
            print()
    print()  # space between frames


def find_positions(board, symbol):
    """Return list of (x,y) positions of given symbol in the board."""
    return [(x, y) for x in range(len(board)) for y in range(len(board[x])) if board[x][y] == symbol]


def move_ghosts(board):
    """Move all ghosts randomly."""
    ghosts = find_positions(board, 'G')

    for ghost_x, ghost_y in ghosts:
        possible_moves = [
            (ghost_x, ghost_y + 1),  # right
            (ghost_x + 1, ghost_y),  # down
            (ghost_x, ghost_y - 1),  # left
            (ghost_x - 1, ghost_y)   # up
        ]

        next_x, next_y = random.choice(possible_moves)

        if not (0 <= next_x < len(board) and 0 <= next_y < len(board[0])):
            continue

        target = board[next_x][next_y]
        if target in ('|', '-', 'G'):
            continue
        if target == '@':
            return True  # Pacman eaten

        # update board (direct assignment)
        board[ghost_x][ghost_y] = "."
        board[next_x][next_y] = "G"

    return False


def move_pacman(board, key):
    """Move pacman based on user input. Returns (game_over, win)."""
    pacman = find_positions(board, '@')
    if not pacman:
        return False, False

    x, y = pacman[0]
    next_x, next_y = x, y

    if key == 'a': next_y -= 1
    elif key == 'd': next_y += 1
    elif key == 'w': next_x -= 1
    elif key == 's': next_x += 1
    else:
        return False, False  # invalid input

    if not (0 <= next_x < len(board) and 0 <= next_y < len(board[0])):
        return False, False

    target = board[next_x][next_y]
    if target in ('|', '-'):
        return False, False
    if target == 'G':
        return True, False  # lost

    # update board
    board[x][y] = "."
    board[next_x][next_y] = "@"

    # check pills
    pills_left = sum(row.count('P') for row in board)
    if pills_left == 0:
        return True, True  # win

    return False, False


# ----------------------
# Main Game Loop
# ----------------------

def run_game(board):
    global game_finished
    game_finished = False
    win = False

    while not game_finished:
        print_board(board)

        # move ghosts
        if move_ghosts(board):
            game_finished = True
            win = False
            break

        # move pacman
        key = input("Move (WASD): ").lower()
        game_finished, win = move_pacman(board, key)

    # Final state
    print_board(board, win)
    print("You win! :)" if win else "You lost! :/")


# ----------------------
# Run
# ----------------------
if __name__ == "__main__":
    # Initial map (strings → lists of chars)
    game_map = map

    # Convert each row string → list of characters
    game_map = [list(row) for row in game_map]

    run_game(game_map)
