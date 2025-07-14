.. CricCatapult documentation master file, created by
   sphinx-quickstart on Sun Sep  4 14:45:50 2022.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to CricCatapult's documentation!
========================================

**CricCatapult** is a comprehensive Python library for cricket data analysis, statistics, and visualization. Access live cricket scores, historical match data, player statistics, and detailed cricket records from international and domestic leagues worldwide.

**Key Features:**

* **Live Scores & Real-time Data**: Get live cricket scores and match updates from around the world
* **Comprehensive Match Data**: Download cricket match data in JSON, YAML, and CSV formats from all major leagues (IPL, BBL, PSL, CPL, and more)
* **Player Analytics**: Detailed player statistics, career records, batting/bowling analysis, and performance metrics across all formats (Test, ODI, T20)
* **Series & Tournament Analysis**: Match scorecards, team statistics, head-to-head records, and tournament standings
* **Advanced Visualizations**: Generate Manhattan plots, Worm graphs, pitch maps, and interactive venue maps
* **Historical Records**: Access cricket records by team, tournament, year, ground, and player performance
* **Location Intelligence**: Cricket ground information with interactive mapping and venue analysis

**Supported Data Sources:**
Cricket data from Test matches, ODIs, T20s, IPL, Big Bash League, Pakistan Super League, Caribbean Premier League, Bangladesh Premier League, Afghanistan Premier League, Lanka Premier League, Women's cricket, and more.

**Perfect for:** Cricket analysts, data scientists, sports journalists, fantasy cricket players, researchers, and cricket enthusiasts who need comprehensive cricket data and analytics.

Installation
============

**Quick Install**

Install CricCatapult from PyPI using pip:

.. code-block:: bash

   pip install criccatapult

**Requirements:**

* Python 3.6+
* Works on Windows, macOS, and Linux

**Optional Dependencies**

For full Location class functionality (interactive maps), install geopandas:

.. code-block:: bash

   pip install geopandas

**Verify Installation**

.. code-block:: python

   from CricCatapult import Scoreboard, Player, Series, Records, Location
   
   # Get live cricket scores
   scores = Scoreboard()
   print(scores.scores())
   
   # Analyze a player
   player = Player("Virat Kohli")
   stats = player.get_summary_stats(format_num=2, view='match', action='batting')
   print(stats)

.. toctree::
   :maxdepth: 2
   :caption: Contents:

Scroll down to view documentation.

Available Documentation:
Scoreboard, Cricsheet, Player, Series, Records, Location

Scoreboard Class
==================
.. py:function:: scores()

   This function outputs a pandas series of all matches in action around the world. To check the live score of an individual match, simply use indexing to get the full description of the match.
   
.. py:function:: scores_df()

   Gets live scores in dataframe format.
  
Cricsheet Class
==================
.. py:function:: all_matches_json()

   Downloads matches from every league in JSON format. Each match will download as an individual file.

.. py:function:: all_matches_yaml()

   Downloads matches from every league in YAML format. Each match will download as an individual file.

.. py:function:: all_matches_csv(gender)

   Parameters:
      gender : "male" or "female" for matches only for that gender, or "all" for all matches in csv format.

.. py:function:: all_matches_csv2(gender)

   Parameters:
      gender : "male" or "female" for matches only for that gender, or "all" for all matches in a different csv format.

.. py:function:: test_matches_csv(gender)

   Parameters:
      gender : "male" or "female" for test matches only for that gender, or "all" for all test matches in csv format.
      
.. py:function:: test_matches_csv2(gender)

   Parameters:
      gender : "male" or "female" for test matches only for that gender, or "all" for all test matches in a different csv format.

.. py:function:: odi_csv(gender)

   Parameters:
      gender : "male" or "female" for odi matches only for that gender, or "all" for all odi matches in csv format.

.. py:function:: odi_csv2(gender)

   Parameters:
      gender : "male" or "female" for odi matches only for that gender, or "all" for all odi matches in a different csv format.
      
.. py:function:: t20_csv(gender)

   Parameters:
      gender : "male" or "female" for T20 matches only for that gender, or "all" for all T20 matches in csv format.

.. py:function:: t20_csv2(gender)

   Parameters:
      gender : "male" or "female" for T20 matches only for that gender, or "all" for all T20 matches in a different csv format.

