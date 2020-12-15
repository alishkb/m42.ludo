from tkinter import *
from tkinter import ttk

win = Tk()
win.geometry('300x200')
win.resizable(False, False)
win.title('Hi LUDOer!')

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

print(en_color.get())
print(type(en_color.get()))

win.mainloop()