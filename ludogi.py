from tkinter import *
from tkinter import ttk, messagebox
from gui.plate import *
from logic.act import *
from logic.move import *

# from main import *

# TODO: defining hard-coded users is not good! Use file instead.
player_db = {'ali': 'alish', 'mina': 'minash'}
# color = []

start_win = Tk()
start_win.geometry('300x300')
start_win.resizable(False, False)
start_win.title('Hi LUDOer!')

# TODO: Not a good dictionary name. better: players
player = {}


def game():
    start_win.withdraw()
    win = Toplevel(start_win)
    win.geometry('820x570')
    win.resizable(False, False)
    win.title('AliSH LUDO')

    menu_bar = Menu(win)
    win.config(menu=menu_bar)

    cnv = Canvas(win, width=820, height=570, background='white')
    cnv.create_rectangle(10, 10, 260, 285, outline='black')
    cnv.create_rectangle(10, 285, 260, 560, outline='black')
    cnv.create_rectangle(260, 10, 810, 560, outline='black')

    positions = position
    for i in range(24):
        cnv.create_oval(positions.get(i))

    for i in range(1, 5):
        cnv.create_oval(positions.get(f's{i}'), fill='silver')
        cnv.create_oval(positions.get(f'f{i}'), fill='springgreen')
    cnv.place(relx=0, rely=0)

    # TODO: Defining nested functions is usually dirty code except a few cases like decorator.
    def lon_in():
        if len(player.keys()) < 4:
            login_win = Tk()
            login_win.geometry('300x200')
            login_win.resizable(False, False)
            login_win.title('Log In')

            en_user = Entry(login_win)
            en_user.place(relx=.35, rely=.1, width=155)
            lb_user = Label(login_win, text='username :')
            lb_user.place(relx=.1, rely=.1, width=60)

            en_pass = Entry(login_win, show='*')
            en_pass.place(relx=.35, rely=.25, width=155)
            lb_pass = Label(login_win, text='password :')
            lb_pass.place(relx=.1, rely=.25, width=60)

            en_color = ttk.Combobox(login_win, values=('blue', 'green', 'red', 'yellow'), state='readonly')
            en_color.place(relx=.35, rely=.4, width=155)
            lb_color = Label(login_win, text='color :')
            lb_color.place(relx=.1, rely=.4, width=60)

            # TODO: Again nested functions!
            def check_sign():
                try:
                    if en_user.get() in player_db.keys() and player_db.get(en_user.get()) == en_pass.get():
                        if en_color.get() not in player.values() and en_color.get():
                            if en_user.get() not in player:
                                f = len(player.keys()) + 1
                                player.update({en_user.get(): en_color.get()})
                                lb_playing = Label(win, text=f'{f}- {en_user.get()}', font=('Arial', 10, 'bold'),
                                                   foreground=en_color.get(), background='white')
                                lb_playing.place(x=25, y=30 + 20 * f)
                                f += 1
                                login_win.destroy()
                            else:
                                messagebox.showerror('ERROR', "This User is exist in the game!")
                        else:
                            messagebox.showerror('ERROR', "You can't choose this Color!")
                    else:
                        messagebox.showerror('ERROR', "Your Username or Password is Incorrect!")
                        en_user.delete(0, END)
                        en_pass.delete(0, END)
                except:
                    messagebox.showerror('ERROR', "Your Inputs are Incorrect!")
                    en_user.delete(0, END)
                    en_pass.delete(0, END)
                    en_color.delete(0, END)

            def sign_up():
                signup = Toplevel(login_win)
                signup.title('Sign Up')
                signup.geometry('400x200')
                signup.resizable(False, False)

                en_user_n = Entry(signup, width=40)
                en_user_n.place(relx=0.3, rely=0.05)
                lb_user_n = Label(signup, text='username : ')
                lb_user_n.place(relx=0.1, rely=0.05)

                en_pass_n = Entry(signup, width=40, show='*')
                en_pass_n.place(relx=0.3, rely=0.25)
                lb_pass_n = Label(signup, text='password : ')
                lb_pass_n.place(relx=0.1, rely=0.25)

                en_repass = Entry(signup, width=40, show='*')
                en_repass.place(relx=0.3, rely=0.45)
                lb_repass = Label(signup, text='reenter pass : ')
                lb_repass.place(relx=0.1, rely=0.45)

                def add_user():
                    try:
                        add_it = None
                        if en_user_n.get() not in player_db.keys() and en_user_n.get():
                            if en_pass_n.get() == en_repass.get() and en_pass_n.get():
                                player_db.update({en_user_n.get(): en_pass_n.get()})
                                messagebox.showinfo('Success', 'Done!')
                                signup.destroy()
                                add_it = 'yes'
                            else:
                                messagebox.showerror('ERROR', "Password doesn't match Reenter Pass")
                                en_pass_n.delete(0, END)
                                en_repass.delete(0, END)
                                add_it = 'yes'
                        test_it = 2 * add_it
                    except:
                        messagebox.showerror('ERROR', "This Username isn't acceptable!")
                        en_user_n.delete(0, END)
                        en_pass_n.delete(0, END)
                        en_repass.delete(0, END)

                btn_add_user = ttk.Button(signup, text='Add User', command=add_user)
                btn_add_user.place(relx=0.5, rely=0.75)

            btn_login = ttk.Button(login_win, text='login', command=check_sign)  # command=
            btn_login.place(relx=.35, rely=.6, width=90)

            btn_sign_up = ttk.Button(login_win, text='sign up', command=sign_up)
            btn_sign_up.place(relx=.35, rely=.8, width=90)
        else:
            messagebox.showerror('ERROR', "You can't add another player!")

    def new_game():
        # save datas
        win.destroy()
        # TODO: using "global" causes usually a dirty code! Do not use it at all except somewhere really necessary!
        global player
        player = {}
        game()

    def playing():
        if len(player.keys()) < 2:
            messagebox.showerror('ERROR', 'You should add Player!')
        else:
            game_menu.entryconfigure(0, state='disable')
            game_menu.entryconfigure(1, state='disable')
            player_num = len(player.keys())
            # users_li = [s for s in player.keys()]
            users_li = list(player.keys())  # It is better!

            user_h = player_home(player_num)
            user_o = player_out(player_num)
            user_f = player_win(player_num)
            pos = start(users_li, user_o)

            # TODO: You are using too much nested things! Now a nested class! Do not define everyhing nested.
            # TODO: Define it directly in the module (global scope).
            class Btn:
                def __init__(self, x, y, name, color):
                    self.x = x
                    self.y = y
                    self.name = name
                    self.color = color

                def create(self):
                    nut_btn = Button(win, text=self.name, fg='white', bg=self.color, state='disable')
                    nut_btn.place(x=self.x, y=self.y, width=30, height=30)

                # def enable(self):
                #     change to enable

                # def remove(self):
                #     delete btn

            # for p in player.keys():
            #     for i in [1, 2, 3, 4]:
            #         btn.append(f'{p}{i}')
            #         e = pos.get(f'{p}{i}')
            #         c = player.get(p)
            #         # img = PhotoImage(file=fr'nuts\{c}.png')
            #         nut = Btn(positions.get(e)[0] + 10, positions.get(e)[1] + 10, p, c)
            #         nut.create()
            #         nut_dic = {nut: (positions.get(e)[0] + 10, positions.get(e)[1] + 10)}
            #         btn.append(nut_dic)
            btn = {}
            # pq = []
            # for p in player.keys():
            #     for q in [1, 2, 3, 4]:
            #         pq.append(f'{p}{q}')
            pq = [f'{p}{q}' for p in player for q in range(1, 5)]  # It is better!

            # TODO: Instead of defining a list of strings:
            #  ['userA1', 'userA2', ...] ,
            #  define a list of tuples : [('userA', 1), ('userA', 2) , ... ]
            # Also define pos as dictionary of tuples to everything you want :
            # {('userA', 1): value1, ('userA', 2): value2 , ...}

            for k in pq:
                e = pos.get(k)
                c = player.get(k[:-1])
                nut = Btn(positions.get(e)[0] + 10, positions.get(e)[1] + 10, k[:-1], c)
                nut.create()
                nut_dic = {k: (positions.get(e)[0] + 10, positions.get(e)[1] + 10)}
                btn.update(nut_dic)
            print(btn)
            # for i in range(len(btn)):
            #     for j in btn[i].keys():
            #         if j == 'mina2':
            #             print(btn[i].values())

            rc = 0
            cd = 0
            pd = 0

            def roll():
                global rc, cd
                rc = dice()
                cd += 1
                # return ch
                lb_roll = Label(win, text=rc, font=('Arial', 20, 'bold'))
                lb_roll.place(x=60, y=450, width=150)

            btn_roll = ttk.Button(win, text='ROLL', state='disable')
            btn_roll.place(x=60, y=400, width=150)  # , font=('Arial', 10, 'bold')

            def choose_nut():
                # enable nuts that can move
                # onclick: move
                pass

            j = 0
            while True:
                #     print('hi')
                num = j % player_num
                user = users_li[num]
                home = user_h[num]
                final = user_f[num]
                out = user_o[num]
                winner_list = []
                if check_final(user, pos, final):
                    pass
                else:
                    chance = 6
                    k = 1
                    while chance == 6 or k <= 3:
                        btn_roll.configure(state='enable', command=roll)
                        chance = rc
                        if cd == pd:
                            while True:
                                if check_marks():  # return treu
                                    choose_nut()
                                    # res = moving(user, choice, chance, pos, home)
                                    if check_final(user, pos, final):
                                        winner_list.append(user)
                                        messagebox.showinfo('CONGRATULATION', message=f'Congratulation {user}!')
                                        break
                                    else:
                                        k = 4
                                        break
                                else:
                                    k = 4
                                    break
                        pd += 1
                if check_end(player.keys(), pos, user_f):
                    messagebox.showinfo('The END', message=f'WiNnErS ArE: {[w for w in winner_list]}!')
                    break
                j += 1

    game_menu = Menu(menu_bar, tearoff=0)
    game_menu.add_command(label='Add Player', command=lon_in)
    game_menu.add_command(label='Start Game', command=playing)
    game_menu.add_command(label='New Game', command=new_game)
    game_menu.add_command(labe='Exit', command=start_win.destroy)
    menu_bar.add_cascade(label='Game', menu=game_menu)

    lb_player = Label(win, text='Players', font=('Arial', 10, 'bold'))
    lb_player.place(x=25, y=20, width=200)


# TODO: This empty entrance page is not a good design.
btn_start = ttk.Button(start_win, text='Start **AliSH LUDO**', command=game)
btn_start.place(relx=.2, rely=.6, width=180)

start_win.mainloop()
