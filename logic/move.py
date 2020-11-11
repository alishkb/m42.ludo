def start(player_num):
    l_of_mark = ['first', 'second', 'third', 'forth']
    for i in range(player_num):
        positions = {i: {j: -1 for j in l_of_mark}}
        return positions


class Mark:
    cells = [i for i in range(1, 25)]
    positions = start(2)

    # args is the number of player
    def __init__(self, num, which, position=-1):
        self.num = num
        self.which = which
        self.position = position

    def move(self, count, positions):
        new = self.position + count
        if new not in positions.get(self.num).values():
            if new in positions.values().values():
                Mark.remove(new, positions)
            self.position = (self.position + count) % 24
            positions[self.num][self.which] = self.position
        else:
            return False

    @staticmethod
    def remove(new, positions):
        for i in positions.keys():
            for j in i.keys():
                if i.get(j) == new:
                    positions[i][j] = -1
