"""
# Authors:  - Marwan Kaouachi
#           - Nikolas Milovanovic
#           - Aymen Soltani
# Start date: 03/01/2023
# End date:   22/01/2023
"""

### Dependecies
import numpy as np

### Global varibales
global start, end, maze

### Functions

# Function to load a maze from a file to a matrix
def load_maze(path: str):
    global maze
    try:
        maze = np.loadtxt(path, dtype=object)
    except:
        print(f"\x1b[31m[ERROR]\x1b[0m: Could not resolve the given path: {path}")
    return maze

# Function that locate the start and end of the maze
def find_s_e(maze):
    global start, end
    
    # Handle errors
    if maze is None: return -1
    if len(maze) == 0: return -1
    
    for i in range(0, len(maze) -1):
        for j in range(0, len(maze) -1):
            if maze[i, j] == "s": 
                start = [i, j]
            if maze[i, j] == "e":
                end = [i, j]

def check_around(position, maze):
        #num ligne of choice
        vlx=position[0]
        #num column of choice
        vly=position[1]

        #get top
        upx=vlx
        upy=vly-1
        up=[upx,upy]

        #get bottom
        dwx=vlx
        dwy=vly+1
        dw=[dwx,dwy]

        #get left
        lex=vlx-1
        ley=vly
        le=[lex,ley]

        #get right
        rix=vlx+1
        riy=vly
        ri=[rix,riy]

        #set a list of all around positions
        poslist=[up, dw, le, ri]

        pos_zero=0
        for elmts in poslist:
            check_pos_x = elmts[0]
            check_pos_y = elmts[1]
            if maze[check_pos_x, check_pos_y]==0:
                pos_zero += 1
        return pos_zero

# Check the bomb count around            
def check_around(position, maze):
    line = int(position[0])
    column = int(position[1])
    bomb_count = 0
    
    # Search for bomb around the coordinates
    if maze[line, column] == 0:
        line_cp = line - 1
        column_cp = column - 1
        
        # Research loop
        for i in range(3):
            column_cp = column - 1
            for j in range(3):
                try:
                    # Find bomb around
                    if maze[line_cp, column_cp] == 1:
                        bomb_count += 1
                    column_cp += 1
                # If coordinates are near edges
                except:
                    pass
        line_cp += 1
        
    return bomb_count

# Faire une fonction qui part de "s", cherche les "0" adjacent et stock les coordonnées 
# test 
maze = load_maze("./maze_files/maze1.txt")

find = find_s_e(maze)
if find == -1: print(f"\x1b[31m[ERROR]\x1b[0m: Invalid parameter, parameter must be an non-empty array")
else:
    print(start)
    print(end)