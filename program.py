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

        cmd = input('Do you [a]ttack, [r]un away, or [l]ook around? ')
        if cmd == 'a':
            print('attack')
        elif cmd == 'r':
            print('runaway')
        elif cmd == 'l':
            print('look around')
        else:
            print('Ok, exiting game...')
            break


if __name__ == '__main__':
    main()
