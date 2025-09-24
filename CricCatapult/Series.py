import ssl
from lib2to3.pgen2.pgen import DFAState
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import requests
import seaborn as sns
import pygame
from bs4 import BeautifulSoup
from .SQLManager import SQLManager
pd.options.display.max_columns = None
pd.options.display.max_rows = None
ssl._create_default_https_context = ssl._create_unverified_context


def clean(df, type):
    df = df.dropna(how='all')
    df = df.reset_index()
    if type == 'bat':
        df = df.drop(columns=['Unnamed: 8', 'Unnamed: 9'])
        df = df.rename(columns={"Unnamed: 1": "Dismissal"})
    elif type == 'bowl':
        list1 = []
        for i in range(len(df)):
            if len(df.iloc[i]['BOWLING'].split(' ')) > 5:
                list1.append(i)
        for i in list1:
            df = df.drop(i)
    df = df.drop(columns=['index'])

    s = df.style.set_table_styles([
        {
            "selector": "thead",
            "props": [("background-color", "dodgerblue"), ("color", "white"),
                      ("border", "3px solid red"),
                      ]
        },
    ])

    return df


class Series(object):
    def __init__(self, series_id=None, match_id=None, db_path=None):
        # Initialize SQL manager if database path is provided
        self.db_manager = SQLManager(db_path) if db_path else None
        
        if series_id is not None and match_id is not None:
            self.series_id = series_id
            self.match_id = match_id
            self.url = f"https://www.espncricinfo.com/series/series-name-{series_id}/match-name-{match_id}/full-scorecard"
            self.page = requests.get(self.url)
            self.soup = BeautifulSoup(self.page.content, "html.parser")
            # self.match_id = str(self.soup.find_all(class_='ColumnistSmry')
            #                     [0]).split('.html')[0].split('/')[-1]

    def batting_df(self, bat_first):
        if bat_first:
            df = pd.read_html(self.url)[0]
        else:
            df = pd.read_html(self.url)[2]

        df = clean(df, 'bat')
        return df

    def bowling_df(self, bowl_first):
        if bowl_first:
            df = pd.read_html(self.url)[1]
        else:
            df = pd.read_html(self.url)[3]
        df = clean(df, 'bowl')
        return df

    def test_bat(self, bat_first, inning):
        if bat_first and inning == 1:
            df = pd.read_html(self.url)[0]
        elif bat_first and inning == 2:
            df = pd.read_html(self.url)[4]
        elif not bat_first and inning == 1:
            df = pd.read_html(self.url)[2]
        elif not bat_first and inning == 2:
            df = pd.read_html(self.url)[6]
        df = clean(df, 'bat')
        return df

    def test_bowl(self, bowl_first, inning):
        if bowl_first and inning == 1:
            df = pd.read_html(self.url)[1]
        if bowl_first and inning == 2:
            df = pd.read_html(self.url)[5]
        if not bowl_first and inning == 1:
            df = pd.read_html(self.url)[3]
        if not bowl_first and inning == 2:
            df = pd.read_html(self.url)[7]

        df = clean(df, 'bowl')
        return df

    def get_general_df_test(self):
        df = pd.read_html(self.url)[8]
        df = clean(df, 'none')
        return df

    def get_general_df(self):
        df = pd.read_html(self.url)[6]
        df = clean(df, 'none')
        return df

    def get_standings(self):
        df = pd.read_html(self.url)[8]
        df = clean(df, 'none')
        return df

    def test_df(self):
        df = pd.read_html(self.url)[6]
        return df

    def current_series(self):
        url = "https://www.espncricinfo.com/ci/content/match/fixtures_futures.html"
        page = requests.get(url)
        soup = BeautifulSoup(page.content, 'html.parser')
        text_elements = []
        parsed_elements = []
        game_dict = {}
        header_list = []
        for element in soup.findAll("h2"):
            header_list.append(element.text)
        for element in soup.find("div", {"id": "first"}):
            text_elements.append(element.text.strip())
        for element in text_elements:
            if len(element) >= 1:
                parsed_elements.append(element.split("\n"))
        for element in parsed_elements:
            for subelement in element:
                if len(subelement) == 0:
                    element.remove(subelement)

        metadata = []
        for i in parsed_elements:
            list1 = []
            for a in i:
                if a in header_list:
                    pass
                else:
                    list1.append(a)
            game_dict[a] = list1
        data_tuples = list(zip(header_list, metadata))
        for i in data_tuples:
            print(i)
        return game_dict

    def get_series_by_year(self, year):
        url = f'https://www.espncricinfo.com/ci/engine/series/index.html?season={year};view=season'
        page = requests.get(url)
        soup = BeautifulSoup(page.content, 'html.parser')
        if format == 'test':
            text_elements = []
            for element in soup.find("section", {"class": "series-summary-wrap"}):
                text_elements.append(element.text.strip())
            text_elements
            print(text_elements)

    def get_results_by_year(self, year, format):
        url = f"https://stats.espncricinfo.com/ci/engine/records/team/match_results.html?class={format};id={year};type=year"
        df = pd.read_html(url)[0]
        return df

    def get_series_results(self, number):
        url = f"https://stats.espncricinfo.com/ci/content/records/{number}.html"
        df = pd.read_html(url)[0]
        return df

    def get_bowler_analysis(self):
        url = f"https://www.espncricinfo.com/series/series-name-{self.series_id}/match-name-{self.match_id}/match-statistics"
        self.page = requests.get(url)
        self.soup = BeautifulSoup(self.page.content, "html.parser")
        results = self.soup.find(id="__next")
        job_elements = results.find_all(
            "table", class_="ds-w-full ds-table ds-table-sm ds-table-bordered ds-border-collapse ds-border ds-border-line ds-table-auto ds-text-tight-xs")
        print(job_elements)

    def manhattan(self):
        def wicket_graph(wicket_list, num):
            for i in range(len(wicket_list)):
                for j in range(wicket_list[i]):
                    if num == 1:
                        plt.scatter(i, (runs[::2][i]) + 1)
                    else:
                        plt.scatter(i+width, (runs[::2][i]) + 1)
        width = 0.3
        url = f"https://www.espncricinfo.com/series/series-name-{self.series_id}/match-name-{self.match_id}/match-overs-comparison"
        self.page = requests.get(url)
        self.soup = BeautifulSoup(self.page.content, "html.parser")
        results = self.soup.find(id="__next")
        job_elements = results.find_all(
            "span", class_="ds-text-tight-s ds-font-regular ds-ml-1")
        over_info = []
        for i in job_elements:
            over_info.append(i.text)
        runs = []
        wickets = []
        for i in over_info:
            runs.append(i[1:3].strip())
            wickets.append(i[9:11].strip())
        overs = len(runs)/2
        overs = int(overs)
        runs = [int(i) for i in runs]
        print(wickets)
        x = [int(i) for i in range(0, overs)]
        print(runs[::2])
        x2 = [int(i) for i in range(overs, overs*2)]
        print(runs[1::2])
        x_axis = np.arange(len(x))
        wickets = [int(i) for i in wickets]
        wickets1 = wickets[::2]
        wickets2 = wickets[1::2]
        plt.bar(x_axis, runs[::2], width=width, label='Team1')
        plt.bar(x_axis + width, runs[1::2], width=width, label='Team2')
        plt.xticks(x_axis + width/2, [i+1 for i in range(len(x))])
        plt.title('Manhattan Graph')
        plt.xlabel('Over')
        plt.ylabel('Runs scored')
        wicket_graph(wickets1, 1)
        wicket_graph(wickets2, 2)
        plt.legend()

    def worm(self):

        def wicket_graph(wicket_list, num):
            for i in range(len(wicket_list)):
                for j in range(wicket_list[i]):
                    if num == 1:
                        plt.scatter(i, (list1[i]) + 10, color='green')
                    else:
                        plt.scatter(i, (list2[i]) + 10, color='blue')
        width = 0.3
        url = f"https://www.espncricinfo.com/series/series-name-{self.series_id}/match-name-{self.match_id}/match-overs-comparison"
        self.page = requests.get(url)
        self.soup = BeautifulSoup(self.page.content, "html.parser")
        results = self.soup.find(id="__next")
        job_elements = results.find_all(
            "span", class_="ds-text-tight-s ds-font-regular ds-ml-1")
        over_info = []
        for i in job_elements:
            over_info.append(i.text)
        runs = []
        wickets = []
        for i in over_info:
            runs.append(i[1:3].strip())
            wickets.append(i[9:11].strip())
        runs = [int(i) for i in runs]
        team_1_bat = runs[::2]
        team_2_bat = runs[1::2]
        list1 = []
        list2 = []
        wickets = [int(i) for i in wickets]
        wickets1 = wickets[::2]
        wickets2 = wickets[1::2]
        for i in range(len(team_1_bat)):
            if i == 0:
                list1.append(team_1_bat[i])
                list2.append(team_2_bat[i])
            else:
                n = list1[i-1] + team_1_bat[i]
                j = list2[i-1] + team_2_bat[i]
                list1.append(n)
                list2.append(j)
        fig = plt.figure(figsize=(15, 10))
        plt.plot(np.arange(20), list1, 'g', marker='P', label='Pakistan')
        plt.plot(np.arange(20), list2, 'b', marker='^', label='India')
        plt.title('Worm Graph')
        plt.xlabel('Over')
        plt.ylabel('Runs scored')
        wicket_graph(wickets1, 1)
        wicket_graph(wickets2, 2)
        plt.legend()

    def mvp(self):
        url = f"https://www.espncricinfo.com/series/series-name-{self.series_id}/match-name-{self.match_id}/match-impact-player"
        df = pd.read_html(url)[0]
        return df

    def pitchmap(self, list1, list2, speeds):
        self.list1 = list1
        self.list2 = list2
        self.speeds = speeds
        spadl_config = {
            "length": 3.66,
            "width": 22.56,
            "origin_x": 0,
            "origin_y": 0,
        }
        plt.rcParams['figure.figsize'] = [2, 6]

        def plot_rectangle(x1, y1, x2, y2, ax, color):
            ax.plot([x1, x1], [y1, y2], color=color)
            ax.plot([x2, x2], [y1, y2], color=color)
            ax.plot([x1, x2], [y1, y1], color=color)
            ax.plot([x1, x2], [y2, y2], color=color)
            ax.set_facecolor("green")

        def pitch(list1, list2, speeds, ax=None, linecolor="green", fieldcolor=None, alpha=1, figsize=None, pitch_config=spadl_config, show=True):
            cfg = pitch_config
            if ax is None:
                fig = plt.figure()
                ax = fig.gca()
            x1, y1, x2, y2 = (
                cfg["origin_x"],
                cfg["origin_y"],
                cfg["origin_x"] + cfg["length"],
                cfg["origin_y"] + cfg["width"],
            )
            plot_rectangle(x1, y1, x2, y2, ax=ax, color=linecolor)
            # lower crease rectangle
            x1 = 0.51
            x2 = 3.15
            y1 = 1.22
            y2 = 2.44
            plot_rectangle(x1, y1, x2, y2, ax=ax, color='white')
            # upper crease rectangle
            x1 = 0.51
            x2 = 3.15
            y1 = 20.12
            y2 = 21.34
            plot_rectangle(x1, y1, x2, y2, ax=ax, color='white')
            plt.axvline(x=0.51, color='white')
            plt.axvline(x=3.15, color='white')
            plt.axhline(y=20.12, color='white', linestyle='-')
            plt.axhline(y=2.44, color='white', linestyle='-')
            plt.axhline(y=18, color='blue', linestyle='-')
            plt.axhline(y=12, color='black', linestyle='-')
            plt.axhline(y=10, color='red', linestyle='-')

            plt.text(2, 19, "Yorker")
            plt.text(2, 13, "Full")
            plt.text(2, 11, "Good")
            plt.text(2, 8, "Short")
            plt.ylabel("Length of pitch (m)")
            ax = sns.scatterplot(list1, list2, hue=speeds, palette='hot')
            norm = plt.Normalize(min(speeds), max(speeds))
            sm = plt.cm.ScalarMappable(cmap="hot", norm=norm)

            sm.set_array([])
        # Remove the legend and add a colorbar
            ax.get_legend().remove()
            ax.figure.colorbar(sm)
            # plt.axis(“off”)
            if show:
                plt.show()
            return ax
        pitch = pitch(self.list1, self.list2, self.speeds)
        return pitch
    
    def save_match_to_database(self, match_data=None):
        """
        Save match data to database.
        
        Args:
            match_data (dict, optional): Match information to store
            
        Returns:
            bool: True if successful, False otherwise
        """
        if not self.db_manager:
            print("Database manager not initialized. Provide db_path in constructor.")
            return False
            
        if not hasattr(self, 'match_id') or not hasattr(self, 'series_id'):
            print("Match ID and Series ID are required to save match data.")
            return False
            
        try:
            if match_data is None:
                match_data = {
                    'series_id': self.series_id,
                    'date': '',  # Could be extracted from page if needed
                    'format': '',  # Could be determined from URL patterns
                    'team1': '',  # Could be extracted from scorecard
                    'team2': '',  # Could be extracted from scorecard
                    'result': '',  # Could be extracted from page
                    'venue': ''  # Could be extracted from page
                }
            
            return self.db_manager.store_match_data(self.match_id, match_data)
        except Exception as e:
            print(f"Error saving match to database: {e}")
            return False
    
    def save_batting_stats_to_database(self, batting_df, innings=1, team_players=None):
        """
        Save batting statistics to database.
        
        Args:
            batting_df (pd.DataFrame): Batting statistics DataFrame
            innings (int): Innings number
            team_players (dict): Mapping of player names to player IDs
            
        Returns:
            bool: True if successful, False otherwise
        """
        if not self.db_manager:
            print("Database manager not initialized. Provide db_path in constructor.")
            return False
            
        try:
            for _, row in batting_df.iterrows():
                # Extract player name (assuming it's in the first column)
                player_name = row.iloc[0] if len(row) > 0 else ''
                
                # Try to get player ID from mapping or use name as fallback
                player_id = team_players.get(player_name, player_name) if team_players else player_name
                
                stats_data = {
                    'player_id': player_id,
                    'match_id': self.match_id,
                    'series_id': self.series_id,
                    'innings': innings,
                    'runs': self._safe_int(row.get('Runs', row.get('R', 0))),
                    'balls_faced': self._safe_int(row.get('Balls', row.get('B', 0))),
                    'fours': self._safe_int(row.get('4s', 0)),
                    'sixes': self._safe_int(row.get('6s', 0)),
                    'strike_rate': self._safe_float(row.get('SR', 0.0)),
                    'dismissal': str(row.get('Dismissal', ''))
                }
                
                self.db_manager.store_batting_stats(stats_data)
            
            return True
        except Exception as e:
            print(f"Error saving batting stats to database: {e}")
            return False
    
    def save_bowling_stats_to_database(self, bowling_df, innings=1, team_players=None):
        """
        Save bowling statistics to database.
        
        Args:
            bowling_df (pd.DataFrame): Bowling statistics DataFrame
            innings (int): Innings number
            team_players (dict): Mapping of player names to player IDs
            
        Returns:
            bool: True if successful, False otherwise
        """
        if not self.db_manager:
            print("Database manager not initialized. Provide db_path in constructor.")
            return False
            
        try:
            for _, row in bowling_df.iterrows():
                # Extract player name from BOWLING column
                bowling_info = row.get('BOWLING', '')
                player_name = bowling_info.split(' ')[0] if bowling_info else ''
                
                # Try to get player ID from mapping or use name as fallback
                player_id = team_players.get(player_name, player_name) if team_players else player_name
                
                # Parse bowling figures (assuming format like "10-2-45-3")
                bowling_parts = bowling_info.split('-') if '-' in bowling_info else []
                
                stats_data = {
                    'player_id': player_id,
                    'match_id': self.match_id,
                    'series_id': self.series_id,
                    'innings': innings,
                    'overs': self._safe_float(bowling_parts[0]) if len(bowling_parts) > 0 else 0.0,
                    'maidens': self._safe_int(bowling_parts[1]) if len(bowling_parts) > 1 else 0,
                    'runs_conceded': self._safe_int(bowling_parts[2]) if len(bowling_parts) > 2 else 0,
                    'wickets': self._safe_int(bowling_parts[3]) if len(bowling_parts) > 3 else 0,
                    'economy_rate': self._safe_float(row.get('ECON', 0.0))
                }
                
                self.db_manager.store_bowling_stats(stats_data)
            
            return True
        except Exception as e:
            print(f"Error saving bowling stats to database: {e}")
            return False
    
    def get_match_scorecard_from_db(self):
        """
        Get match scorecard from database.
        
        Returns:
            dict: Batting and bowling scorecards
        """
        if not self.db_manager or not hasattr(self, 'match_id'):
            print("Database manager not initialized or match ID not set.")
            return {}
            
        return {
            'batting': self.db_manager.get_match_batting_scorecard(self.match_id),
            'bowling': self.db_manager.get_match_bowling_figures(self.match_id)
        }
    
    def _safe_int(self, value, default=0):
        """Safely convert value to int."""
        try:
            return int(str(value).replace('*', '').strip()) if value else default
        except (ValueError, TypeError):
            return default
    
    def _safe_float(self, value, default=0.0):
        """Safely convert value to float."""
        try:
            return float(str(value).strip()) if value else default
        except (ValueError, TypeError):
            return default


# depending on IDE, might need to print or not
# print(Series(1327237, 1327270).get_results_by_year(2020, 1))
