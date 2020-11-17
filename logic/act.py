from random import randrange
from logic.move import *


def dice():
    return randrange(1, 7)


def player_home(players):
    if players == 2:
        return [0, 12]
    elif players == 3:
        return [0, 6, 12]
    else:
        return [0, 6, 12, 18]


def check_final(user, pos):
    for i in range(1, 5):
        if pos[f'{user}{i}'] != 100:
            return False
    return True


def check_end(pos):
    for i in pos.values():
        if i != 100:
            return False
    return True


def check_marks(user, chance, pos, home):
    for choice in range(1, 5):
        if check_mark(user, choice, chance, pos, home):
            return True
    return False


def check_mark(user, choice, chance, pos, home):
    now = pos[f'{user}{choice}']
    if home in [(now + i) % 24 for i in range(1, chance + 1)] and now != -1:
        if go_win(user, pos):
            return "WIN"
        else:
            return True
    else:
        cell = (now + chance) % 24
        if now == -1:
            if chance == 6:
                if check(user, home, pos):
                    return True
                else:
                    return False
            else:
                return False
        elif now == 100:
            return False
        elif check(user, cell, pos):
            return True
        else:
            return False

# def check_marks(user, chance, pos_test, home):
#     for i in range(1, 5):
#         if moving(user, i, chance, pos_test, home):
#             return True
#     return False
