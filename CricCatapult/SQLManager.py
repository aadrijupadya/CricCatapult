import sqlite3
import pandas as pd
import os
from datetime import datetime
from typing import Optional, Dict, Any, List


class SQLManager:
    """
    SQL integration for CricCatapult package.
    Manages cricket data storage and retrieval using SQLite database.
    """
    
    def __init__(self, db_path: str = "cricket_data.db"):
        """
        Initialize SQLManager with database path.
        
        Args:
            db_path (str): Path to SQLite database file
        """
        self.db_path = db_path
        self.conn = None
        self._init_database()
    
    def _init_database(self):
        """Initialize database connection and create tables if they don't exist."""
        self.conn = sqlite3.connect(self.db_path)
        self.conn.row_factory = sqlite3.Row  # Enable column access by name
        self._create_tables()
    
    def _create_tables(self):
        """Create all necessary tables for cricket data storage."""
        cursor = self.conn.cursor()
        
        # Players table
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS players (
                player_id TEXT PRIMARY KEY,
                name TEXT NOT NULL,
                full_name TEXT,
                birth_info TEXT,
                age TEXT,
                batting_style TEXT,
                bowling_style TEXT,
                playing_role TEXT,
                teams TEXT,
                description TEXT,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        ''')
        
        # Series table
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS series (
                series_id TEXT PRIMARY KEY,
                name TEXT,
                year INTEGER,
                format TEXT,
                location TEXT,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        ''')
        
        # Matches table
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS matches (
                match_id TEXT PRIMARY KEY,
                series_id TEXT,
                date TEXT,
                format TEXT,
                team1 TEXT,
                team2 TEXT,
                result TEXT,
                venue TEXT,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY (series_id) REFERENCES series (series_id)
            )
        ''')
        
        # Batting stats table
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS batting_stats (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                player_id TEXT,
                match_id TEXT,
                series_id TEXT,
                innings INTEGER,
                runs INTEGER,
                balls_faced INTEGER,
                fours INTEGER,
                sixes INTEGER,
                strike_rate REAL,
                dismissal TEXT,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY (player_id) REFERENCES players (player_id),
                FOREIGN KEY (match_id) REFERENCES matches (match_id),
                FOREIGN KEY (series_id) REFERENCES series (series_id)
            )
        ''')
        
        # Bowling stats table
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS bowling_stats (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                player_id TEXT,
                match_id TEXT,
                series_id TEXT,
                innings INTEGER,
                overs REAL,
                maidens INTEGER,
                runs_conceded INTEGER,
                wickets INTEGER,
                economy_rate REAL,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY (player_id) REFERENCES players (player_id),
                FOREIGN KEY (match_id) REFERENCES matches (match_id),
                FOREIGN KEY (series_id) REFERENCES series (series_id)
            )
        ''')
        
        # Records table
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS records (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                record_type TEXT NOT NULL,
                record_category TEXT,
                value TEXT NOT NULL,
                player_id TEXT,
                match_id TEXT,
                series_id TEXT,
                team TEXT,
                format TEXT,
                date TEXT,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY (player_id) REFERENCES players (player_id),
                FOREIGN KEY (match_id) REFERENCES matches (match_id),
                FOREIGN KEY (series_id) REFERENCES series (series_id)
            )
        ''')
        
        # Live scores cache table
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS live_scores (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                match_info TEXT,
                score_data TEXT,
                last_updated TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        ''')
        
        self.conn.commit()
    
    def store_player_data(self, player_id: str, player_data: Dict[str, Any]) -> bool:
        """
        Store player information in the database.
        
        Args:
            player_id (str): Unique player identifier
            player_data (dict): Dictionary containing player information
            
        Returns:
            bool: True if successful, False otherwise
        """
        try:
            cursor = self.conn.cursor()
            cursor.execute('''
                INSERT OR REPLACE INTO players 
                (player_id, name, full_name, birth_info, age, batting_style, 
                 bowling_style, playing_role, teams, description, updated_at)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, CURRENT_TIMESTAMP)
            ''', (
                player_id,
                player_data.get('name', ''),
                player_data.get('full_name', ''),
                player_data.get('birth_info', ''),
                player_data.get('age', ''),
                player_data.get('batting_style', ''),
                player_data.get('bowling_style', ''),
                player_data.get('playing_role', ''),
                str(player_data.get('teams', [])),
                str(player_data.get('description', []))
            ))
            self.conn.commit()
            return True
        except sqlite3.Error as e:
            print(f"Error storing player data: {e}")
            return False
    
    def store_match_data(self, match_id: str, match_data: Dict[str, Any]) -> bool:
        """
        Store match information in the database.
        
        Args:
            match_id (str): Unique match identifier
            match_data (dict): Dictionary containing match information
            
        Returns:
            bool: True if successful, False otherwise
        """
        try:
            cursor = self.conn.cursor()
            cursor.execute('''
                INSERT OR REPLACE INTO matches 
                (match_id, series_id, date, format, team1, team2, result, venue)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?)
            ''', (
                match_id,
                match_data.get('series_id', ''),
                match_data.get('date', ''),
                match_data.get('format', ''),
                match_data.get('team1', ''),
                match_data.get('team2', ''),
                match_data.get('result', ''),
                match_data.get('venue', '')
            ))
            self.conn.commit()
            return True
        except sqlite3.Error as e:
            print(f"Error storing match data: {e}")
            return False
    
    def store_batting_stats(self, stats_data: Dict[str, Any]) -> bool:
        """
        Store batting statistics in the database.
        
        Args:
            stats_data (dict): Dictionary containing batting stats
            
        Returns:
            bool: True if successful, False otherwise
        """
        try:
            cursor = self.conn.cursor()
            cursor.execute('''
                INSERT INTO batting_stats 
                (player_id, match_id, series_id, innings, runs, balls_faced, 
                 fours, sixes, strike_rate, dismissal)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            ''', (
                stats_data.get('player_id', ''),
                stats_data.get('match_id', ''),
                stats_data.get('series_id', ''),
                stats_data.get('innings', 0),
                stats_data.get('runs', 0),
                stats_data.get('balls_faced', 0),
                stats_data.get('fours', 0),
                stats_data.get('sixes', 0),
                stats_data.get('strike_rate', 0.0),
                stats_data.get('dismissal', '')
            ))
            self.conn.commit()
            return True
        except sqlite3.Error as e:
            print(f"Error storing batting stats: {e}")
            return False
    
    def store_bowling_stats(self, stats_data: Dict[str, Any]) -> bool:
        """
        Store bowling statistics in the database.
        
        Args:
            stats_data (dict): Dictionary containing bowling stats
            
        Returns:
            bool: True if successful, False otherwise
        """
        try:
            cursor = self.conn.cursor()
            cursor.execute('''
                INSERT INTO bowling_stats 
                (player_id, match_id, series_id, innings, overs, maidens, 
                 runs_conceded, wickets, economy_rate)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
            ''', (
                stats_data.get('player_id', ''),
                stats_data.get('match_id', ''),
                stats_data.get('series_id', ''),
                stats_data.get('innings', 0),
                stats_data.get('overs', 0.0),
                stats_data.get('maidens', 0),
                stats_data.get('runs_conceded', 0),
                stats_data.get('wickets', 0),
                stats_data.get('economy_rate', 0.0)
            ))
            self.conn.commit()
            return True
        except sqlite3.Error as e:
            print(f"Error storing bowling stats: {e}")
            return False
    
    def get_player_data(self, player_id: str) -> Optional[Dict[str, Any]]:
        """
        Retrieve player data from database.
        
        Args:
            player_id (str): Player identifier
            
        Returns:
            dict or None: Player data if found, None otherwise
        """
        try:
            cursor = self.conn.cursor()
            cursor.execute('SELECT * FROM players WHERE player_id = ?', (player_id,))
            row = cursor.fetchone()
            if row:
                return dict(row)
            return None
        except sqlite3.Error as e:
            print(f"Error retrieving player data: {e}")
            return None
    
    def get_match_data(self, match_id: str) -> Optional[Dict[str, Any]]:
        """
        Retrieve match data from database.
        
        Args:
            match_id (str): Match identifier
            
        Returns:
            dict or None: Match data if found, None otherwise
        """
        try:
            cursor = self.conn.cursor()
            cursor.execute('SELECT * FROM matches WHERE match_id = ?', (match_id,))
            row = cursor.fetchone()
            if row:
                return dict(row)
            return None
        except sqlite3.Error as e:
            print(f"Error retrieving match data: {e}")
            return None
    
    def get_player_stats(self, player_id: str, stat_type: str = 'batting') -> pd.DataFrame:
        """
        Retrieve player statistics as DataFrame.
        
        Args:
            player_id (str): Player identifier
            stat_type (str): Type of stats ('batting' or 'bowling')
            
        Returns:
            pd.DataFrame: Player statistics
        """
        try:
            if stat_type == 'batting':
                query = 'SELECT * FROM batting_stats WHERE player_id = ?'
            elif stat_type == 'bowling':
                query = 'SELECT * FROM bowling_stats WHERE player_id = ?'
            else:
                raise ValueError("stat_type must be 'batting' or 'bowling'")
            
            return pd.read_sql_query(query, self.conn, params=(player_id,))
        except Exception as e:
            print(f"Error retrieving player stats: {e}")
            return pd.DataFrame()
    
    def get_match_batting_scorecard(self, match_id: str) -> pd.DataFrame:
        """
        Get batting scorecard for a specific match.
        
        Args:
            match_id (str): Match identifier
            
        Returns:
            pd.DataFrame: Batting scorecard
        """
        try:
            query = '''
                SELECT p.name, bs.innings, bs.runs, bs.balls_faced, 
                       bs.fours, bs.sixes, bs.strike_rate, bs.dismissal
                FROM batting_stats bs
                JOIN players p ON bs.player_id = p.player_id
                WHERE bs.match_id = ?
                ORDER BY bs.innings, bs.id
            '''
            return pd.read_sql_query(query, self.conn, params=(match_id,))
        except Exception as e:
            print(f"Error retrieving batting scorecard: {e}")
            return pd.DataFrame()
    
    def get_match_bowling_figures(self, match_id: str) -> pd.DataFrame:
        """
        Get bowling figures for a specific match.
        
        Args:
            match_id (str): Match identifier
            
        Returns:
            pd.DataFrame: Bowling figures
        """
        try:
            query = '''
                SELECT p.name, bs.innings, bs.overs, bs.maidens, 
                       bs.runs_conceded, bs.wickets, bs.economy_rate
                FROM bowling_stats bs
                JOIN players p ON bs.player_id = p.player_id
                WHERE bs.match_id = ?
                ORDER BY bs.innings, bs.id
            '''
            return pd.read_sql_query(query, self.conn, params=(match_id,))
        except Exception as e:
            print(f"Error retrieving bowling figures: {e}")
            return pd.DataFrame()
    
    def search_players(self, name_pattern: str) -> pd.DataFrame:
        """
        Search for players by name pattern.
        
        Args:
            name_pattern (str): Name pattern to search for
            
        Returns:
            pd.DataFrame: Matching players
        """
        try:
            query = '''
                SELECT player_id, name, full_name, batting_style, 
                       bowling_style, playing_role
                FROM players 
                WHERE name LIKE ? OR full_name LIKE ?
            '''
            pattern = f'%{name_pattern}%'
            return pd.read_sql_query(query, self.conn, params=(pattern, pattern))
        except Exception as e:
            print(f"Error searching players: {e}")
            return pd.DataFrame()
    
    def get_records_by_type(self, record_type: str) -> pd.DataFrame:
        """
        Get records by type from database.
        
        Args:
            record_type (str): Type of record to retrieve
            
        Returns:
            pd.DataFrame: Records data
        """
        try:
            query = 'SELECT * FROM records WHERE record_type = ? ORDER BY value DESC'
            return pd.read_sql_query(query, self.conn, params=(record_type,))
        except Exception as e:
            print(f"Error retrieving records: {e}")
            return pd.DataFrame()
    
    def export_to_csv(self, table_name: str, output_path: str) -> bool:
        """
        Export table data to CSV file.
        
        Args:
            table_name (str): Name of table to export
            output_path (str): Path for output CSV file
            
        Returns:
            bool: True if successful, False otherwise
        """
        try:
            df = pd.read_sql_query(f'SELECT * FROM {table_name}', self.conn)
            df.to_csv(output_path, index=False)
            return True
        except Exception as e:
            print(f"Error exporting to CSV: {e}")
            return False
    
    def execute_query(self, query: str, params: tuple = ()) -> pd.DataFrame:
        """
        Execute custom SQL query and return results as DataFrame.
        
        Args:
            query (str): SQL query to execute
            params (tuple): Query parameters
            
        Returns:
            pd.DataFrame: Query results
        """
        try:
            return pd.read_sql_query(query, self.conn, params=params)
        except Exception as e:
            print(f"Error executing query: {e}")
            return pd.DataFrame()
    
    def get_database_stats(self) -> Dict[str, int]:
        """
        Get statistics about the database contents.
        
        Returns:
            dict: Database statistics
        """
        stats = {}
        tables = ['players', 'matches', 'series', 'batting_stats', 
                 'bowling_stats', 'records', 'live_scores']
        
        try:
            cursor = self.conn.cursor()
            for table in tables:
                cursor.execute(f'SELECT COUNT(*) FROM {table}')
                stats[table] = cursor.fetchone()[0]
        except sqlite3.Error as e:
            print(f"Error getting database stats: {e}")
            
        return stats
    
    def close(self):
        """Close database connection."""
        if self.conn:
            self.conn.close()
    
    def __enter__(self):
        """Context manager entry."""
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        """Context manager exit."""
        self.close()
