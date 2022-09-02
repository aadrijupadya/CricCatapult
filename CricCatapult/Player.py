import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import requests
from bs4 import BeautifulSoup


class Player(object):

    def __init__(self, player_name):
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

    def get_format_df(self, format_num, view):
        df = pd.read_html(
            f'https://stats.espncricinfo.com/ci/engine/player/{self.player_id}.html?class={format_num};template=results;type=batting;view={view}')[3]
        return df

    def get_summary_stats(self, format_num, view):
        summary_df = pd.read_html(
            f'https://stats.espncricinfo.com/ci/engine/player/{self.player_id}.html?class={format_num};template=results;type=batting;view={view}')[2]
        return summary_df

    def get_overall_df(self, type_num, view):
        overall_df = pd.read_html(
            f'https://stats.espncricinfo.com/ci/engine/player/{self.player_id}.html?class=11;template=results;type=batting;view={view}')[type_num]
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

    def get_records(self):
        results = self.temp_soup.find(id="__next")
        job_elements = results.find_all(
            "div", class_="ds-grid lg:ds-grid-cols-2 ds-bg-fill-content-prime")
        print(job_elements)
        text_list = []
        for job_element in job_elements:
            for i in job_element:
                for element in i:
                    text_list.append(element)
        return text_list

    def get_overview_df(self, pos):
        df = pd.read_html(
            f'https://www.espncricinfo.com/player/player-name-{self.player_id}')[pos]
        return df


print(Player('Mithali Raj').get_description())

# player = 'Virat Kohli'
# url = "http://search.espncricinfo.com/ci/content/player/search.html?search=" + \
#     player.lower().replace(" ", "+") + "&x=0&y=0"
# page = requests.get(url)clear

# soup = BeautifulSoup(page.content, "html.parser")

# format = 1

# format_name = ""
# if format == 1:
#     format_name = "Tests"
# elif format == 2:
#     format_name = "ODIs"
# else:
#     format_name = "T20s"


# print(df.shape)
