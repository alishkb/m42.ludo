from tkinter import *
from tkinter import ttk
from tkinter import messagebox

win = Tk()
win.resizable(False, False)
win.title('AliSH - LUDO')

player = {'ali': 'alish'}


def sign_in():
    login = Toplevel(win)
    login.title('Sign In')
    login.geometry('400x200')
    login.resizable(False, False)

    en_user = Entry(login, width=40)
    en_user.place(relx=0.3, rely=0.05)
    lb_user = Label(login, text='username : ')
    lb_user.place(relx=0.1, rely=0.05)

    en_pass = Entry(login, width=40, show='*')
    en_pass.place(relx=0.3, rely=0.25)
    lb_pass = Label(login, text='password : ')
    lb_pass.place(relx=0.1, rely=0.25)

    def check_sign():
        try:

            if en_user.get() in player.keys() and player.get(en_user.get()) == en_pass.get():
                login.withdraw()
                profile = Toplevel(login, bg='blue')
                profile.title('Hi')
                profile.geometry('400x400')
                profile.resizable(False, False)
                lb = Label(profile, text=f'Welcome {en_user.get()}', font=('mitra', 25, 'bold'), fg='black')
                lb.place(relx=0.2, rely=0.5)
            else:
                messagebox.showerror('ERROR', "Your Username or Password is Incorrect!")
                en_user.delete(0, END)
                en_pass.delete(0, END)
        except:
            messagebox.showerror('ERROR', "Your Username or Password is Incorrect!")
            en_user.delete(0, END)
            en_pass.delete(0, END)

    btn_sign_in = ttk.Button(login, text='Login', command=check_sign)
    btn_sign_in.place(relx=0.5, rely=0.75)


def sign_up():
    signup = Toplevel(win)
    signup.title('Sign Up')
    signup.geometry('400x200')
    signup.resizable(False, False)

    en_user = Entry(signup, width=40)
    en_user.place(relx=0.3, rely=0.05)
    lb_user = Label(signup, text='username : ')
    lb_user.place(relx=0.1, rely=0.05)

    en_pass = Entry(signup, width=40)
    en_pass.place(relx=0.3, rely=0.25)
    lb_pass = Label(signup, text='password : ')
    lb_pass.place(relx=0.1, rely=0.25)

    en_repass = Entry(signup, width=40)
    en_repass.place(relx=0.3, rely=0.45)
    lb_repass = Label(signup, text='reenter pass : ')
    lb_repass.place(relx=0.1, rely=0.45)

    def add_user():
        try:
            add_it = None
            if en_user.get() not in player.keys():
                if en_pass.get() == en_repass.get() and en_pass.get():
                    player.update({en_user.get(): en_pass.get()})
                    messagebox.showinfo('Success', 'Done!')
                    signup.destroy()
                    add_it = 'yes'
                else:
                    messagebox.showerror('ERROR', "Password doesn't match Reenter Pass")
                    en_user.delete(0, END)
                    en_pass.delete(0, END)
                    en_repass.delete(0, END)
                    add_it = 'yes'
            test_it = 2 * add_it
        except:
            messagebox.showerror('ERROR', 'This Username is already exist!')
            en_user.delete(0, END)
            en_pass.delete(0, END)
            en_repass.delete(0, END)

    btn_add_user = ttk.Button(signup, text='Add User', command=add_user)
    btn_add_user.place(relx=0.5, rely=0.75)





btn_sign_in = ttk.Button(win, text='Sign In', command=sign_in)
btn_sign_in.place(relx=0.3, rely=0.3)

btn_sign_up = ttk.Button(win, text='Sign Up', command=sign_up)
btn_sign_up.place(relx=0.3, rely=0.6)

win.mainloop()
