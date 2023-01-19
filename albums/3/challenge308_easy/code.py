'''
This week all challenges will be inspired by the game Flash Point

The game is a fun cooperative game, where a bunch of fire(wo)men try to rescue victims
in a burning building.

Each round the fire is spreading, and it is this mechanic that we are going to implement.
Formal Inputs & Outputs
Input description

You receive a floorplan of the building with the current situation on it.
The floorplan is a grid and all tiles are connected vertically and horizontally.
There is never ever a diagonally interaction.

Here is the legend to what is what:

S <- smoke
F <- fire
# <- wall
| <- closed door
/ <- open door
= <- damaged wall
_ <- broken wall or broken door
  <- Open space (blank space)

After the floorplan you will receive a bunch of coordinates ((0,0)
is top left coord).

Each of these coordinates indicate where smoke develops.
Depending on the tile it lands can have various outcomes:

S -> S becomes F, smoke turns into fire
F -> Nothing happens
# -> invalid move
| -> invalid move
/ -> invalid move
= -> invalid move
_ -> invalid move
  ->   becomes S, Smoke develops on a blank spot

Additional rules:

    Fire and smoke: When smoke is next to a fire itself turns into a fire

    Doors and broken walls: doors and broken walls (or broken doors)
    connect to spaces. This means that if smoke is at one side and fire
    at the other the smoke turns into fire

Small house:

#############/#
#     |       #
#     #       #
#     #       #
#######       #
#     _       #
###############

Small house Input

1 1
1 2
1 3
6 5
4 2
1 1
1 2
5 5
5 5
9 1
5 7
2 2

Output description

Show the final Output

#############/#
#F    |  S    #
#FF   #       #
#F    #       #

#######       #
#    F_F      #
###############

'''

def out_of_maze(w, h, x, y):
    if x >= h:
        return False
    if y >= w:
        return  False
    return True


def update_maze(l, x, y):
    '''if target = " " or "S" '''
    i = l[x][y]
    if i == 'S':
        l[x][y] = 'F'
    elif i == ' ':
        l[x][y] = 'S'
    return l


def update_maze2(l, x, y):
    '''if 'S' next to 'F', turn 'S' 'F'.'''
    i = l[x][y]
    if i == 'F':
        try:
            if l[x][y - 1] == 'S':
                l[x - 1][y] = 'F'
            if l[x][y + 1] == 'S':
                l[x][y + 1] = 'F'
            if l[x - 1][y] == 'S':
                l[x - 1][y] = 'F'
            if l[x + 1][y] == 'S':
                l[x + 1][y] = 'F'
        except IndexError:
            return l
    return l


def update_maze3(l, x, y):
    '''if 'S' next to 'F', turn 'S' to fire.'''
    i = l[x][y]
    if i == 'S':
        try:
            if l[x + 1][y] == 'F':
                l[x][y] = 'F'
            if l[x - 1][y] == 'F':
                l[x][y] = 'F'
            if l[x][y - 1] == 'F':
                l[x][y] = 'F'
            if l[x][y + 1] == 'F':
                l[x][y] = 'F'
        except IndexError:
            return l
    return l


def update_maze4(l, x, y):
    i = l[x][y]
    if l[x][y + 1] == 'F':
        l[x][y] = 'F'
    return l


def fire_fire(l, x, y):
    i = l[x][y]
    j = l[x][y - 1]
    k = l[x][y - 2]
    try:
        if i == 'F' and l[x][y - 1] == 'S':
            l[x][y - 1] = 'F'
    except IndexError:
        pass
    try:
        if i == 'F' and l[x][y + 1] == 'S':
            l[x + 1][y] = 'F'
    except IndexError:
        pass
    try:
        if i == 'S'and (l[x + 1][y] == '_' or l[x + 1][y] == '/') and l[x + 2][y] == 'F':
            l[x][y] = 'F'
        elif l[x][y] == 'S' and (l[x][y - 1] == '_' or l[x][y - 1 == '/']) and l[x][y - 2] == 'F':
            l[x][y] = 'F'
    except IndexError:
        pass
    return l


if __name__ == '__main__':

    maze = '''#############/#
    #     |       #
    #     #       #
    #     #       #
    #######       #
    #     _       #
    ###############'''

    co_ords = '''1 1
    1 2
    1 3
    6 5
    4 2
    1 1
    1 2
    5 5
    5 5
    9 1
    7 5
    2 2'''

    maze = maze.splitlines()
    height_maze = len(maze)
    width_maze = len(maze[0])
    new_maze = []
    for row in maze:
        row = row.strip()
        row = list(row)
        new_maze.append(row)

    co_ords = co_ords.splitlines()

    for co_ord in co_ords:
        co_ord = co_ord.strip()
        x = co_ord[2]
        y = co_ord[0]
        x = int(x)
        y = int(y)
        state = out_of_maze(width_maze, height_maze, x, y)
        if state:
            refresh = update_maze(new_maze, x, y)
            refresh = update_maze2(new_maze, x, y)
            refresh = update_maze3(new_maze, x, y)
            refresh = update_maze4(new_maze, x, y)
            fire_check = fire_fire(new_maze, x, y)
        else:
            continue
        print('x: ',y, 'y: ', x)


        for row in new_maze:
            row = ''.join(row)
            print(row)



    co_ords = '''1 1
        1 2
        1 3
        6 5
        4 2
        1 1
        1 2
        5 5
        5 5
        9 1
        7 5
        2 2'''