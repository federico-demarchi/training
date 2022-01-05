# Part 2) Make another implementation of make_maze that starts from maze (a matrix of tiles)
# using a representation of a tile as a matrix


def make_maze(maze):
    result = ''
    for row in maze:
        line1 = ''
        line2 = ''
        line3 = ''
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

    user_input = [[NP, NP, BR, LR],
                  [BR, LR, TL, NP],
                  [BR, LR, TL, NP]]

    output = make_maze(user_input)

    print(output)
