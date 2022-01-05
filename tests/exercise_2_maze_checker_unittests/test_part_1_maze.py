from unittest import TestCase
from exercise_2_maze_checker.part_1_maze_checker import check_maze, find_openings, make_dict, find_neighbors, \
    is_connected


        maze = [["LR", "BL"],
                ["LR", "TL"]]
        result = check_maze(maze)
        expected = True, [(0, 0), (0, 1), (1, 1), (1, 0)]
        self.assertEqual(expected, result)

    def test_check_maze_3x3(self):
        maze = [["BT", "BR", "LR"],
                ["TR", "TL", "NP"],
                ["TR", "TR", "NP"]]
        result = check_maze(maze)
        expected = True, [(0, 0), (1, 0), (1, 1), (0, 1), (0, 2)]
        self.assertEqual(expected, result)

    def test_check_maze_4x4(self):
        maze = [["BL", "BL", "BR", "BR"],
                ["TR", "LR", "BL", "BL"],
                ["BT", "TL", "BT", "BR"],
                ["NP", "BT", "TR", "BL"]]
        result = check_maze(maze)
        expected = True, [(0, 0), (1, 0), (1, 1), (1, 2), (2, 2), (3, 2), (3, 3)]
        self.assertEqual(expected, result)

        maze = [["NP", "BR", "BR", "BR"],
                ["BR", "BR", "BR", "BR"],
                ["NP", "BR", "BR", "BR"],
                ["LR", "BT", "BR", "NP"]]
        result = check_maze(maze)
        expected = False, None
        self.assertEqual(expected, result)
