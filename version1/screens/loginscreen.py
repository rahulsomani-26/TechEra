import tkinter as tk 
from tkinter import ttk

from screens.dashboard import show_dashboard 


def check_credentials():
    print('echo')

def test():
    print('Trying to get the dashboad screen ')
    show_dashboard(tk.Tk())


def create_login_screen(root):
     
    username = tk.StringVar()
    password = tk.StringVar()


    # Frame

    outer_frame = tk.Frame(root)
    outer_frame.place(relwidth=1,relheight=1)
    outer_frame.configure({'background':'#322E2E'})


    # text logo

    text_logo = ttk.Label(outer_frame,text='Shopify',foreground='#CDE82A', background='#322E2E')
    text_logo.place(relx=0.08,rely=0.08)
    text_logo.configure(font=(r'C:\Users\soman\Downloads\montserrat8',32))

# logo description 

    logo_description = ttk.Label(outer_frame,text="For all your needs",foreground='#CDE82A', background='#322E2E')
    logo_description.place(relx=0.08,rely=0.14)
    logo_description.configure(font=(r'C:\Users\soman\Downloads\montserrat8',16))


# Login fields.

# username label

    username_label = ttk.Label(outer_frame,text="Username",foreground='#CDE82A', background='#322E2E')
    username_label.place(relx=0.2,rely=0.35)
    username_label.configure(font=(r'C:\Users\soman\Downloads\montserrat8',24))

# username Entry


    name = ttk.Entry(outer_frame,textvariable=username,foreground='#000')
    name.place(relx=0.35,rely=0.35)
    name.configure(font=(r'C:\Users\soman\Downloads\montserrat8',24))

    print(name.focus)

# password label

    password_label = ttk.Label(outer_frame,text="Password",foreground='#CDE82A', background='#322E2E')
    password_label.place(relx=0.2,rely=0.45)
    password_label.configure(font=(r'C:\Users\soman\Downloads\montserrat8',24))

# password Entry


    pwd = ttk.Entry(outer_frame,textvariable=password,foreground='#000')
    pwd.place(relx=0.35,rely=0.45)
    pwd.configure(font=(r'C:\Users\soman\Downloads\montserrat8',24))




    login_btn = ttk.Button(outer_frame, text="Login",padding=(30,10,30,10),command=check_credentials)
    login_btn.place(relx=0.2,rely=0.6)
    # login_btn.configure()



    signup_btn = ttk.Button(outer_frame, text="SignUp",padding=(30,10,30,10),command=test)
    signup_btn.place(relx=0.4,rely=0.6)
    # signup_btn.configure()




    

