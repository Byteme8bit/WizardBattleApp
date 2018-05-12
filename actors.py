import random

__author__ = "byteme8bit"


class Wizard:
    def __init__(self, name, level):
        self.name = name
        self.level = level

    def attack(self, creature):
        print("The wizard {} attacks {}!".format(
            self.name, creature.name
        ))

        my_roll = random.randint(1, 12) * self.level
        # creature_roll = random.randint(1, 12) * creature.level
        creature_roll = creature.get_defensive_roll()

        print("You rolled {}....".format(my_roll))
        print("{} rolled {}....".format(creature.name, creature_roll))

        if my_roll >= creature_roll:
            print("The wizard has handily triumphed over {}".format(creature.name))
            return True
        else:
            print("The wizard has been DEFEATED!!!!")
            return False



class Creature:
    def __init__(self, name, the_level):
        self.name = name
        self.level = the_level

    def __repr__(self):
        return "Creature {} of level {}".format(
            self.name, self.level
        )

    def get_defensive_roll(self):
        return random.randint(1, 12) * self.level