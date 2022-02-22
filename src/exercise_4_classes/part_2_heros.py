"""write classes of the following heroes: warrior, mage, and archer. all classes have health points (
hp) and magic energy (mana). there are three different types of magic: fire, ice and arcane; fire magic has the spell
fireball, ice magic has the spell freeze and arcane magic has the spell black hole. the warrior is furious and can
use fire magic as well as his hammer; the archer is calm and can use ice magic in addition to his arrows; the mage
can use all types of magic. each magic spell costs an arbitrary amount of magic energy and can be cast only if there
is enough mana. use magic mixins to reduce repetitive code. """

from random import randint
from abc import abstractmethod, ABCMeta, ABC


class Magic(ABC):           # INTERFACE
    @abstractmethod
    def __init__(self):
        raise NotImplementedError

    @staticmethod
    @abstractmethod
    def _get_spells():
        raise NotImplementedError


class FireMagic(Magic, ABC):
    @abstractmethod
    def __init__(self):
        raise NotImplementedError

    @staticmethod
    def _get_spells():
        return [FireMagic.fireball]

    def fireball(self, target):
        if self.mana >= 20:
            if target.is_fire_resistant():
                target.hp -= 10
                self.mana -= 20
                print(f"You fired a fire-ball to {target.name}. He doesn't seem to feel it tho, he's Fire resistant!!!")
            else:
                target.hp -= 20
                self.mana -= 20
                print(f'You fired an fire-ball to {target.name}. He might burn his anger now...')
        else:
            print(f'Cant throw a fire-ball, your mana is not enough.')


class IceMagic(Magic, ABC):
    @abstractmethod
    def __init__(self):
        raise NotImplementedError

    @staticmethod
    def _get_spells():
        return [IceMagic.freeze]

    def freeze(self, target):
        if self.mana >= 20:
            if target.is_ice_resistant():
                target.hp -= 10
                self.mana -= 20
                print(f"You fired an ice-ball to {target.name}. He doesn't seem to feel it tho, he's Ice resistant!!!")
            else:
                target.hp -= 20
                self.mana -= 20
                print(f'You fired an ice-ball to {target.name}. He can feel the cold...')
        else:
            print(f'Cant throw an ice-ball, your mana is not enough.')


class ArcaneMagic(Magic, ABC):
    @abstractmethod
    def __init__(self):
        raise NotImplementedError

    @staticmethod
    def _get_spells():
        return [ArcaneMagic.blackhole]

    def blackhole(self, target):
        if self.mana >= 20:
            if target.is_arcane_resistant():
                target.hp -= 10
                self.mana -= 20
                print(f"You fired a blackhole to {target.name}. He doesn't seem to feel it tho, he's Arcane resistant!!!")
            else:
                target.hp -= 20
                self.mana -= 20
                print(f'You fired a blackhole to {target.name}. He might loose himself for a while now...')
        else:
            print(f'Cant throw a blackhole, your mana is not enough.')


class Hero(ABC):                    # ABSTRACT BASE CLASSES
    @abstractmethod
    def __init__(self, num_potions=3, hp=100, mana=100, name="", character=""):
        self.hp = hp
        self.mana = mana
        self.character = character
        self.name = name
        self.num_potions = num_potions

    @staticmethod
    @abstractmethod
    def _get_actions(x):
        raise NotImplementedError

    def get_actions(self):
        actions = []
        actions.extend(self._get_actions())
        if issubclass(self.__class__, Magic):
            for c in self.__class__.__bases__:
                if issubclass(c, Magic):
                    actions.extend(c._get_spells())
        return actions

    def __str__(self):
        return f'{self.name}. HP: {self.hp}. Mana: {self.mana}. Class: {self.__class__.__name__}.'

    def take_potion(self):
        if self.num_potions > 0:
            if self.mana >= 10:
                self.mana -= 10
                self.num_potions -= 1
                self.hp += randint(20, 60)
                print(f'You drank a potion! feeling much better now...')
            else:
                print(f'Cant make a potion, your mana is not enough. Be careful!')
        else:
            print(f'Oh no... You are out of potion. Be careful!')

    def _unveil_character(self):
        if self.character:
            print(f'{self.name}s character is: {self.character}.')
        else:
            print(f'{self.name}s character is undefined')

    def _show_health(self):
        if self.hp < 0:
            self.hp = 0
        elif self.mana < 0:
            self.mana = 0
        if isinstance(self, Monster):
            print(f"MONSTER{' '*49} HP: {self.hp} Mana: {self.mana}")
        elif isinstance(self, Hero):
            print(f"PLAYER {' '*49} HP: {self.hp} Mana: {self.mana}")


class Warrior(Hero, FireMagic):                            # INHERITANCE
    def __init__(self, name):
        super().__init__(character='furious', name=name, num_potions=2)

    @staticmethod
    def _get_actions():
        return [Warrior.take_potion, Warrior.hammer_attack, Warrior.fist_attack]

    @staticmethod
    def _get_potions(num_potions):

        return num_potions

    def hammer_attack(self, target):
        target.hp -= 10
        print(f'You attacked {target.name} with a hammer.')

    def fist_attack(self, target):
        target.hp -= 10
        print(f'You attacked {target.name} with your fist.')


class Mage(Hero, FireMagic, IceMagic, ArcaneMagic):        # MULTIPLE INHERITANCE
    def __init__(self, name, mana=150, hp=80):
        super().__init__(name=name, mana=mana, hp=hp, num_potions=1)

    def _get_actions(self):
        return [Mage.take_potion]


class Archer(Hero, IceMagic):
    def __init__(self, name):
        super().__init__(name=name, character='calm', num_potions=3)

    @staticmethod
    def _get_actions():
        return [Archer.take_potion, Archer.arrow_attack, Archer.knife_attack]

    def arrow_attack(self, target):
        target.hp -= 10
        print(f'You attacked {target.name} with an arrow.')

    def knife_attack(self, target):
        target.hp -= 10
        print(f'You attacked {target.name} with a knife.')


class Monster(Hero, ABC):
    def __init__(self, name):
        self.name = name
        super().__init__(name=name, character='unstable')

    def is_fire_resistant(self):
        return False

    def is_ice_resistant(self):
        return False

    def is_arcane_resistant(self):
        return False

    @staticmethod
    def _get_actions():
        return [Monster.beast_attack, Monster.crash_running_attack, Monster.invisible_attack]

    def beast_attack(self, target):
        if self.mana >= 30:
            target.hp -= randint(10, 40)
            self.mana -= 40
            return f'{self.name} made his beast attack.'
        else:
            return f'{self.name} is really dizzy now...'

    def crash_running_attack(self, target):
        if self.mana >= 0:
            target.hp -= randint(5, 30)
            self.mana -= 10
            return f'{self.name} made his crash running attack.'
        else:
            return f"{self.name} is on his knees...this shouldn't last for long"

    def invisible_attack(self, target):
        if self.mana >= 10:
            target.hp -= randint(10, 25)
            self.mana -= 10
            return f'{self.name} made an invisible attack. You can feel it tho.'
        else:
            return f"{self.name} is trying to run...he seems pretty scared."


class FireResistantMonster(Monster):
    def is_fire_resistant(self):
        return True


class IceResistantMonster(Monster):
    def is_ice_resistant(self):
        return True


class ArcaneResistantMonster(Monster):
    def is_arcane_resistant(self):
        return True


class FullyResistantMonster(Monster):
    def is_fire_resistant(self):
        return True

    def is_ice_resistant(self):
        return True

    def is_arcane_resistant(self):
        return True

