# 3) Rework one of these programs using Numpy
# Write a function that takes a two-dimensional array as an argument and outputs
# a maze drawn with tiles corresponding to this array:
#
# maze = [[NP, NP, BR, LR],
#         [BR, LR, TL, NP],
#         [BR, LR, TL, NP]]

import numpy as np


def make_maze(maze):
    result = ""
    for row in maze:
        line1 = ""
        line2 = ""
        line3 = ""
        for tile in row:
            line1 = line1 + tile[0][0] + tile[0][1] + tile[0][2]
            line2 = line2 + tile[1][0] + tile[1][1] + tile[1][2]
            line3 = line3 + tile[2][0] + tile[2][1] + tile[2][2]
        result = result + line1 + "\n" + line2 + "\n" + line3 + "\n"
    return result


# USAGE
if __name__ == '__main__':
    NP = [["#", "#", "#"],
          ["#", "#", "#"],
          ["#", "#", "#"]]

    LR = [["#", "#", "#"],
          [" ", " ", " "],
          ["#", "#", "#"]]

    TL = [["#", " ", "#"],
          [" ", " ", "#"],
          ["#", "#", "#"]]

    BR = [["#", "#", "#"],
          ["#", " ", " "],
          ["#", " ", "#"]]

    user_input = np.array([[NP, NP, BR, LR],
                           [BR, LR, TL, NP],
                           [BR, LR, TL, NP]])

    output = make_maze(user_input)

    print(output)
