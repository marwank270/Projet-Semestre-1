"""
# Authors:  - Marwan Kaouachi
#           - Nikolas Milovanovic
#           - Aymen Soltani
# Start date: 03/01/2023
# End date:   22/01/2023
"""

# Dependecies
import numpy as np

# Functions
def load_maze(path: str):
    maze = np.loadtxt(path)
    return maze

def create_matrix(height, width): # Matrix Creation function
    return np.zeros((height, width), dtype = np.int32)


# test 
maze = load_maze("./maze_files/Maze1.txt")