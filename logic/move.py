def start(user_data):
    positions = {}
    l_of_mark = [1, 2, 3, 4]
    for i in user_data:
        pos = {f"{i}{j}": -1 for j in l_of_mark}
        positions.update(pos)
    return positions


def moving(user, choice, chance, pos, home):
    now = pos[f'{user}{choice}']
    if home in [(now + i) % 24 for i in range(1, chance + 1)] and now != -1:
        pos[f'{user}{choice}'] = 100
        if go_win(user, pos):
            return "WIN"
        else:
            return True
    else:
        cell = (now + chance) % 24
        if now == -1:
            if chance == 6:
                if check(user, home, pos):
                    pos[f'{user}{choice}'] = home
                    return True
                else:
                    return False
            else:
                return False
        elif now == 100:
            return False
        elif check(user, cell, pos):
            pos[f'{user}{choice}'] = cell
            return True
        else:
            return False


def go_win(user, pos):
    for i in range(1, 5):
        if pos[f'{user}{i}']:
            return False
    return True


def remove(cell, pos):
    for i in pos.keys():
        if pos[i] == cell:
            pos[i] = -1
            return f'{i} has removed!'


def check(user, cell, pos):
    if cell == 100:
        return True
    for i in range(1, 5):
        if pos[f'{user}{i}'] == cell:
            return False
    if cell in pos.values():
        print(remove(cell, pos))
        return True
    else:
        return True

# class Mark:
#     cells = [i for i in range(1, 25)]
#     positions = start(2)
#
#     # args is the number of player
#     def __init__(self, num, which, position=-1):
#         self.num = num
#         self.which = which
#         self.position = position
#
#     def move(self, count, positions):
#         new = self.position + count
#         if new not in positions.get(self.num).values():
#             if new in positions.values().values():
#                 Mark.remove(new, positions)
#             self.position = (self.position + count) % 24
#             positions[self.num][self.which] = self.position
#         else:
#             return False
#
#     @staticmethod
#     def remove(new, positions):
#         for i in positions.keys():
#             for j in i.keys():
#                 if i.get(j) == new:
#                     positions[i][j] = -1
