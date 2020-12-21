# from ludogi import *

players = {'ali': 'alish'}
# players_data = player


def add(*args):
    if args[0] in players.keys():
        if players.get(args[0]) == args[1]:
            return False
        else:
            return True
    else:
        players[args[0]] = args[1]
        return False


# def data(*args):
#     players_data[args[0]] = args[1]
