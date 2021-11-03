import tkinter as tk

global username 
username= tk.StringVar()


def user_name():
    print('within {}'.format(__name__))
    print(username.get())

 