Domestic League Data
==================

.. py:function:: afghanleague_csv()

   Downloads all matches from the Afghanistan Premier League in csv format.

.. py:function:: afghanleague_csv2()

   Downloads all matches from the Afghanistan Premier League in a different csv format.
   
.. py:function:: bigbashleague_csv()

   Downloads all matches from the Big Bash League in csv format.

.. py:function:: bigbashleague_csv2()

   Downloads all matches from the Big Bash League in a different csv format.

.. py:function:: bangladeshleague_csv()

   Downloads all matches from the Bangladesh Premier League in csv format.
   
.. py:function:: caribbeanleague_csv()

   Downloads all matches from the Caribbean Premier League in csv format.
   
.. py:function:: caribbeanleague_csv2()

   Downloads all matches from the Caribbean Premier League in a different csv format.
   
.. py:function:: IPL_csv()

   Downloads all matches from the Indian Premier League in csv format.

.. py:function:: IPL_csv2()

   Downloads all matches from the Indian Premier League in a different csv format.
   
.. py:function:: lankaleague_csv()

   Downloads all matches from the Lanka Premier League in csv format.
   
.. py:function:: lankaleague_csv2()

   Downloads all matches from the Lanka Premier League in a different csv format.
   
.. py:function:: pakistanleague_csv()

   Downloads all matches from the Pakistan Super League in csv format.

.. py:function:: pakistanleague_csv2()

   Downloads all matches from the Pakistan Super League in a different csv format.
   
.. py:function:: womensbigbashleague_csv()

   Downloads all matches from the Womens Big Bash League in csv format.

.. py:function:: womensbigbashleague_csv2()

   Downloads all matches from the Womens Big Bash League in a different csv format.
   
.. py:function:: womenst20_csv()

   Downloads all women's T20 matches in csv format.

.. py:function:: womenst20_csv2()

   Downloads all women's T20 matches in a different csv format.
   
Recent Match Data
==================
.. py:function:: recent_csv(gender, days)

   Parameters:
      gender : "male" or "men" for recent mens cricket matches.
               "women" or "female" for recent womens cricket matches.
               "all" or "both" for recent matches from both genders.
               
      days : 2 for csv files from the past 2 days.
             7 for csv files from the past 7 days.
             30 for csv files from the past 30 days.

Player Class
==================
.. py:function:: __init__(self, player_name)

   The object is initalized using a player name, passed in as a string.
   
