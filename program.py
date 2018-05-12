import random
import time

from actors import Wizard, Creature

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
        Creature('Toad', 1),
        Creature('Tiger', 12),
        Creature('Bat', 3),
        Creature('Dragon', 50),
        Creature('Evil Wizard', 1000),
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


if __name__ == '__main__':
    main()
