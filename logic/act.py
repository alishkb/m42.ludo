from random import randrange


def dice():
    return randrange(1, 7)


def player_home(players):
    if players == 2:
        return [0, 12]
    elif players == 3:
        return [0, 6, 12]
    else:
        return [0, 6, 12, 18]


