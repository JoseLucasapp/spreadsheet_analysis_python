import pandas as pd
import requests
import io
from matplotlib import pyplot as plt
import numpy as np


class Analysis:
    def __init__(self, link):
        get_content = requests.get(link).content
        self.csv = pd.read_html(io.StringIO(get_content.decode('ISO-8859-1')))
        self.sheet_titles = {}
        self.sheet_finals = []
        self.titles_by_state = {}

    def get_title_values_from_sheet(self):
        for index, data in enumerate(self.csv[1].get('Unnamed: 1')):
            self.sheet_titles[data] = [
                {"titles": self.csv[1].get('Unnamed: 2')[index]},
                {"second": self.csv[1].get('Unnamed: 3')[index]},
                {"finals": self.csv[1].get('Unnamed: 4')[index]},
                {"state": self.csv[1].get('Unnamed: 5')[index]}
            ]

    def get_all_finals_from_sheet(self):
        for index, data in enumerate(self.csv[0].get('Unnamed: 1')):
            self.sheet_finals.append(
                {"champion": data, "second": self.csv[0].get('Unnamed: 2')[index]})

    def organize_titles_by_state(self):
        for i in self.sheet_titles:
            state = self.sheet_titles[i][3]['state']
            if state not in self.titles_by_state:
                self.titles_by_state[f'{state}'] = self.sheet_titles[i][0]['titles']
            else:
                self.titles_by_state[f'{state}'] += self.sheet_titles[i][0]['titles']

    def caller(self):
        self.get_title_values_from_sheet()
        self.get_all_finals_from_sheet()
        self.organize_titles_by_state()
