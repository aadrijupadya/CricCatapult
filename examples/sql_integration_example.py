#!/usr/bin/env python3
"""
Example script demonstrating CricCatapult SQL integration.

This script shows how to:
1. Initialize classes with database support
2. Scrape data and save to database  
3. Retrieve data from database
4. Query and analyze stored data
"""

import sys
import os

# Add parent directory to path to import CricCatapult
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from CricCatapult import Player, Series, Records, SQLManager

def main():
    print("CricCatapult SQL Integration Example")
    print("=" * 40)
    
    # Initialize database path
    db_path = "cricket_example.db"
    
    # Example 1: Working with Players and Database
    print("\n1. Player Data with Database Integration")
    print("-" * 40)
    
    try:
        # Initialize player with database support
        player = Player("Virat Kohli", db_path=db_path)
        print(f"Player ID: {player.player_id}")
        
        # Save player data to database
        if player.save_to_database():
            print("✓ Player data saved to database")
        
        # Retrieve player data from database
        db_player_data = player.get_from_database()
        if db_player_data:
            print(f"✓ Retrieved player: {db_player_data.get('name', 'N/A')}")
    
    except Exception as e:
        print(f"✗ Error with player example: {e}")
    
    # Example 2: Working with Series/Matches
    print("\n2. Match Data with Database Integration")
    print("-" * 40)
    
    try:
        # Initialize series with database support
        # Note: You'll need actual series_id and match_id for this to work
        series_id = "1327237"  # Example series ID
        match_id = "1327270"   # Example match ID
        
        series = Series(series_id=series_id, match_id=match_id, db_path=db_path)
        
        # Save match data (you can provide custom match data)
        match_data = {
            'series_id': series_id,
            'date': '2023-10-15',
            'format': 'ODI',
            'team1': 'India',
            'team2': 'Australia',
            'result': 'India won by 6 wickets',
            'venue': 'Wankhede Stadium, Mumbai'
        }
        
        if series.save_match_to_database(match_data):
            print("✓ Match data saved to database")
        
    except Exception as e:
        print(f"✗ Error with series example: {e}")
    
    # Example 3: Working with Records
    print("\n3. Records with Database Integration")
    print("-" * 40)
    
    try:
        # Initialize records with database support
        records = Records(db_path=db_path)
        
        # You could save scraped records to database
        print("✓ Records manager initialized with database support")
        
    except Exception as e:
        print(f"✗ Error with records example: {e}")
    
    # Example 4: Direct Database Operations
    print("\n4. Direct Database Operations")
    print("-" * 40)
    
    try:
        # Initialize SQL manager directly
        with SQLManager(db_path) as sql_manager:
            
            # Get database statistics
            stats = sql_manager.get_database_stats()
            print("Database Statistics:")
            for table, count in stats.items():
                print(f"  {table}: {count} records")
            
            # Search for players
            search_results = sql_manager.search_players("Kohli")
            if not search_results.empty:
                print(f"\n✓ Found {len(search_results)} players matching 'Kohli'")
                print(search_results[['name', 'batting_style', 'playing_role']].to_string(index=False))
            
            # Execute custom query
            custom_query = "SELECT COUNT(*) as total_players FROM players"
            result = sql_manager.execute_query(custom_query)
            if not result.empty:
                print(f"\n✓ Total players in database: {result.iloc[0]['total_players']}")
        
    except Exception as e:
        print(f"✗ Error with direct database operations: {e}")
    
    # Example 5: Data Export
    print("\n5. Data Export")
    print("-" * 40)
    
    try:
        with SQLManager(db_path) as sql_manager:
            # Export players data to CSV
            if sql_manager.export_to_csv('players', 'exported_players.csv'):
                print("✓ Players data exported to 'exported_players.csv'")
        
    except Exception as e:
        print(f"✗ Error with data export: {e}")
    
    print("\n" + "=" * 40)
    print("Example completed!")
    print(f"Database file: {db_path}")
    print("You can examine the database using any SQLite browser.")

if __name__ == "__main__":
    main()
