from tkinter import *
from tkinter import ttk


class GUI:
    def __init__(self):
        self.root = Tk()
        self.root.minsize(width=500, height=500)
        self.selected = 'Nenhum'

    def select_field(self):
        options = []
        self.combobox = ttk.Combobox(self.root, values=options)
        self.combobox.pack(pady=20)

        self.combobox.bind("<<ComboboxSelected>>", self.selected_option)

        self.label_selected = ttk.Label(
            self.root, text=f"Selecionado: {self.selected or 'Nenhum'}")
        self.label_selected.pack(pady=20)

    def selected_option(self, event):
        self.selected = self.combobox.get()
        self.label_selected.config(text=f"Selecionado: {self.selected}")

    def caller(self):
        self.select_field()
        self.root.mainloop()


if __name__ == '__main__':
    gui = GUI().caller()
