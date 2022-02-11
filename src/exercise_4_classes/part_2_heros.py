"""write classes of the following heroes: warrior, mage, and archer. all classes have health points (
hp) and magic energy (mana). there are three different types of magic: fire, ice and arcane; fire magic has the spell
fireball, ice magic has the spell freeze and arcane magic has the spell black hole. the warrior is furious and can
use fire magic as well as his hammer; the archer is calm and can use ice magic in addition to his arrows; the mage
can use all types of magic. each magic spell costs an arbitrary amount of magic energy and can be cast only if there
is enough mana. use magic mixins to reduce repetitive code. """
from abc import abstractmethod, ABCMeta


class FireMagic(object, metaclass=ABCMeta):
    @abstractmethod
    def __init__(self):
        pass

    def fire_fireball(self, target):
        if self.mana >= 20:
            target.hp -= 20
            self.mana -= 20
            print(f'You fired a fire-ball to {target.name}. He seems hurt...')
        else:
            print(f'Cant throw a fire-ball, your mana is not enough.')

    def fire_freeze(self, target):
        if self.mana >= 20:
            target.hp -= 20
            self.mana -= 20
            print(f'You fired an ice-ball to {target.name}. He can feel the cold...')
        else:
            print(f'Cant throw an ice-ball, your mana is not enough.')

    def fire_blackhole(self, target):
        if self.mana >= 20:
            target.hp -= 20
            self.mana -= 20
            print(f'You fired a blackhole to {target.name}. Now he might loose himself for a while...')
        else:
            print(f'Cant throw a blackhole, your mana is not enough.')

    def get_affix(self):
        if self.mana >= 10:
            self.mana -= 10
            self.hp += 20
            print(f'You got the affix! The pain seems to be seizing now...')
        else:
            print(f'Cant get affix, your mana is not enough. Be careful!')


class Hero(object, metaclass=ABCMeta):
    @abstractmethod
    def __init__(self, hp=100, mana=100, character=""):
        self.hp = hp
        self.mana = mana
        self.character = character

    def __str__(self):
        return f'{self.name}. HP: {self.hp}. Mana: {self.mana}. Class: {self.__class__.__name__}.'

    def _unveil_character(self):
        if self.character:
            print(f'{self.name}s character is: {self.character}.')
        else:
            print(f'{self.name}s character is undefined')

    def _get_actions(self):
        actions = [attribute for attribute in dir(self) if callable(getattr(self, attribute)) and attribute.startswith('_') is False]
        return actions

    def _show_health(self):
        print(f'{self.name} HP: {self.hp}. Mana: {self.mana}.')


class Warrior(Hero, FireMagic):
    def __init__(self, name):
        self.name = name
        super().__init__()
        self.character = 'furious'

    @staticmethod
    def hammer_attack(self, target):
        target.hp -= 10
        print(f'You attacked {target.name} with a hammer.')


class Mage(Hero, FireMagic):
    def __init__(self, name):
        self.name = name
        super().__init__()


class Archer(Hero, FireMagic):
    def __init__(self, name):
        self.name = name
        super().__init__()
        self.character = 'calm'

    @staticmethod
    def arrow_attack(self, target):
        target.hp -= 10
        print(f'You attacked {target.name} with an arrow.')


class Monster(Hero):
    def __init__(self, name):
        self.name = name
        super().__init__()
        self.character = 'unstable'

    def beast_attack(self, target):
        if self.mana >= 40:
            target.hp -= 60
            self.mana -= 40
            return f'{self.name} made his beast attack.'
        else:
            return f'{self.name} is really dizzy now...'

    def crash_running_attack(self, target):
        if self.mana >= 0:
            target.hp -= 40
            self.mana -= 10
            return f'{self.name} made his crash running attack.'
        else:
            return f"{self.name} is on hes knees...this shouldn't last for long"

    def invisible_attack(self, target):
        if self.mana >= 10:
            target.hp -= 20
            self.mana -= 10
            return f'{self.name} made an invisible attack. You can feel it tho.'
        else:
            return f"{self.name} is trying to run...he seems pretty scared."

#todo: restrict ths use of methods for each hero.








