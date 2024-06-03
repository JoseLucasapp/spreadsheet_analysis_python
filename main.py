import pandas as pd
import requests
import io


class Analysis:
    def __init__(self, link):
        get_content = requests.get(link).content
        self.csv = pd.read_html(io.StringIO(get_content.decode('utf-8')))
        self.sheet_titles = {}

    def get_title_values_from_sheet(self):
        for index, data in enumerate(self.csv[1].get('Unnamed: 1')):
            self.sheet_titles[data] = [
                {"titles": self.csv[1].get('Unnamed: 2')[index]},
                {"second": self.csv[1].get('Unnamed: 3')[index]},
                {"finals": self.csv[1].get('Unnamed: 4')[index]},
                {"state": self.csv[1].get('Unnamed: 5')[index]}
            ]

    def caller(self):
        print(self.csv[0])
        self.get_title_values_from_sheet()
        print(self.sheet_titles)


if (__name__ == '__main__'):
    sheet_link = 'https://docs.google.com/spreadsheets/u/1/d/e/2PACX-1vS5qVKbg9hoLHg00Y5AqZu5XQxylCKHDjlOL0y3MtDRAVHmJcdkCp9tzi5m9kXwES8ObCqplRXHSW4M/pubhtml#'
    main = Analysis(sheet_link)

    main.caller()
