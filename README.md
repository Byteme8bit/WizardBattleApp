## Welcome to my GitHub Page for WizardBattleApp

This is a short game written following a tutorial to learn and practice Object Oriented Programming in Python. It contains several classes, class methods and gave me an opportunity to learn more about inheritence and polymorphism in programming.

### Rundown of classes:

- **Creature** - everything is derived from this main class. It has 2 main parameters "name" and "level" and also defines the main class       method for attack as well as a "magic method" for less ambiguity in output.

- **Wizard(_Creature_)** - defins a class derived from Creature with modified stats. This is the class of the player and of the "boss"

- **SmallAnimal(_Creature_)** - defines a  class derived from Creature with a weakend attack method
- **Dragon(_Creature_)** - defines a class derived from Creature with extra parameters and stronger attack

1. Code that defines main game:

```
import random
import time

from actors import Wizard, Creature, SmallAnimal, Dragon

__author__ = "byteme8bit"


def main():
    print_header()
    game_loop()
    pass


def print_header():
    print('----------------------------------------')
    print('           WIZARD GAME APP              ')
    print('----------------------------------------')
    print()


def game_loop():
    creatures = [
        SmallAnimal('Toad', 1),
        Creature('Tiger', 12),
        SmallAnimal('Bat', 3),
        Dragon('Dragon', 50, 75, True),
        Wizard('Evil Wizard', 1000)
    ]

    hero = Wizard('Gandolf', 75)

    while True:

        active_creature = random.choice(creatures)
        print('A {} of level {} has appeared from a dark and foggy forest....'
              .format(active_creature.name, active_creature.level))

        cmd = input('Do you [a]ttack, [r]un away, or [l]ook around? ')
        if cmd == 'a':
            if hero.attack(active_creature):
                creatures.remove(active_creature)
            else:
                print("The wizard runs and hides taking time to recover.")
                time.sleep(5)
                print("The wizard returns revitalized!")
        elif cmd == 'r':
            print('The wizard has become unsure of his powers and flees!!!')
        elif cmd == 'l':
            print('The wizard {} takes in the surroundings and sees: ')
            for c in creatures:
                print(" * A {} of level {}".format(
                    c.name, c.level
                ))
        else:
            print('Ok, exiting game...')
            break

        if not creatures:
            print("You've defeated all the creatures, well done!")
            break
        print()


if __name__ == '__main__':
    main()
```

2. Code that defines classes:

```
__author__ = "byteme8bit"
import random


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


class Wizard(Creature):
    # def __init__(self, name, level):
    #     super().__init__(name, level)

    def attack(self, creature):
        print("The wizard {} attacks {}!".format(
            self.name, creature.name
        ))

        my_roll = self.get_defensive_roll()
        creature_roll = creature.get_defensive_roll()

        print("You rolled {}....".format(my_roll))
        print("{} rolled {}....".format(creature.name, creature_roll))

        if my_roll >= creature_roll:
            print("The wizard has handily triumphed over {}".format(creature.name))
            return True
        else:
            print("The wizard has been DEFEATED!!!!")
            return False


class SmallAnimal(Creature):
    def get_defensive_roll(self):
        base_roll = super().get_defensive_roll()
        return base_roll // 2


class Dragon(Creature):
    def __init__(self, name, level, scaliness, breaths_fire):
        super().__init__(name, level)
        self.breaths_fire = breaths_fire
        self.scaliness = scaliness

    def get_defensive_roll(self):
        base_roll = super().get_defensive_roll()
        # fire_modifier = None
        # if self.breaths_fire:
        #     fire_modifier = 5
        # else:
        #     fire_modifier = 1
        fire_modifier = 5 if self.breaths_fire else 1
        scale_modifier = self.scaliness / 10

        return base_roll * fire_modifier * scale_modifier

```
