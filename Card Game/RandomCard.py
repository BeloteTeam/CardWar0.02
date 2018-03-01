import random

from Deck import Deck


class RandomCard:

    def random_pick():
        choice = input("Are you ready? Y/N:")
        if choice.lower() in ('y', 'yes'):
            card = random.randint(0, len(Deck)-1)
            print(Deck[card])
        else:
            print("Type Yes or Y when you are ready!")

    random_pick()
