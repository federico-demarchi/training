
# Part 1) Write a function that takes a two-dimensional array as an argument and outputs
# a maze drawn with tiles corresponding to this array

def make_maze(maze):
    result = ''
    for row in maze:
        line1 = ''
        line2 = ''
        line3 = ''
        for tile in row:
            line1 = line1 + tile[0:3]
            line2 = line2 + tile[3:6]
            line3 = line3 + tile[6:9]
        result = result + line1 + "\n" + line2 + "\n" + line3 + "\n"
    return result


# USAGE
if __name__ == '__main__':
    NP = "#########"
    BT = "# ## ## #"
    LR = "###   ###"
    BR = "####  # #"
    BL = "###  ## #"
    TR = "# ##  ###"
    TL = "# #  ####"

    user_input = [[NP, NP, BR, LR],
                  [BR, LR, TL, NP],
                  [BR, LR, TL, NP]]

    output = make_maze(user_input)

    print(output)
