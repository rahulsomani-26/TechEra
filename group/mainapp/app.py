import tkinter as tk 
# from widgets.frames import UserInputFrame


class MainApplication(tk.Tk):
    def __init__(self,yourtitle):
        super().__init__()
        self.title(yourtitle)

class UserInputFrame(tk.Frame):
    def __init__(self):
        super().__init__(root)
        frame = tk.Frame(root)
        
        # frame.configure({'bg':color,'width':width,'height':height})
        # frame.place(relx=0.08,rely=0.08)

        name_label = tk.Label(root,text="Enter Name")
        name_label.place(relx=0.1,rely=0.1)

        name_entry = tk.Entry(root)
        name_entry.place(relx=0.1,rely=0.2)


        


if __name__ == '__main__':
    root = MainApplication('Lib Management System')
    root.state('zoomed')
    root.configure({'bg':'#465081'})
    left_frame = UserInputFrame()
    left_frame.place(relx=0.08)
    root.mainloop()
