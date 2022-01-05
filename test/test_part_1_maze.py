from unittest import TestCase
from exercise_1_maze.part_1_maze import make_maze

NP = "#########"
BT = "# ## ## #"
LR = "###   ###"
BR = "####  # #"
BL = "###  ## #"
TR = "# ##  ###"
TL = "# #  ####"


class Test(TestCase):
    def test_make_maze(self):
        user_input = [[NP, NP, BR, LR],
                      [BR, LR, TL, NP],
                      [BR, LR, TL, NP]]
        output = make_maze(user_input)
        expected_output = ("############\n"
                           "#######     \n"
                           "####### ####\n"
                           "####### ####\n"
                           "#       ####\n"
                           "# ##########\n"
                           "####### ####\n"
                           "#       ####\n"
                           "# ##########\n")
        self.assertEqual(output, expected_output)

    def test_make_maze_NP(self):
        user_input = [[NP, NP, NP, NP],
                      [NP, NP, NP, NP],
                      [NP, NP, NP, NP]]
        output = make_maze(user_input)
        expected_output = ("############\n"
                           "############\n"
                           "############\n"
                           "############\n"
                           "############\n"
                           "############\n"
                           "############\n"
                           "############\n"
                           "############\n")
        self.assertEqual(output, expected_output)

    def test_make_maze_1x1(self):
        user_input = [[NP]]
        output = make_maze(user_input)
        expected_output = ("###\n"
                           "###\n"
                           "###\n")
        self.assertEqual(output, expected_output)
