import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import requests
from bs4 import BeautifulSoup
from .SQLManager import SQLManager


class Player(object):

    def __init__(self, player_name, db_path=None):
        # Initialize SQL manager if database path is provided
        self.db_manager = SQLManager(db_path) if db_path else None
        self.player_name = player_name
        
        # use
        self.url = "http://search.espncricinfo.com/ci/content/player/search.html?search=" + \
            player_name.lower().replace(" ", "+") + "&x=0&y=0"
        self.page = requests.get(self.url)
        self.soup = BeautifulSoup(self.page.content, "html.parser")
        self.player_id = str(self.soup.find_all(class_='ColumnistSmry')
                             [0]).split('.html')[0].split('/')[-1]
        self.url_2 = f'https://www.espncricinfo.com/player/player-name-{self.player_id}'
        self.page_2 = requests.get(self.url_2)
        self.soup2 = BeautifulSoup(self.page_2.content, "html.parser")

        self.temp_url = 'https://www.espncricinfo.com/player/player-name-{self.player_id}/tests-odi-t20-records'
        self.temp_page = requests.get(self.temp_url)
        self.temp_soup = BeautifulSoup(self.temp_page.content, "html.parser")

    def get_format_df(self, format_num, view, action):
        df = pd.read_html(
            f'https://stats.espncricinfo.com/ci/engine/player/{self.player_id}.html?class={format_num};template=results;type={action};view={view}')[3]
        return df

    def get_summary_stats(self, format_num, view, action):
        summary_df = pd.read_html(
            f'https://stats.espncricinfo.com/ci/engine/player/{self.player_id}.html?class={format_num};template=results;type={action};view={view}')[2]
        return summary_df

    def get_overall_df(self, type_num, view, action):
        overall_df = pd.read_html(
            f'https://stats.espncricinfo.com/ci/engine/player/{self.player_id}.html?class=11;template=results;type={action};view={view}')[type_num]
        return overall_df

    def get_career_df(self):
        # print(self.url)
        personal_df = pd.read_html(self.url_2)[0]
        return personal_df

    def get_personal_info(self, arg):
        # for item in self.soup2.findAll('span', {'class': 'ds-text-title-s ds-font-bold'}):
        #     items.append(item)
        results = self.soup2.find(id="__next")
        job_elements = results.find_all(
            "div", class_="ds-grid lg:ds-grid-cols-3 ds-grid-cols-2 ds-gap-4 ds-mb-8")
        text_list = []
        for job_element in job_elements:
            for i in job_element:
                for element in i:
                    text_list.append(element.text)
        print(text_list)
        if arg == "full_name":
            return text_list[1]
        elif arg == "birth_info":
            return text_list[3]
        elif arg == "age":
            return text_list[5]
        elif arg == "batting_style":
            return text_list[7]
        elif arg == "bowling_style":
            return text_list[9]
        elif arg == "playing_role":
            return text_list[11]
        # print(list1)

        #     "span", class_="ds-text-title-s ds-font-bold ds-text-ui-typo")
        # return elements
    def get_teams(self):
        results = self.soup2.find(id="__next")
        job_elements = results.find_all(
            "div", class_="ds-grid lg:ds-grid-cols-3 ds-grid-cols-2 ds-gap-y-4")
        text_list = []
        for job_element in job_elements:
            for i in job_element:
                for element in i:
                    text_list.append(element.text)
        for i in text_list:
            if i == '':
                text_list.remove(i)
        return text_list

    def get_description(self):
        results = self.soup2.find(id="__next")
        job_elements = results.find_all(
            "div", class_="ds-relative ds-overflow-hidden ds-mt-6")
        text_list = []
        for job_element in job_elements:
            for i in job_element:
                for element in i:
                    text_list.append(element.text)
        for i in text_list:
            if i == '':
                text_list.remove(i)
        return text_list

    def get_overview_df(self, pos):
        df = pd.read_html(
            f'https://www.espncricinfo.com/player/player-name-{self.player_id}')[pos]
        return df
    
    def save_to_database(self):
        """
        Save player data to database.
        
        Returns:
            bool: True if successful, False otherwise
        """
        if not self.db_manager:
            print("Database manager not initialized. Provide db_path in constructor.")
            return False
            
        try:
            player_data = {
                'name': self.player_name,
                'full_name': self.get_personal_info('full_name'),
                'birth_info': self.get_personal_info('birth_info'),
                'age': self.get_personal_info('age'),
                'batting_style': self.get_personal_info('batting_style'),
                'bowling_style': self.get_personal_info('bowling_style'),
                'playing_role': self.get_personal_info('playing_role'),
                'teams': self.get_teams(),
                'description': self.get_description()
            }
            
            return self.db_manager.store_player_data(self.player_id, player_data)
        except Exception as e:
            print(f"Error saving player to database: {e}")
            return False
    
    def get_from_database(self):
        """
        Retrieve player data from database.
        
        Returns:
            dict or None: Player data if found, None otherwise
        """
        if not self.db_manager:
            print("Database manager not initialized. Provide db_path in constructor.")
            return None
            
        return self.db_manager.get_player_data(self.player_id)
    
    def get_career_stats_from_db(self, stat_type='batting'):
        """
        Get career statistics from database.
        
        Args:
            stat_type (str): Type of stats ('batting' or 'bowling')
            
        Returns:
            pd.DataFrame: Career statistics
        """
        if not self.db_manager:
            print("Database manager not initialized. Provide db_path in constructor.")
            return pd.DataFrame()
            
        return self.db_manager.get_player_stats(self.player_id, stat_type)


# print(Player('Mithali Raj').get_description())
