# -*- coding: utf-8 -*-

from tkinter import *
from tkinter import ttk

from analysis import Analysis


class GUI:
    def __init__(self):
        sheet_link = 'https://docs.google.com/spreadsheets/u/1/d/e/2PACX-1vS5qVKbg9hoLHg00Y5AqZu5XQxylCKHDjlOL0y3MtDRAVHmJcdkCp9tzi5m9kXwES8ObCqplRXHSW4M/pubhtml#'
        self.analysis = Analysis(sheet_link)
        self.analysis.caller()

        self.root = Tk()
        self.root.minsize(width=500, height=500)
        self.selected = 'Nenhum'

    def select_field(self):
        options = self.analysis.champions
        self.combobox = ttk.Combobox(
            self.root, values=options)
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
