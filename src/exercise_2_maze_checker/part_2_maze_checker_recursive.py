# Write a function that checks if a maze is valid
# A valid maze has two openings and a path connecting them
# Input:
#   maze: a maze definition as a matrix of strings (like in 1.3)
# Output:
#   boolean: depending on whether the maze is valid.
#   list or None: if maze is valid, the valid path, else none
#
# Try to subdivide the problem into smaller problems

def make_dict(maze):
    return {(row_idx, col_idx): tile for (row_idx, row) in enumerate(maze) for (col_idx, tile) in enumerate(row)}


def find_openings(maze_dict, height, width):
    openings = []
    for row_idx in range(height):
        for col_idx in range(width):
            if row_idx == 0 or row_idx == height - 1 or col_idx == 0 or col_idx == width - 1:
                current = (row_idx, col_idx)
                if maze_dict[current] == "NP":
                    continue
                neighbor1, neighbor2 = find_neighbors(current, maze_dict)
                if maze_dict.get(neighbor1) is None or maze_dict.get(neighbor2) is None:
                    openings.append(current)
    if not openings:
        return None
    else:
        return openings


def find_neighbors(current, maze_dict):
    tile = maze_dict.get(current)
    neighbor1, neighbor2 = None, None
    if tile == 'NP':
        neighbor1, neighbor2 = None, None
    elif tile == 'LR':
        neighbor1, neighbor2 = (current[0], current[1] + 1), (current[0], current[1] - 1)
    elif tile == 'BT':
        neighbor1, neighbor2 = (current[0] + 1, current[1]), (current[0] - 1, current[1])
    elif tile == 'TL':
        neighbor1, neighbor2 = (current[0] - 1, current[1]), (current[0], current[1] - 1)
    elif tile == 'TR':
        neighbor1, neighbor2 = (current[0] - 1, current[1]), (current[0], current[1] + 1)
    elif tile == 'BR':
        neighbor1, neighbor2 = (current[0] + 1, current[1]), (current[0], current[1] + 1)
    elif tile == 'BL':
        neighbor1, neighbor2 = (current[0] + 1, current[1]), (current[0], current[1] - 1)
    return neighbor1, neighbor2


def is_connected(current, neighbor, maze_dict):
    if maze_dict.get(neighbor) is None:
        current1, current2 = find_neighbors(current, maze_dict)
        if current1 == neighbor or current2 == neighbor:
            return True
        else:
            return False
    elif maze_dict.get(current) is None:
        neighbor1, neighbor2 = find_neighbors(neighbor, maze_dict)
        if neighbor1 == current or neighbor2 == current:
            return True
        else:
            return False
    else:
        neighbor1, neighbor2 = find_neighbors(neighbor, maze_dict)
        current1, current2 = find_neighbors(current, maze_dict)
        if (neighbor1 == current or neighbor2 == current) and (current1 == neighbor or current2 == neighbor):
            return True
        else:
            return False


# Use Recursion here
def check_maze(maze):
    maze_dict = make_dict(maze)
    openings = find_openings(maze_dict, len(maze), len(maze[0]))
    if openings is None:
        return False, None
    for opening in openings:
        path_list = [opening]
        current = opening
        neighbor1, neighbor2 = find_neighbors(current, maze_dict)
        if maze_dict.get(neighbor1) is None and maze_dict.get(neighbor2) is None:
            return True, path_list
        elif maze_dict.get(neighbor1) is None:
            next_coord = neighbor2
        else:
            next_coord = neighbor1
        has_valid_path, path = next_tile(current, next_coord, path_list, maze_dict)
        if has_valid_path:
            return True, path
    return False, None


def next_tile(current, next_coord, path_list, maze_dict):
    if is_connected(current, next_coord, maze_dict):
        path_list.append(next_coord)
        current = next_coord
        neighbor1, neighbor2 = find_neighbors(current, maze_dict)
        if neighbor1 in path_list:
            next_coord = neighbor2
        else:
            next_coord = neighbor1
        if maze_dict.get(next_coord) is None:
            return True, path_list
        else:
            return next_tile(current, next_coord, path_list, maze_dict)
    else:
        return False, path_list


# USAGE
if "__name__" == '__main__':
    user_input = [['NP', 'NP', 'BR', 'LR'],
                  ['BR', 'LR', 'TL', 'NP'],
                  ['BR', 'LR', 'TL', 'NP']]

    output = check_maze(user_input)

    print(output)
