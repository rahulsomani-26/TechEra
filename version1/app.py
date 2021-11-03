import tkinter as tk 
from tkinter import ttk

from screens.loginscreen import create_login_screen 
from database.customerorder import DatabaseEngine



if __name__ == '__main__':

    database_engine=DatabaseEngine()

    root = tk.Tk()
    root.configure({'background':'#575151'})
    root.state('zoomed')
    root.title('Shopify')
    root.resizable(False,False)
    create_login_screen(root)
    root.mainloop()


 