.. CricCatapult documentation master file, created by
   sphinx-quickstart on Sun Sep  4 14:45:50 2022.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to CricCatapult's documentation!
========================================

.. toctree::
   :maxdepth: 2
   :caption: Contents:



Indices and tables
==================

* :ref:`installation`
* :ref:`classes`
* :ref:`search`

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
