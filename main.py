# -*- coding: utf-8 -*-
from tkinter import ttk
from tkinter import *
from PIL import Image, ImageTk

from convert import Convert
from analysis import Analysis


class GUI:
    def __init__(self):
        sheet_link = 'https://docs.google.com/spreadsheets/u/1/d/e/2PACX-1vS5qVKbg9hoLHg00Y5AqZu5XQxylCKHDjlOL0y3MtDRAVHmJcdkCp9tzi5m9kXwES8ObCqplRXHSW4M/pubhtml#'
        self.analysis = Analysis(sheet_link)
        Convert()
        from chart_generator import Generate_Charts
        self.chart_generator = Generate_Charts(self.analysis.sheet_titles)

        self.root = Tk()
        self.root.minsize(width=500, height=500)
        self.selected = 'Nenhum'
        self.photo = None

    def on_click_display_chart(self):
        self.chart_generator.championship_chart()
        self.display_chart(600, 500)

    def display_chart(self, w=400, h=400):
        image = Image.open('./chart.png')
        resized = image.resize((w, h))
        self.photo = ImageTk.PhotoImage(image=resized)
        label_image_chart = ttk.Label(self.root, image=self.photo)
        label_image_chart.pack()

    def select_field(self, options):
        self.combobox = ttk.Combobox(
            self.root, values=options)
        self.combobox.pack()

        self.combobox.bind("<<ComboboxSelected>>", self.selected_option)

        self.label_selected = ttk.Label(
            self.root, text=f"Selecionado: {self.selected or 'Nenhum'}")
        self.label_selected.pack()

    def selected_option(self, event):
        self.selected = self.combobox.get()
        self.chart_generator.finals_win_percentage(self.selected)
        self.display_chart()
        self.label_selected.config(text=f"Selecionado: {self.selected}")

    def button(self):
        button = ttk.Button(self.root, text="Todos os campeões", command=self
                            .on_click_display_chart)
        button.pack()

    def caller(self):
        self.button()
        self.select_field(self.analysis.champions)
        self.root.mainloop()


if __name__ == '__main__':
    gui = GUI().caller()
