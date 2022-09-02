import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import requests
from bs4 import BeautifulSoup


class Records(object):
    def __init__(self):
        a = 1

    def get_records_by_team(self, team_id, record, type, format):
        self.url = f'https://stats.espncricinfo.com/ci/engine/records/{type}/{record}.html?class={format};id={team_id};type=team'
        self.page = requests.get(self.url)
        self.soup = BeautifulSoup(self.page.content, "html.parser")
        df = pd.read_html(self.url)[0]
        return df

    def get_records_by_tournament(self, type, record, tourney_id):
        self.url = f'https://stats.espncricinfo.com/ci/engine/records/{type}/{record}.html?id={tourney_id};type=trophy'
        self.page = requests.get(self.url)
        self.soup = BeautifulSoup(self.page.content, "html.parser")
        df = pd.read_html(self.url)[0]
        return df

    def get_records_h2h(self, team_id1, team_id2, record, type):
        self.url = f'https://stats.espncricinfo.com/ci/engine/records/{type}/{record}.html?class=2;id={team_id1};id={team_id2};type=headtohead'
        self.page = requests.get(self.url)
        self.soup = BeautifulSoup(self.page.content, "html.parser")
        df = pd.read_html(self.url)[0]
        return df

    def get_records_year(self, year, record, type):
        self.url = f'https://stats.espncricinfo.com/ci/engine/records/{type}/{record}.html?class=1;id={year};type=year'
        self.page = requests.get(self.url)
        self.soup = BeautifulSoup(self.page.content, "html.parser")
        df = pd.read_html(self.url)[0]
        return df

    def get_records_ground(self, type, record, ground_id):
        self.url = f'https://stats.espncricinfo.com/ci/engine/records/{type}/{record}.html?class=2;id={ground_id};type=ground'

    def get_general_records(self, record_id):
        self.url = f'https://stats.espncricinfo.com/ci/content/records/{record_id}.html'
        self.page = requests.get(self.url)
        self.soup = BeautifulSoup(self.page.content, "html.parser")
        df = pd.read_html(self.url)[0]
        return df

    def get_ipl_records(self, format, record):
        self.url = f"https://stats.espncricinfo.com/ci/engine/records/{format}/{record_id}.html?id=14452;type=tournament"
        self.page = requests.get(self.url)
        self.soup = BeautifulSoup(self.page.content, "html.parser")
        df = pd.read_html(self.url)[0]
        return df

    def get_bbl_records(self, format, record):
        self.url = f"https://stats.espncricinfo.com/ci/engine/records/{format}/{record}.html?id=158;type=trophy"
        self.page = requests.get(self.url)
        self.soup = BeautifulSoup(self.page.content, "html.parser")
        df = pd.read_html(self.url)[0]
        return df

    def get_et20_records(self, format, record):
        self.url = f"https://stats.espncricinfo.com/ci/engine/records/{format}/{record}.html?id=113;type=trophy"
        self.page = requests.get(self.url)
        self.soup = BeautifulSoup(self.page.content, "html.parser")
        df = pd.read_html(self.url)[0]
        return df

    def get_psl_records(self, format, record):
        self.url = f"https://stats.espncricinfo.com/ci/engine/records/{format}/{record}.html?id=205;type=trophy"
        self.page = requests.get(self.url)
        self.soup = BeautifulSoup(self.page.content, "html.parser")
        df = pd.read_html(self.url)[0]
        return df

    def get_psl_records(self, format, record):
        self.url = f"https://stats.espncricinfo.com/ci/engine/records/{format}/{record}.html?id=748;type=trophy"
        self.page = requests.get(self.url)
        self.soup = BeautifulSoup(self.page.content, "html.parser")
        df = pd.read_html(self.url)[0]
        return df


print(Records().get_psl_records("batting", "most_runs_career"))
