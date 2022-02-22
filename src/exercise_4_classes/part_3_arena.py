"""Exercise 5a-1. Create an arena for the mighty heroes from Exercise 5-2. The game starts with hero class selection.
Then the game will generate a random monster. The monster has health points and can attack the hero, subtracting some
amount of HP. The monster can have (or not) an affix that reduces damage taken from fire, ice or arcane magic. The
main point of the game is to stay alive (hero HP > 0) and defeat the enemy. """

from part_2_heros import Hero, Warrior, Archer, Mage, FireResistantMonster, ArcaneResistantMonster, \
    IceResistantMonster, FullyResistantMonster
from random import choice
from datetime import datetime


class Arena:
    def __init__(self, player_name="", date=datetime.today()):
        self.game_date = date
        self.player_name = player_name

    def set_user_name(self):
        self.player_name = input("Please enter your name and press Enter to register your score: ")

    def get_user_name(self):
        return self.player_name

    @staticmethod
    def store_score():
        with open("scores.txt", "a") as f:
            f.write(f"\nDate: {new_game.game_date}.\n"
                    f"Player Name: {new_game.player_name}\n"
                    f"Fighter: {player.name}. Final HP: {player.hp}\n"
                    f"Monster Name: {monster.name}. Final HP: {monster.hp}\n\n")
            f.close()

    @staticmethod
    def show_scores():
        Arena.clear()
        with open("scores.txt") as f:
            print(f.read())
            f.close()

    @staticmethod
    def play_again_or_exit():
        user_choice = input(f"Type 'exit' if you want to quit or Press Enter if you want to play again: ")
        if user_choice == 'exit':
            Arena.clear()
            print(f"Hope you've had fun {Arena.get_user_name(new_game)}. See you later!")
            result = False
            return result
        else:
            result = True
            return result

    @staticmethod
    def clear():
        print("\n" * 12)

    @staticmethod
    def game_intro():
        Arena.clear()
        print("###########################################################################")
        print("######################### WELCOME TO THE ARENA ############################")
        print("###########################################################################\n")
        print("INSTRUCTIONS: Choose a fighter. Try to defeat a randomly selected monster.\n"
              "Each class of fighter has it's own type of magic and a single potion.\n")

    @staticmethod
    def show_fighters():
        for key, val in heroes_dict.items():
            print(key, val)

    @staticmethod
    def select_player():
        try:
            print()
            selector = int(input("Please, select a fighter, type it's number and press Enter to confirm: "))
            result = heroes_dict[selector]
            print()
        except ValueError:
            print()
            print("Wrong selection, try again...")
            return Arena.select_player()
        except KeyError:
            print()
            print("Wrong selection, try again...")
            return Arena.select_player()
        return result

    @staticmethod
    def actions_dict_maker():
        Arena.clear()
        print(f"Excellent selection, a {player.__class__.__name__}!! Let's see what can he do...")
        if isinstance(player, Hero):
            actions = player.get_actions()
        result = dict(zip(range(len(actions)), actions))
        return result

    @staticmethod
    def show_actions():
        print("------------------------------------------------------------------------")
        print(f"{player.name} Actions:")
        print()
        for k, v in player_actions_dict.items():
            print(k, ": ", v.__name__)
        print("------------------------------------------------------------------------")

    @staticmethod
    def monster_selector():
        monster_list = list(monsters_dict.values())
        result = choice(monster_list)
        input(f"You will fight {result.name}!! Press Enter to Start the fight: ")
        Arena.clear()
        return result

    @staticmethod
    def game_start():
        print("*************************************************************************")
        print("***************************THE FIGHT HAD BEGUN***************************")
        print("*************************************************************************")
        print()
        print(f"You see the monster, it’s horrifying and dangerous!!! \nBut {player.name} has no fear...")
        print()

    @staticmethod
    def player_move():
        try:
            Arena.show_actions()
            move = player_actions_dict[int(input("SELECT AN ACTION BY IT'S NUMBER AND PRESS ENTER TO CONTINUE: "))]
            Arena.clear()
        except KeyError:
            Arena.clear()
            print(f"Ouch! {player.name} doesn't have an action for that number. Check out:")
            return Arena.player_move()
        except ValueError:
            Arena.clear()
            print(f"Ouch! {player.name} doesn't have an action for that number. Check out:")
            return Arena.player_move()
        try:
            return move(player, monster)
        except TypeError:
            return move(player)

    @staticmethod
    def monster_move():
        actions = monster._get_actions()
        move = choice(actions)
        print(move(monster, player))

    @staticmethod
    def fight():
        Arena.player_move()
        Arena.monster_move()
        print()
        print("#########################################################################")
        monster._show_health()
        player._show_health()
        print("#########################################################################")
        print()
        if monster.hp <= 0:
            print(f"{' '*10}† † † ...{monster.name} is dead... † † †")
            print()
            print('*************************************************************************')
            print(f'************VERY GOOD, YOU WON!! {monster.name} was defeated.***********')
            print('*************************************************************************')
        elif player.hp <= 0:
            print(f"{' '*10}† † † ...{player.name} is dead... † † †")
            print()
            print('*************************************************************************')
            print(f'******************* GAME OVER!! {monster.name} defeated you.**************')
            print('*************************************************************************')
        else:
            return Arena.fight()


# USAGE
if __name__ == '__main__':
    heroes_dict = {1: Warrior('Jorge "El Roña" Castro'),
                   2: Warrior('Richie "Treta" Silver'),
                   3: Mage('Carlos "La Mona" Jimenez'),
                   4: Mage('Daniel "Tota" Santillán'),
                   5: Archer('Guillermo "Willy" Crook'),
                   6: Archer('Enzo "El "Principe" Franccescoli')}

    monsters_dict = {1: FireResistantMonster('Baby Etchecopar'),
                     2: FullyResistantMonster('Ramon "Wanchope" Abila'),
                     3: ArcaneResistantMonster('Hector "Bambino" Veira'),
                     4: IceResistantMonster('Daniel "Tota" Santillán'),
                     5: FireResistantMonster('Ricardo Fort'),
                     6: ArcaneResistantMonster('Emilio Dissi')}

    flag = True
    while flag:
        new_game = Arena()
        new_game.game_intro()
        new_game.show_fighters()
        player = new_game.select_player()
        player_actions_dict = new_game.actions_dict_maker()
        new_game.show_actions()
        monster = new_game.monster_selector()
        new_game.game_start()
        new_game.fight()
        new_game.set_user_name()
        new_game.store_score()
        new_game.show_scores()
        flag = new_game.play_again_or_exit()
