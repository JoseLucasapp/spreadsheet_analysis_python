from tkinter import *
from tkinter import ttk


class GUI:
    def __init__(self):
        self.root = Tk()
        frm = ttk.Frame(self.root, padding=10)
        frm.grid()
        self.root.mainloop()


if __name__ == '__main__':
    gui = GUI()
