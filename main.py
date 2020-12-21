# from logic.act import *
# from logic.move import *
# # from logic.player import *
# from ludogi import *
#
# player_num = len(player.keys())
# # player_num = i = 1
# # player_c = ['red', 'blue', 'green', 'yellow']
# # user_c = None
# # while player_num > 4 or player_num < 2:
# #     player_num = int(input('Enter Number of Players: '))
# #     print()
# # while i <= player_num:
#     # user_n = input(f'Enter Name of Player {i}: ')
#     # user_p = input(f'Enter Pass of Player {i}: ')
#     # while add(user_n, user_p):
#     #     user_p = input(f'ReEnter Correct Pass P{i}: ')
#     # while user_c not in player_c:
#     #     user_c = input(f'Enter Color of Player {i}: ')
#     # player_c.remove(user_c)
#     # data(user_n, user_c)
#     # i += 1
#
# users_li = [i for i in player.keys()]
#
# user_h = player_home(player_num)
# # print(user_h)
# pos = start(users_li)
# # print(pos)
# j = 0
# while True:
#     num = j % player_num
#     user = users_li[num]
#     winner_list = []
#     if check_final(user, pos):
#         pass
#     else:
#         home = user_h[num]
#         chance = 6
#         k = 1
#         while chance == 6 or k <= 3:
#             chance = dice()
#             print(chance)
#             while True:
#                 print([pos[f'{user}{i}'] for i in range(1, 5)])
#                 choice = input(f'Enter your mark {user}: ')
#                 res = moving(user, choice, chance, pos, home)
#                 if res == 'WIN':
#                     winner_list.append(user)
#                     print(f'CONGRATULATION {user}!')
#                     if check_final(user, pos):
#                         k = 4
#                         break
#                 elif res:
#                     k = 4
#                     break
#                 pos_test = pos
#                 if check_marks(user, chance, pos_test, home):
#                     print(pos)
#                     print(pos_test)
#                     print('you should choose another mark!')
#                 else:
#                     k += 1
#                     break
#     if check_end(pos):
#         print('Play is finished! Winners are:')
#         for i in winner_list:
#             print(i)
#         break
#     j += 1
