import random

# . -> empty space (ghosts and pacman can walk)
# | and - -> wall, no one can go through it
# @ -> our hero: Pacman
# G -> ghosts, they are the bad folks
# P -> pills. Pacman needs to eat them

map = [
    "|--------|",
    "|G..|..G.|",
    "|...PP...|",
    "|G....@|.|",
    "|...P..|.|",
    "|--------|"
]

platforms = ['.', '-', '|', 'P', 'G']
weights = [10, 5, 5, 3, 3]

map = [list(row) for row in map]

for i in range(0,6):
    for j in range(0,10):
        if i == 0 or i == 5:
            pass
        elif j == 0 or j == 9:
            pass
        else:
            map[i][j] = random.choices(platforms, weights=weights)[0]

map[3][3] = '@'

ui_wall = [
	"......",
	"......",
	"......",
	"......"
]

ui_ghost = [
	" .-.  ",
	"| OO| ",
	"|   | ",
	"'^^^' "
]

ui_hero = [
	" .--. ",
	"/ _.-'",
	"\\  '-.",
	" '--' "
]

ui_empty = [
	"      ",
	"      ",
	"      ",
	"      "
]

ui_pill = [
	"      ",
	" .-.  ",
	" '-'  ",
	"      "
]

wall_color = "blue"
ghost_color = "red"
pacman_color = "yellow"
pill_color = "grey"