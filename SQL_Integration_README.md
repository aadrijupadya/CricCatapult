# CricCatapult SQL Integration

This document describes the new SQL integration features added to CricCatapult, allowing you to store and retrieve cricket data using a local SQLite database.

## Overview

The SQL integration provides:
- Local SQLite database storage for cricket data
- Caching of frequently accessed data
- Historical data analysis capabilities
- Data export functionality
- Reduced dependency on web scraping for repeated queries

## New Classes and Features

### SQLManager Class

The `SQLManager` class is the core of the SQL integration, providing:

```python
from CricCatapult import SQLManager

# Initialize with database path
sql_manager = SQLManager("my_cricket_data.db")

# Get database statistics
stats = sql_manager.get_database_stats()

# Search players
players = sql_manager.search_players("Kohli")

# Execute custom queries
results = sql_manager.execute_query("SELECT * FROM players LIMIT 5")

# Export data to CSV
sql_manager.export_to_csv('players', 'players_export.csv')
```

### Database Schema

The integration creates the following tables:

#### Players Table
- `player_id` (TEXT PRIMARY KEY): Unique player identifier
- `name` (TEXT): Player name
- `full_name` (TEXT): Full player name
- `birth_info` (TEXT): Birth information
- `age` (TEXT): Player age
- `batting_style` (TEXT): Batting style
- `bowling_style` (TEXT): Bowling style
- `playing_role` (TEXT): Playing role
- `teams` (TEXT): Teams played for
- `description` (TEXT): Player description
- `created_at`, `updated_at` (TIMESTAMP): Timestamps

#### Matches Table
- `match_id` (TEXT PRIMARY KEY): Unique match identifier
- `series_id` (TEXT): Associated series ID
- `date` (TEXT): Match date
- `format` (TEXT): Match format (Test, ODI, T20)
- `team1`, `team2` (TEXT): Team names
- `result` (TEXT): Match result
- `venue` (TEXT): Match venue

#### Batting Stats Table
- `player_id`, `match_id`, `series_id` (TEXT): Foreign keys
- `innings` (INTEGER): Innings number
- `runs`, `balls_faced`, `fours`, `sixes` (INTEGER): Batting statistics
- `strike_rate` (REAL): Strike rate
- `dismissal` (TEXT): How the player was dismissed

#### Bowling Stats Table
- `player_id`, `match_id`, `series_id` (TEXT): Foreign keys
- `innings` (INTEGER): Innings number
- `overs` (REAL): Overs bowled
- `maidens`, `runs_conceded`, `wickets` (INTEGER): Bowling statistics
- `economy_rate` (REAL): Economy rate

#### Records Table
- `record_type` (TEXT): Type of record
- `record_category` (TEXT): Record category
- `value` (TEXT): Record value
- Associated player, match, series, team, and format information

#### Series Table
- `series_id` (TEXT PRIMARY KEY): Unique series identifier
- `name`, `location` (TEXT): Series details
- `year` (INTEGER): Series year
- `format` (TEXT): Series format

## Updated Class Features

### Player Class

```python
from CricCatapult import Player

# Initialize player with database support
player = Player("Virat Kohli", db_path="cricket_data.db")

# Save player data to database
success = player.save_to_database()

# Retrieve player data from database
player_data = player.get_from_database()

# Get career statistics from database
batting_stats = player.get_career_stats_from_db('batting')
bowling_stats = player.get_career_stats_from_db('bowling')
```

### Series Class

```python
from CricCatapult import Series

# Initialize series with database support
series = Series(series_id="123", match_id="456", db_path="cricket_data.db")

# Save match data to database
match_data = {
    'date': '2023-10-15',
    'format': 'ODI',
    'team1': 'India',
    'team2': 'Australia',
    'result': 'India won by 6 wickets',
    'venue': 'Wankhede Stadium'
}
series.save_match_to_database(match_data)

# Save batting and bowling statistics
batting_df = series.batting_df(bat_first=True)
series.save_batting_stats_to_database(batting_df, innings=1)

bowling_df = series.bowling_df(bowl_first=False)
series.save_bowling_stats_to_database(bowling_df, innings=1)

# Get scorecard from database
scorecard = series.get_match_scorecard_from_db()
```

### Records Class

```python
from CricCatapult import Records

# Initialize records with database support
records = Records(db_path="cricket_data.db")

# Save scraped records to database
records_df = records.get_general_records("123")
records.save_records_to_database(
    records_df, 
    record_type="most_runs", 
    record_category="career",
    format_type="Test"
)

# Search records in database
search_results = records.search_records("highest score")
```

## Usage Examples

### Basic Usage

```python
from CricCatapult import Player, SQLManager

# Create a player with database support
player = Player("MS Dhoni", db_path="cricket.db")

# Save player information
if player.save_to_database():
    print("Player data saved successfully")

# Later, retrieve the data
stored_data = player.get_from_database()
print(f"Stored player: {stored_data['name']}")
```

