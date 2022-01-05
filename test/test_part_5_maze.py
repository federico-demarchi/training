from unittest import TestCase
from exercise_1_maze.part_5_maze_checker import check_maze, find_openings, make_dict, find_neighbors, is_connected


class Test(TestCase):
    def test_make_dict(self):
        maze = [['NP', 'NP', 'BR', 'LR'],
                ['BR', 'LR', 'TL', 'NP'],
                ['BR', 'LR', 'TL', 'NP']]
        result = make_dict(maze)
        expected = {(0, 0): 'NP', (0, 1): 'NP', (0, 2): 'BR', (0, 3): 'LR',
                    (1, 0): 'BR', (1, 1): 'LR', (1, 2): 'TL', (1, 3): 'NP',
                    (2, 0): 'BR', (2, 1): 'LR', (2, 2): 'TL', (2, 3): 'NP'}
        self.assertEqual(expected, result)

    def test_find_openings_2x2(self):
        maze = [["NP", "BL"],
                ["NP", "TL"]]
        result = find_openings(maze)
        expected = None
        self.assertEqual(expected, result)

    def test_find_openings_3x3(self):
        maze = [["BR", "BL", "NP"],
                ["TR", "TL", "NP"],
                ["TR", "LR", "TL"]]
        result = find_openings(maze)
        expected = None
        self.assertEqual(expected, result)

    def test_find_openings_4x3(self):
        maze = [['BT', 'TR', 'TR', 'LR'],
                ['BL', 'LR', 'TL', 'BR'],
                ['BR', 'BT', 'BL', 'BL']]
        result = find_openings(maze)
        expected = [(0, 0), (0, 1), (0, 2), (0, 3), (1, 0), (1, 3), (2, 0), (2, 1), (2, 2), (2, 3)]
        self.assertEqual(expected, result)

    def test_find_neighbors(self):
        current = (0, 1)
        maze_dict = {(0, 0): 'NP', (0, 1): 'NP'}
        result = find_neighbors(current, maze_dict)
        expected = (None, None)
        self.assertEqual(expected, result)

        current = (0, 1)
        maze_dict = {(0, 0): 'LR', (0, 1): 'LR'}
        result = find_neighbors(current, maze_dict)
        expected = (0, 2), (0, 0)
        self.assertEqual(expected, result)

        current = (0, 1)
        maze_dict = {(0, 0): 'LR', (0, 1): 'BT'}
        result = find_neighbors(current, maze_dict)
        expected = ((1, 1), (-1, 1))
        self.assertEqual(expected, result)

        current = (0, 1)
        maze_dict = {(0, 0): 'LR', (0, 1): 'BL'}
        result = find_neighbors(current, maze_dict)
        expected = ((1, 1), (0, 0))
        self.assertEqual(expected, result)

        current = (0, 1)
        maze_dict = {(0, 0): 'LR', (0, 1): 'BR'}
        result = find_neighbors(current, maze_dict)
        expected = ((1, 1), (0, 2))
        self.assertEqual(expected, result)

        current = (0, 1)
        maze_dict = {(0, 0): 'LR', (0, 1): 'TR'}
        result = find_neighbors(current, maze_dict)
        expected = ((-1, 1), (0, 2))
        self.assertEqual(expected, result)

        current = (0, 1)
        maze_dict = {(0, 0): 'LR', (0, 1): 'TL'}
        result = find_neighbors(current, maze_dict)
        expected = ((-1, 1), (0, 0))
        self.assertEqual(expected, result)

        current = (0, -1)
        maze_dict = {(0, 0): 'NP', (0, 1): 'NP'}
        result = find_neighbors(current, maze_dict)
        expected = (None, None)
        self.assertEqual(expected, result)

    def test_is_connected(self):
        maze_dict = {(0, 0): 'NP', (0, 1): 'BL'}
        current = (0, 0)
        neighbor = (0, 1)
        result = is_connected(current, neighbor, maze_dict)
        self.assertFalse(result)

        maze_dict = {(0, 0): 'TR', (0, 1): 'BL'}
        current = (0, 0)
        neighbor = (0, 1)
        result = is_connected(current, neighbor, maze_dict)
        self.assertTrue(result)

        maze_dict = {(0, 0): 'TR', (0, 1): 'BL', (0, 2): 'BL'}
        current = (0, 0)
        neighbor = (0, 2)
        result = is_connected(current, neighbor, maze_dict)
        self.assertFalse(result)

        maze_dict = {(0, 0): 'TR', (0, 1): 'BL', (0, 2): 'BL'}
        current = (0, 0)
        neighbor = (0, 500)
        result = is_connected(current, neighbor, maze_dict)
        self.assertFalse(result)

        maze_dict = {(0, 0): 'LR', (0, 1): 'BL', (0, 2): 'BL'}
        current = (0, 0)
        neighbor = (0, -1)
        result = is_connected(current, neighbor, maze_dict)
        self.assertTrue(result)

        maze_dict = {(0, 0): 'LR', (0, 1): 'BL', (0, 2): 'BL'}
        current = (0, -1)
        neighbor = (0, 0)
        result = is_connected(current, neighbor, maze_dict)
        self.assertTrue(result)

    def test_check_maze_1x1(self):
        maze = [["NP"]]
        result = check_maze(maze)
        expected = False, None
        self.assertEqual(expected, result)

        maze = [["LR"]]
        result = check_maze(maze)
        expected = True, [(0, 0)]
        self.assertEqual(expected, result)

    def test_check_maze_2x2(self):
        maze = [["NP", "BL"],
                ["NP", "TL"]]
        result = check_maze(maze)
        expected = False, None
        self.assertEqual(expected, result)

        maze = [["NP", "TL"],
                ["BL", "TL"]]
        result = check_maze(maze)
        expected = True, [(1, 0)]
        self.assertEqual(expected, result)

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
