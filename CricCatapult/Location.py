import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import requests
from bs4 import BeautifulSoup
import geocoder
import folium 

class Location(object):
    def __init__(self, match_id):
        self.url = "https://stats.espncricinfo.com/ci/engine/match/" + str(match_id) + ".html"
        self.page = requests.get(self.url)
        self.soup = BeautifulSoup(self.page.content, 'html.parser')

    def get_location(self):
        address = self.soup.find_all("div", class_="ds-p-0")
        text_list = []
        for address in address:
            for i in address:
                for element in i:
                    text_list.append(element.text)
        print(pd.Series(text_list[0]).str.split(pat=",", expand=True)[1] + " Cricket Ground")
    
    def get_map(self):
        address = self.soup.find_all("div", class_="ds-p-0")
        text_list = []
        for address in address:
            for i in address:
                for element in i:
                    text_list.append(element.text)
        venue = str(pd.Series(text_list[0]).str.split(pat=",", expand=True)[1] + " Cricket")
        g = geocoder.mapbox(venue, key="pk.eyJ1Ijoic3VtYW50aHBhbCIsImEiOiJjbDJycHl0bGwzNzM3M2Nsd3Y1dzZtdHBuIn0.C8bl-xGiXrmz_WBAeYpOsA")
        map = folium.Map(location=(g.latlng), zoom_start=8)
        folium.Marker((g.latlng)).add_to(map)
        map


print(Location("1249875").get_location())
# print(Location("1249875").get_map())