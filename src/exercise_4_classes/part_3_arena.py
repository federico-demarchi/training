"""Exercise 5a-1. Create an arena for the mighty heroes from Exercise 5-2. The game starts with hero class selection.
Then the game will generate a random monster. The monster has health points and can attack the hero, subtracting some
amount of HP. The monster can have (or not) an affix that reduces damage taken from fire, ice or arcane magic. The
main point of the game is to stay alive (hero HP > 0) and defeat the enemy. """

from part_2_heros import Warrior, Archer, Mage, Monster
import random


def clear():
    print("\n" * 12)


heroes_dict = {1: Warrior('Jorge "El Roña" Castro'),
               2: Warrior('Richie "Treta" Silver'),
               3: Mage('Carlos "La Mona" Jimenez'),
               4: Mage('Daniel "Tota" Santillán'),
               5: Archer('Guillermo "Willy" Crook'),
               6: Archer('Enzo "El "Principe" Franccescoli')}

monsters_dict = {1: Monster('Baby Etchecopar'),
                 2: Monster('Ramon "Wanchope" Abila'),
                 3: Monster('Hetor "Bambino" Veira'),
                 4: Monster('Daniel "Tota" Santillán'),
                 5: Monster('Ricardo Fort'),
                 6: Monster('Emilio Dissi')}


def game_intro():
    print("############## WELCOME TO THE ARENA ################\n")
    print("INSTRUCTIONS \nYou would have to fight a monster and try to stay alive. \n"
          "Each class of fighter has his own weapons and all of them \n"
          "count with just one affix.\n")
    input("Press Enter to continue:")
    clear()
    input("THESE WOULD BE THE FIGHTERS...\n\nPress Enter again to meet them: ")
    clear()


game_intro()


def show_fighters():
    for key, val in heroes_dict.items():
        print(key, val)


show_fighters()


def select_player():
    try:
        print()
        selector = int(input("Please, select a fighter, type it's number and press Enter to confirm: "))
        result = heroes_dict[selector]
        print()
    except KeyError:
        print()
        print("Wrong selection, try again...")
        return select_player()
    return result


player = select_player()


def actions_dict_maker():
    print("You chose:", player.name, "\n")
    input(f"Press Enter again, to see {player.name} actions: ")
    result = dict(zip(range(len(player._get_actions())), player._get_actions()))
    return result


player_actions_dict = actions_dict_maker()


def show_actions():
    print()
    for k, v in player_actions_dict.items():
        print(k, ": ", v)
    print()


show_actions()


def monster_selector():
    input(f"Now, a monster should be selected randomly. Please, Press Enter to do so: ")
    clear()
    monster_list = list(monsters_dict.values())
    result = random.choice(monster_list)
    return result


monster = monster_selector()


def game_start():
    input(f"The selected monster was: {monster.name}. Press Enter to Start the fight: ")
    clear()
    print("*****************************************************************")
    print("**********************THE FIGHT HAD BEGUN************************")
    print("*****************************************************************")
    print("\n"*10)
    print(f"You see the monster, it’s horrifying and dangerous!!! But {player.name} has no fear...")
    print()


game_start()


def player_move():
    try:
        move = player_actions_dict[int(input("SELECT AN ACTION BY IT'S NUMBER AND PRESS ENTER TO CONTINUE: "))]
        clear()
    except KeyError:
        print(f"Ouch! {player.name} doesn't have an action for that number. Check out:")
        show_actions()
        return player_move()
    if move == 'fire_blackhole':
        return player.fire_blackhole(monster)
    elif move == 'fire_fireball':
        return player.fire_fireball(monster)
    elif move == 'fire_freeze':
        return player.fire_freeze(monster)
    elif move == 'hammer_attack':
        return player.hammer_attack(player, monster)
    elif move == 'arrow_attack':
        return player.arrow_attack(player, monster)
    elif move == 'get_affix':
        return player.get_affix()


def monster_move():
    monster_actions = [action for action in dir(monster) if callable(getattr(monster, action)) and action.startswith('_') is False]

    move = random.choice(monster_actions)

    if move == monster_actions[0]:
        print(monster.beast_attack(player))
    elif move == monster_actions[1]:
        print(monster.crash_running_attack(player))
    elif move == monster_actions[2]:
        print(monster.invisible_attack(player))


def game():
    player_move()
    monster_move()
    print()
    monster._show_health()
    player._show_health()
    print()
    if monster.hp <= 0:
        print(f"{monster.name} is dead....")
        print()
        print('*********************************************************')
        print(f'VERY GOOD, YOU WON!! {monster.name} was defeated.')
        print('*********************************************************')
    elif player.hp <= 0:
        print(f"{player.name} is dead....")
        print()
        print('***************************************')
        print(f'TOO BAD!! {monster.name} defeated you.')
        print('***************************************')
    else:
        return game()


game()
