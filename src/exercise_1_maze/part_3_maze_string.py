# Part 3) Make another implementation of make_maze that starts from maze (a matrix of tiles)
#    using a representation of a tile as a String indicating which tile to draw
#    maze = [["NP", "BR"], ["LR", etc...
#


def make_maze(maze):
    dict_tiles = {
        "NP": ["###", "###", "###"],
        "BT": ["# #", "# #", "# #"],
        "LR": ["###", "   ", "###"],
        "BR": ["###", "#  ", "# #"],
        "BL": ["###", "  #", "# #"],
        "TR": ["# #", "#  ", "###"],
        "TL": ["# #", "  #", "###"]
    }
    result = ''
    for row in maze:
        line1 = ''
        line2 = ''
        line3 = ''
        for tile in row:
            line1 = line1 + dict_tiles[tile][0]
            line2 = line2 + dict_tiles[tile][1]
            line3 = line3 + dict_tiles[tile][2]
        result = result + line1 + "\n" + line2 + "\n" + line3 + "\n"
    return result


# USAGE
if __name__ == '__main__':
    user_input = [['NP', 'NP', 'BR', 'LR'],
                  ['BR', 'LR', 'TL', 'NP'],
                  ['BR', 'LR', 'TL', 'NP']]

    output = make_maze(user_input)

    print(output)
