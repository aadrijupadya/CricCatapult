import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import requests
from bs4 import BeautifulSoup
import geocoder
import geopandas
class Scoreboard(object):
    
    def __init__(self):
        self.url ="https://www.espncricinfo.com/live-cricket-score"
        self.page = requests.get(self.url)
        self.soup = BeautifulSoup(self.page.content, 'html.parser')
        
    def scores(self):
        data = self.soup.find_all("div", class_="ds-px-4 ds-py-3")
        text_list = []
        for data in data:
            for i in data:
                for element in i:
                    text_list.append(element.text)
        for i in text_list:
            if i == '':
                text_list.remove(i)
        return pd.Series(text_list)
    
    def scores_df(self):
        data = self.soup.find_all("div", class_="ds-px-4 ds-py-3")
        text_list = []
        for data in data:
            for i in data:
                for element in i:
                    text_list.append(element.text)
        for i in text_list:
            if i == '':
                text_list.remove(i)
        df = pd.Series(text_list).str.split(pat=",", expand=True )
        return df


print(Scoreboard().scores()[0])
print(Scoreboard().scores()[1])
print(Scoreboard().scores()[2])