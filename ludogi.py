from tkinter import *
from tkinter import ttk, messagebox

player = {'ali': 'alish'}
color = []

start_win = Tk()
start_win.geometry('300x300')
start_win.resizable(False, False)
start_win.title('Hi LUDOer!')


def game():
    start_win.withdraw()
    win = Toplevel(start_win)
    win.geometry('820x520')
    win.resizable(False, False)
    win.title('AliSH LUDO')

    def do_nothing():
        pass

    menu_bar = Menu(win)
    win.config(menu=menu_bar)
    game_menu = Menu(menu_bar, tearoff=0)
    game_menu.add_command(label='Add Player', command=do_nothing)
    game_menu.add_command(label='Start Game', command=do_nothing)
    game_menu.add_command(label='New Game', command=do_nothing)
    game_menu.add_command(labe='Exit', command=do_nothing)
    menu_bar.add_cascade(label='Game', menu=game_menu)

    cnv = Canvas(win, width=820, height=520)
    cnv.create_rectangle(10, 10, 260, 260, outline='black')
    cnv.create_rectangle(10, 260, 260, 510, outline='black')
    cnv.create_rectangle(260, 10, 810, 510, outline='black')

    # cnv.create_oval(0, 150, 150, 250)
    cnv.place(relx=0, rely=0)

    lb_player = Label(win, text='Players', font=('Arial', 10, 'bold'))
    lb_player.place(x=25, y=20, width=200)

    # cnv_result = Canvas(win, width=800, height=500)
    # cnv.place(relx=0, rely=0)


btn_start = ttk.Button(start_win, text='Start **AliSH LUDO**', command=game)
btn_start.place(relx=.2, rely=.6, width=180)

start_win.mainloop()


def lon_in():
    win = Tk()
    win.geometry('300x200')
    win.resizable(False, False)
    win.title('Log In')

    en_user = Entry(win)
    en_user.place(relx=.35, rely=.1, width=155)
    lb_user = Label(win, text='username :')
    lb_user.place(relx=.1, rely=.1, width=60)

    en_pass = Entry(win)
    en_pass.place(relx=.35, rely=.25, width=155)
    lb_pass = Label(win, text='password :')
    lb_pass.place(relx=.1, rely=.25, width=60)

    en_color = ttk.Combobox(win, values=('blue', 'green', 'red', 'yellow'), state='readonly')
    en_color.place(relx=.35, rely=.4, width=155)
    lb_color = Label(win, text='color :')
    lb_color.place(relx=.1, rely=.4, width=60)

    # def check():
    #     try:
    #         if en_user.get() in player.keys() and player.get(en_user.get()) == en_pass.get() and en_color not in color:
    #             color.append(en_color.get())
    #             print(color)

    btn_login = ttk.Button(win, text='login')  # command=
    btn_login.place(relx=.35, rely=.6, width=90)

    btn_sign_up = ttk.Button(win, text='sign up')  # command=
    btn_sign_up.place(relx=.35, rely=.8, width=90)

# try:
#     if en_user.get() in player.keys() and player.get(en_user.get()) == en_pass.get():
#         login.withdraw()
#         profile = Toplevel(login, bg='blue')
#         profile.title('Hi')
#         profile.geometry('400x400')
#         profile.resizable(False, False)
#         lb = Label(profile, text=f'Welcome {en_user.get()}', font=('mitra', 25, 'bold'), fg='black')
#         lb.place(relx=0.2, rely=0.5)
#     else:
#         messagebox.showerror('ERROR', "Your Username or Password is Incorrect!")
#         en_user.delete(0, END)
#         en_pass.delete(0, END)
# except:
#     messagebox.showerror('ERROR', "Your Username or Password is Incorrect!")
#     en_user.delete(0, END)
#     en_pass.delete(0, END)
