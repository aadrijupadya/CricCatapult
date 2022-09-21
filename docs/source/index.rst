.. CricCatapult documentation master file, created by
   sphinx-quickstart on Sun Sep  4 14:45:50 2022.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to CricCatapult's documentation!
========================================

.. toctree::
   :maxdepth: 2
   :caption: Contents:
   
Scroll down to view documentation.

Available Documentation:
Scoreboard and Cricsheet

In Progress Documentation:
Series, Player, Records, Location


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

   This function returns numerous individual player data (through a dataframe) that covers all formats, all actions (batting, bowling, fielding), and a   variety of views   (partnership by partnership, dismissal by dismissal, ground by ground, etc.)
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
         
.. py:function:: get_summary_stats(self, format_num, action)

   This function returns a player's summary statistics for a specific format and action, in a dataframe. 
   
   Parameters: 
         format_num : integer that specifies the match format from which you want data from. 
            1: test data
            2: ODI data
            3: T-20 data
            
           action : 
           
            'batting' : returns batting statistics

            'bowling' : returns bowling statistics

            'fielding' : returns fielding statistics (catches, stumps, etc.)

            'allround' : returns all-rounder statistics
            
.. py:function:: get_overall_df(self, type_num, view, action)

   This function returns a player's summary statistics for a specific format and action, in a dataframe. 
   
   Parameters: 
         format_num : integer that specifies the match format from which you want data from. 
            1: test data
            2: ODI data
            3: T-20 data
            
           action : 
           
            'batting' : returns batting statistics

            'bowling' : returns bowling statistics

            'fielding' : returns fielding statistics (catches, stumps, etc.)

            'allround' : returns all-rounder statistics
           view :
           

.. py:function:: get_career_df(self, type_num, view, action)


.. py:function:: get_personal_info(self, arg):
   This function returns useful player personal info such as name, birth info, and style of play.
   Parameters
   
      - arg : string that specifies type of personal info
         - full_name : returns Full name of player
         - birth_info : returns information related to Birth of player such as birthplace, birthdate, etc.
         - age : returns player age
         - batting_style : returns right/left handedness with bat
         - bowling_style : returns right/left handedness with ball
         - playing_role : returns player position
        
      

         


      
