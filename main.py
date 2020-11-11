from logic.act import *
from logic.move import *
import logic.player

player_num = i = 1
player_c = ['red', 'blue', 'green', 'yellow']
user_c = None
while player_num > 4 or player_num < 2:
    player_num = int(input('Enter Number of Players: '))
    print()
while i <= player_num:
    user_n = input(f'Enter Name of Player {i}: ')
    user_p = input(f'Enter Pass of Player {i}: ')
    while logic.player.add(user_n, user_p):
        user_p = input(f'ReEnter Correct Pass P{i}: ')
    while user_c not in player_c:
        user_c = input(f'Enter Color of Player {i}: ')
    player_c.remove(user_c)
    logic.player.data(user_n, user_c, i)
    user_num = i
    i += 1

user_h = player_home(player_num)
pos = start(player_num)
j = 0
while True:
    num = j % player_num
    chance = dice()


    j += 1
