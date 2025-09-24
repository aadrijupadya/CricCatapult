import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import requests
from bs4 import BeautifulSoup
from .SQLManager import SQLManager


class Records(object):
    def __init__(self, db_path=None):
        self.db_manager = SQLManager(db_path) if db_path else None

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
    
    def save_records_to_database(self, df, record_type, record_category="", format_type="", team=""):
        """
        Save records data to database.
        
        Args:
            df (pd.DataFrame): Records data
            record_type (str): Type of record (e.g., 'most_runs', 'best_bowling')
            record_category (str): Category of record (e.g., 'career', 'innings')
            format_type (str): Cricket format (e.g., 'Test', 'ODI', 'T20')
            team (str): Team name if applicable
            
        Returns:
            bool: True if successful, False otherwise
        """
        if not self.db_manager:
            print("Database manager not initialized. Provide db_path in constructor.")
            return False
            
        try:
            for _, row in df.iterrows():
                record_data = {
                    'record_type': record_type,
                    'record_category': record_category,
                    'value': str(row.iloc[1]) if len(row) > 1 else '',  # Assuming value is in second column
                    'player_id': '',  # Would need player name -> ID mapping
                    'match_id': '',
                    'series_id': '',
                    'team': team,
                    'format': format_type,
                    'date': ''
                }
                
                # Insert into database (using None for auto-increment ID)
                cursor = self.db_manager.conn.cursor()
                cursor.execute('''
                    INSERT INTO records 
                    (record_type, record_category, value, player_id, match_id, 
                     series_id, team, format, date)
                    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
                ''', (
                    record_data['record_type'],
                    record_data['record_category'],
                    record_data['value'],
                    record_data['player_id'],
                    record_data['match_id'],
                    record_data['series_id'],
                    record_data['team'],
                    record_data['format'],
                    record_data['date']
                ))
            
            self.db_manager.conn.commit()
            return True
        except Exception as e:
            print(f"Error saving records to database: {e}")
            return False
    
    def get_records_from_database(self, record_type, limit=10):
        """
        Get records from database by type.
        
        Args:
            record_type (str): Type of record to retrieve
            limit (int): Maximum number of records to return
            
        Returns:
            pd.DataFrame: Records data
        """
        if not self.db_manager:
            print("Database manager not initialized. Provide db_path in constructor.")
            return pd.DataFrame()
            
        return self.db_manager.get_records_by_type(record_type)
    
    def search_records(self, search_term, record_category=""):
        """
        Search records by value or category.
        
        Args:
            search_term (str): Term to search for
            record_category (str): Optional category filter
            
        Returns:
            pd.DataFrame: Matching records
        """
        if not self.db_manager:
            print("Database manager not initialized. Provide db_path in constructor.")
            return pd.DataFrame()
            
        try:
            query = '''
                SELECT * FROM records 
                WHERE value LIKE ? OR record_type LIKE ?
            '''
            params = [f'%{search_term}%', f'%{search_term}%']
            
            if record_category:
                query += ' AND record_category = ?'
                params.append(record_category)
                
            query += ' ORDER BY created_at DESC'
            
            return pd.read_sql_query(query, self.db_manager.conn, params=params)
        except Exception as e:
            print(f"Error searching records: {e}")
            return pd.DataFrame()


# print(Records().get_psl_records("batting", "most_runs_career"))