.. py:function:: get_format_df(self, format_num, view, action)

   This function returns numerous individual player data (through a dataframe) that covers all formats, all actions (batting, bowling, fielding), and a variety of views (partnership by partnership, dismissal by dismissal, ground by ground, etc.)
   
   Parameters: 
      format_num : integer that specifies the match format from which you want data from. 
         1: test data
         2: ODI data
         3: T-20 data
         
      view : specifies the view of the data (match-by-match, inning-by-inning, partnership, etc.)
      
         'innings' : returns inning-by-inning data
         
         'match' : returns match-by-match data
         
         'cumulative' : returns cumulative data (running total of runs/wickets/etc.)
         
         'series' : returns series-by-series data
         
         'tour' : returns data from tours only (any time player's team travels to another nation to play a series)
         
         'ground' : returns ground-by-ground data
         
         (BATTING SUBSET ONLY) 'fow_summary' : returns batsman partnership data 
         
         (BATTING SUBSET ONLY) 'fow_list' : returns list of batting partnerships and corresponding data
         
         (BATTING/FIELDING SUBSET ONLY) 'dismissal_history' : returns list of dismissal history
         
         (BATTING/FIELDING SUBSET ONLY) 'bowler_summary' : returns list of bowler statistics against a particular batter
         
         (BATTING SUBSET ONLY) 'fielder_summary' : returns list of dismissal by fielder

         (BOWLING SUBSET ONLY) 'wickets_summary' : returns summary of types of deliveries on wicket balls, 
         
         (BOWLING/FIELDING SUBSET ONLY) 'batter_dismissed' : returns list of batters dismissed by bowler
         
         (BOWLING SUBSET ONLY) 'fielder_summary' : returns list of fielders that have contributed to dismissal by bowler (through catch or stumping)
         
         (BOWLING/FIELDING SUBSET ONLY) 'dismissal_list' : returns details for each dismissal by bowler
         
         (ALL ROUNDER SUBSET ONLY) 'awards_series' : returns any series awards a player one (if applicable)
         
         (ALL ROUNDER SUBSET ONLY) 'results' : returns match by match results in every game a player was invovled in
         
         (ALL ROUNDER SUBSET ONLY) 'awards_match' : returns any match awards a player one (if applicable)
         
      action : specifies analysis type with respect to action (batting, bowling, fielding)
      
         'batting' : returns batting statistics
         
         'bowling' : returns bowling statistics
         
         'fielding' : returns fielding statistics (catches, stumps, etc.)
         
         'allround' : returns all-rounder statistics
         
.. py:function:: get_summary_stats(self, format_num, view, action)

   This function returns a player's summary statistics for a specific format and action, in a dataframe. 
   
   Parameters: 
         format_num : integer that specifies the match format from which you want data from. 
            1: test data
            2: ODI data
            3: T-20 data
            
         view : specifies the view of the data (match-by-match, inning-by-inning, partnership, etc.)
            
         action : 
           
            'batting' : returns batting statistics

            'bowling' : returns bowling statistics

            'fielding' : returns fielding statistics (catches, stumps, etc.)

            'allround' : returns all-rounder statistics
            
.. py:function:: get_overall_df(self, type_num, view, action)

   This function returns a player's overall statistics across all formats for a specific action, in a dataframe. 
   
   Parameters: 
         type_num : integer that specifies which table to return from the overall statistics page
            
         view : specifies the view of the data
         
            'innings' : returns inning-by-inning data
            
            'match' : returns match-by-match data
            
            'cumulative' : returns cumulative data
            
            'series' : returns series-by-series data
            
            'ground' : returns ground-by-ground data
            
         action : 
           
            'batting' : returns batting statistics

            'bowling' : returns bowling statistics

            'fielding' : returns fielding statistics (catches, stumps, etc.)

            'allround' : returns all-rounder statistics

.. py:function:: get_career_df(self)

   This function returns a player's career overview statistics in a dataframe format.

.. py:function:: get_personal_info(self, arg)

   This function returns useful player personal info such as name, birth info, and style of play.
   
   Parameters:
   
      arg : string that specifies type of personal info
         'full_name' : returns Full name of player
         'birth_info' : returns information related to Birth of player such as birthplace, birthdate, etc.
         'age' : returns player age
         'batting_style' : returns right/left handedness with bat
         'bowling_style' : returns right/left handedness with ball
         'playing_role' : returns player position

.. py:function:: get_teams(self)

   This function returns a list of teams the player has represented.

.. py:function:: get_description(self)

   This function returns a text description/biography of the player.

.. py:function:: get_overview_df(self, pos)

   This function returns overview statistics for the player from their profile page.
   
   Parameters:
      pos : integer position of the table to return from the player's profile page

Series Class
==================
.. py:function:: __init__(self, series_id=None, match_id=None)

   The object is initialized using a series ID and match ID, both passed in as integers.
   
   Parameters:
      series_id : unique identifier for the cricket series
      match_id : unique identifier for the specific match within the series

.. py:function:: batting_df(self, bat_first)

   Returns batting scorecard data for limited overs matches (ODI/T20).
   
   Parameters:
      bat_first : boolean indicating if the team batting first is desired (True) or second (False)

.. py:function:: bowling_df(self, bowl_first)

   Returns bowling figures data for limited overs matches (ODI/T20).
   
   Parameters:
      bowl_first : boolean indicating if the team bowling first is desired (True) or second (False)

.. py:function:: test_bat(self, bat_first, inning)

   Returns batting scorecard data for Test matches by inning.
   
   Parameters:
      bat_first : boolean indicating if the team batting first is desired
      inning : integer (1 or 2) indicating which inning

.. py:function:: test_bowl(self, bowl_first, inning)

   Returns bowling figures data for Test matches by inning.
   
   Parameters:
      bowl_first : boolean indicating if the team bowling first is desired
      inning : integer (1 or 2) indicating which inning

.. py:function:: get_general_df_test(self)

   Returns general match information and statistics for Test matches.

.. py:function:: get_general_df(self)

   Returns general match information and statistics for limited overs matches.

.. py:function:: get_standings(self)

   Returns current tournament/series standings in dataframe format.

.. py:function:: test_df(self)

   Returns Test match specific data in dataframe format.

.. py:function:: current_series(self)

   Returns information about currently ongoing cricket series worldwide.

.. py:function:: get_series_by_year(self, year)

   Returns cricket series that took place in a specific year.
   
   Parameters:
      year : integer year for which to retrieve series information

.. py:function:: get_results_by_year(self, year, format)

   Returns match results for a specific year and format.
   
   Parameters:
      year : integer year for results
      format : integer format code (1=Test, 2=ODI, 3=T20)

.. py:function:: get_series_results(self, number)

   Returns series results based on a specific record number.
   
   Parameters:
      number : integer record identifier

.. py:function:: get_bowler_analysis(self)

   Returns detailed bowling analysis and statistics for the match.

.. py:function:: manhattan(self)

   Generates a Manhattan plot visualization showing runs scored per over by both teams, including wicket markers.

.. py:function:: worm(self)

   Generates a Worm plot visualization showing cumulative runs scored by both teams over the course of the match.

.. py:function:: mvp(self)

   Returns the Most Valuable Player (MVP) statistics for the match in dataframe format.

.. py:function:: pitchmap(self, list1, list2, speeds)

   Generates a pitch map visualization showing ball locations and speeds.
   
   Parameters:
      list1 : list of x-coordinates for ball positions
      list2 : list of y-coordinates for ball positions
      speeds : list of ball speeds corresponding to each position

Records Class
==================
.. py:function:: __init__(self)

   Initializes the Records object for accessing cricket records and statistics.

.. py:function:: get_records_by_team(self, team_id, record, type, format)

   Returns cricket records filtered by team.
   
   Parameters:
      team_id : unique identifier for the team
      record : type of record (e.g., 'most_runs_career', 'most_wickets_career')
      type : category of record ('batting', 'bowling', 'fielding')
      format : match format (1=Test, 2=ODI, 3=T20)

.. py:function:: get_records_by_tournament(self, type, record, tourney_id)

   Returns cricket records filtered by tournament.
   
   Parameters:
      type : category of record ('batting', 'bowling', 'fielding')
      record : type of record to retrieve
      tourney_id : unique identifier for the tournament

.. py:function:: get_records_h2h(self, team_id1, team_id2, record, type)

   Returns head-to-head records between two teams.
   
   Parameters:
      team_id1 : unique identifier for first team
      team_id2 : unique identifier for second team
      record : type of record to retrieve
      type : category of record ('batting', 'bowling', 'fielding')

.. py:function:: get_records_year(self, year, record, type)

   Returns cricket records for a specific year.
   
   Parameters:
      year : integer year for records
      record : type of record to retrieve
      type : category of record ('batting', 'bowling', 'fielding')

.. py:function:: get_records_ground(self, type, record, ground_id)

   Returns cricket records for a specific ground/venue.
   
   Parameters:
      type : category of record ('batting', 'bowling', 'fielding')
      record : type of record to retrieve
      ground_id : unique identifier for the ground

.. py:function:: get_general_records(self, record_id)

   Returns general cricket records based on record ID.
   
   Parameters:
      record_id : unique identifier for the specific record type

.. py:function:: get_ipl_records(self, format, record)

   Returns Indian Premier League (IPL) specific records.
   
   Parameters:
      format : match format for IPL records
      record : type of record to retrieve

.. py:function:: get_bbl_records(self, format, record)

   Returns Big Bash League (BBL) specific records.
   
   Parameters:
      format : match format for BBL records
      record : type of record to retrieve

.. py:function:: get_et20_records(self, format, record)

   Returns Euro T20 League specific records.
   
   Parameters:
      format : match format for Euro T20 records
      record : type of record to retrieve

.. py:function:: get_psl_records(self, format, record)

   Returns Pakistan Super League (PSL) specific records.
   
   Parameters:
      format : match format for PSL records
      record : type of record to retrieve

Location Class
==================
.. py:function:: __init__(self, match_id)

   Initializes the Location object with a specific match ID to analyze venue information.
   
   Parameters:
      match_id : unique identifier for the cricket match

.. py:function:: get_location(self)

   Returns the cricket ground/venue name where the match is being played.

.. py:function:: get_map(self)

   Generates and returns an interactive map showing the location of the cricket ground using Folium mapping library.


Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`


      
