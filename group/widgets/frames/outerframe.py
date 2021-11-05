from tkinter import ttk
import tkinter as tk 
from tkinter import messagebox

class UserInputFrame(tk.Frame):
    def __init__(self,color=None,width=None,height=None):
        super().__init__(root)
        frame = tk.Frame(root)
        frame.configure({'bg':color,'width':width,'height':height}).render
        frame.place(relx=0.08,rely=0.08)
        print('Frame working')