### Advanced Database Operations

```python
from CricCatapult import SQLManager

with SQLManager("cricket.db") as db:
    # Get all players from a specific team
    indian_players = db.execute_query("""
        SELECT * FROM players 
        WHERE teams LIKE '%India%'
    """)
    
    # Get match statistics
    match_stats = db.execute_query("""
        SELECT m.team1, m.team2, m.result, 
               AVG(bs.runs) as avg_runs
        FROM matches m
        JOIN batting_stats bs ON m.match_id = bs.match_id
        GROUP BY m.match_id
    """)
    
    # Export specific data
    db.export_to_csv('players', 'all_players.csv')
```

### Data Analysis Example

```python
import pandas as pd
from CricCatapult import SQLManager

with SQLManager("cricket.db") as db:
    # Analyze batting performance
    batting_analysis = db.execute_query("""
        SELECT p.name, 
               AVG(bs.runs) as avg_runs,
               AVG(bs.strike_rate) as avg_strike_rate,
               COUNT(bs.id) as total_innings
        FROM players p
        JOIN batting_stats bs ON p.player_id = bs.player_id
        GROUP BY p.player_id
        HAVING total_innings >= 5
        ORDER BY avg_runs DESC
    """)
    
    print("Top Batsmen by Average:")
    print(batting_analysis.head())
```

## Benefits

1. **Reduced Web Scraping**: Store data locally to avoid repeated API calls
2. **Faster Queries**: Database queries are much faster than web scraping
3. **Historical Analysis**: Build comprehensive datasets over time
4. **Data Export**: Export data for use in other tools
5. **Custom Analysis**: Execute custom SQL queries for detailed analysis
6. **Caching**: Automatic caching of frequently accessed data

## Installation Requirements

The SQL integration uses Python's built-in `sqlite3` library, so no additional installations are required. However, for the best experience:

```bash
# Optional: Install pandas for better DataFrame support (already in requirements)
pip install pandas

# Optional: Install a SQLite browser for examining the database
# DB Browser for SQLite: https://sqlitebrowser.org/
```

## File Structure

```
CricCatapult/
├── CricCatapult/
│   ├── SQLManager.py          # New SQL integration class
│   ├── Player.py              # Updated with database methods
│   ├── Series.py              # Updated with database methods  
│   ├── Records.py             # Updated with database methods
│   └── __init__.py            # Updated imports
├── examples/
│   └── sql_integration_example.py  # Usage examples
├── SQL_Integration_README.md  # This file
└── cricket_data.db           # Database file (created automatically)
```

## Best Practices

1. **Database Path**: Use a consistent database path across your application
2. **Context Managers**: Use `with SQLManager(db_path) as db:` for automatic connection cleanup
3. **Error Handling**: Always wrap database operations in try-catch blocks
4. **Data Validation**: Validate data before storing in database
5. **Regular Backups**: Backup your database file regularly
6. **Query Optimization**: Use appropriate indexes for frequently queried columns

## Troubleshooting

### Common Issues

1. **Import Error**: Make sure you're importing from the updated CricCatapult package
2. **Database Locked**: Close other connections to the database file
3. **Permission Error**: Ensure write permissions for the database directory
4. **Data Not Saving**: Check for exceptions and validate data format

### Debugging

```python
from CricCatapult import SQLManager

# Check database statistics
with SQLManager("cricket.db") as db:
    stats = db.get_database_stats()
    print("Database contents:", stats)
    
    # Test connection
    result = db.execute_query("SELECT sqlite_version()")
    print("SQLite version:", result.iloc[0, 0])
```

## Future Enhancements

Potential future improvements:
- Support for other databases (PostgreSQL, MySQL)
- Data synchronization features
- Advanced analytics dashboard
- Real-time data updates
- Data visualization integration

## Contributing

When contributing to the SQL integration:
1. Maintain backward compatibility
2. Add comprehensive error handling
3. Include unit tests
4. Update documentation
5. Follow existing code style

## Example Output

When you run the example script, you should see output like:

```
CricCatapult SQL Integration Example
========================================

1. Player Data with Database Integration
----------------------------------------
Player ID: 253802
✓ Player data saved to database
✓ Retrieved player: Virat Kohli

2. Match Data with Database Integration
----------------------------------------
✓ Match data saved to database

Database Statistics:
  players: 1 records
  matches: 1 records
  series: 0 records
  batting_stats: 0 records
  bowling_stats: 0 records
  records: 0 records

✓ Found 1 players matching 'Kohli'
        name batting_style playing_role
  Virat Kohli   Right-hand      Batsman

✓ Total players in database: 1
✓ Players data exported to 'exported_players.csv'

========================================
Example completed!
Database file: cricket_example.db
```

This SQL integration makes CricCatapult much more powerful for data analysis and reduces the need for constant web scraping while providing a robust local data storage solution.
