import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import requests
import zipfile
import io
from bs4 import BeautifulSoup

class Cricsheet(object):
    def __init__(self):
        self.url = "https://cricsheet.org/downloads/"
        self.page = requests.get(self.url)
        self.soup = BeautifulSoup(self.page.content, "html.parser")
    def all_matches_json(self):
        link = "https://cricsheet.org/downloads/all_json.zip"
        link = requests.get(link)
        zip = zipfile.ZipFile(io.BytesIO(link.content))
        zip.extractall()
    def all_matches_yaml(self):
        link = "https://cricsheet.org/downloads/all.zip"
        link = requests.get(link)
        zip = zipfile.ZipFile(io.BytesIO(link.content))
        zip.extractall()
    def all_matches_csv(self, gender):
        if gender == "male":
            link = "https://cricsheet.org/downloads/all_male_csv.zip"
            link = requests.get(link)
            zip = zipfile.ZipFile(io.BytesIO(link.content))
            zip.extractall()
        elif gender == "women":
            link = "https://cricsheet.org/downloads/all_female_csv.zip"
            link = requests.get(link)
            zip = zipfile.ZipFile(io.BytesIO(link.content))
            zip.extractall()
        else:
            link = "https://cricsheet.org/downloads/all_csv.zip"
            link = requests.get(link)
            zip = zipfile.ZipFile(io.BytesIO(link.content))
            zip.extractall()
    def all_matches_csv2(self, gender):
        if gender == "male":
            link = "https://cricsheet.org/downloads/all_male_csv2.zip"
            link = requests.get(link)
            zip = zipfile.ZipFile(io.BytesIO(link.content))
            zip.extractall()
        elif gender == "women":
            link = "https://cricsheet.org/downloads/all_female_csv2.zip"
            link = requests.get(link)
            zip = zipfile.ZipFile(io.BytesIO(link.content))
            zip.extractall()
        else:
            link = "https://cricsheet.org/downloads/all_csv2.zip"
            link = requests.get(link)
            zip = zipfile.ZipFile(io.BytesIO(link.content))
            zip.extractall()
    def test_matches_csv(self, gender):
        if gender == "male" or gender == "men":
            link = "https://cricsheet.org/downloads/tests_male_csv.zip"
            link = requests.get(link)
            zip = zipfile.ZipFile(io.BytesIO(link.content))
            zip.extractall()
        elif gender == "women" or gender == "female":
            link = "https://cricsheet.org/downloads/tests_female_csv.zip"
            link = requests.get(link)
            zip = zipfile.ZipFile(io.BytesIO(link.content))
            zip.extractall()
        else:
            link = "https://cricsheet.org/downloads/tests_csv.zip"
            link = requests.get(link)
            zip = zipfile.ZipFile(io.BytesIO(link.content))
            zip.extractall()
    def test_matches_csv2(self, gender):
        if gender == "male" or gender == "men":
            link = "https://cricsheet.org/downloads/tests_male_csv2.zip"
            link = requests.get(link)
            zip = zipfile.ZipFile(io.BytesIO(link.content))
            zip.extractall()
        elif gender == "women" or gender == "female":
            link = "https://cricsheet.org/downloads/tests_female_csv2.zip"
            link = requests.get(link)
            zip = zipfile.ZipFile(io.BytesIO(link.content))
            zip.extractall()
        else:
            link = "https://cricsheet.org/downloads/tests_csv2.zip"
            link = requests.get(link)
            zip = zipfile.ZipFile(io.BytesIO(link.content))
            zip.extractall()
    def odi_csv(self, gender):
        if gender == "male" or gender == "men":
            link = "https://cricsheet.org/downloads/odis_male_csv.zip"
            link = requests.get(link)
            zip = zipfile.ZipFile(io.BytesIO(link.content))
            zip.extractall()
        elif gender == "women" or gender == "female":
            link = "https://cricsheet.org/downloads/odis_female_csv.zip"
            link = requests.get(link)
            zip = zipfile.ZipFile(io.BytesIO(link.content))
            zip.extractall()
        else:
            link = "https://cricsheet.org/downloads/odis_csv.zip"
            link = requests.get(link)
            zip = zipfile.ZipFile(io.BytesIO(link.content))
            zip.extractall()
    def odi_csv2(self, gender):
        if gender == "male" or gender == "men":
            link = "https://cricsheet.org/downloads/odis_male_csv2.zip"
            link = requests.get(link)
            zip = zipfile.ZipFile(io.BytesIO(link.content))
            zip.extractall()
        elif gender == "women" or gender == "female":
            link = "https://cricsheet.org/downloads/odis_female_csv2.zip"
            link = requests.get(link)
            zip = zipfile.ZipFile(io.BytesIO(link.content))
            zip.extractall()
        else:
            link = "https://cricsheet.org/downloads/odis_csv2.zip"
            link = requests.get(link)
            zip = zipfile.ZipFile(io.BytesIO(link.content))
            zip.extractall()
    def t20_csv(self, gender):
        if gender == "male" or gender == "men":
            link = "https://cricsheet.org/downloads/t20s_male_csv.zip"
            link = requests.get(link)
            zip = zipfile.ZipFile(io.BytesIO(link.content))
            zip.extractall()
        elif gender == "women" or gender == "female":
            link = "https://cricsheet.org/downloads/t20s_female_csv.zip"
            link = requests.get(link)
            zip = zipfile.ZipFile(io.BytesIO(link.content))
            zip.extractall()
        else:
            link = "https://cricsheet.org/downloads/t20s_csv.zip"
            link = requests.get(link)
            zip = zipfile.ZipFile(io.BytesIO(link.content))
            zip.extractall()
    def t20_csv2(self, gender):
        if gender == "male" or gender == "men":
            link = "https://cricsheet.org/downloads/t20s_male_csv2.zip"
            link = requests.get(link)
            zip = zipfile.ZipFile(io.BytesIO(link.content))
            zip.extractall()
        elif gender == "women" or gender == "female":
            link = "https://cricsheet.org/downloads/t20s_female_csv2.zip"
            link = requests.get(link)
            zip = zipfile.ZipFile(io.BytesIO(link.content))
            zip.extractall()
        else:
            link = "https://cricsheet.org/downloads/t20s_csv2.zip"
            link = requests.get(link)
            zip = zipfile.ZipFile(io.BytesIO(link.content))
            zip.extractall()
    def afghanleague_csv(self):
        link = "https://cricsheet.org/downloads/apl_csv.zip"
        link = requests.get(link)
        zip = zipfile.ZipFile(io.BytesIO(link.content))
        zip.extractall()
    def afghanleague_csv2(self):
        link = "https://cricsheet.org/downloads/apl_csv2.zip"
        link = requests.get(link)
        zip = zipfile.ZipFile(io.BytesIO(link.content))
        zip.extractall()
    def bigbashleague_csv(self):
        link = "https://cricsheet.org/downloads/bbl_csv.zip"
        link = requests.get(link)
        zip = zipfile.ZipFile(io.BytesIO(link.content))
        zip.extractall()
    def bigbashleague_csv2(self):
        link = "https://cricsheet.org/downloads/bbl_csv2.zip"
        link = requests.get(link)
        zip = zipfile.ZipFile(io.BytesIO(link.content))
        zip.extractall()
    def bangladeshleague_csv(self):
        link = "https://cricsheet.org/downloads/bpl_csv.zip"
        link = requests.get(link)
        zip = zipfile.ZipFile(io.BytesIO(link.content))
        zip.extractall()
    def bangladeshleague_csv2(self):
        link = "https://cricsheet.org/downloads/bpl_csv2.zip"
        link = requests.get(link)
        zip = zipfile.ZipFile(io.BytesIO(link.content))
        zip.extractall()
    def caribbeanleague_csv(self):
        link = "https://cricsheet.org/downloads/cpl_csv.zip"
        link = requests.get(link)
        zip = zipfile.ZipFile(io.BytesIO(link.content))
        zip.extractall()
    def caribbeanleague_csv(self):
        link = "https://cricsheet.org/downloads/cpl_csv2.zip"
        link = requests.get(link)
        zip = zipfile.ZipFile(io.BytesIO(link.content))
        zip.extractall()
    def IPL_csv(self):
        link = "https://cricsheet.org/downloads/ipl_csv.zip"
        link = requests.get(link)
        zip = zipfile.ZipFile(io.BytesIO(link.content))
        zip.extractall()
    def IPL_csv2(self):
        link = "https://cricsheet.org/downloads/ipl_csv2.zip"
        link = requests.get(link)
        zip = zipfile.ZipFile(io.BytesIO(link.content))
        zip.extractall()
    def lankaleague_csv(self):
        link = "https://cricsheet.org/downloads/lpl_csv.zip"
        link = requests.get(link)
        zip = zipfile.ZipFile(io.BytesIO(link.content))
        zip.extractall()
    def lankaleague_csv2(self):
        link = "https://cricsheet.org/downloads/lpl_csv2.zip"
        link = requests.get(link)
        zip = zipfile.ZipFile(io.BytesIO(link.content))
        zip.extractall()
    def pakistanleague_csv(self):
        link = "https://cricsheet.org/downloads/psl_csv.zip"
        link = requests.get(link)
        zip = zipfile.ZipFile(io.BytesIO(link.content))
        zip.extractall()
    def pakistanleague_csv2(self):
        link = "https://cricsheet.org/downloads/psl_csv2.zip"
        link = requests.get(link)
        zip = zipfile.ZipFile(io.BytesIO(link.content))
        zip.extractall()
    def womensbigbashleague_csv(self):
        link = "https://cricsheet.org/downloads/wbb_csv.zip"
        link = requests.get(link)
        zip = zipfile.ZipFile(io.BytesIO(link.content))
        zip.extractall()
    def womensbigbashleague_csv2(self):
        link = "https://cricsheet.org/downloads/wbb_csv2.zip"
        link = requests.get(link)
        zip = zipfile.ZipFile(io.BytesIO(link.content))
        zip.extractall()
    def womenst20_csv(self):
        link = "https://cricsheet.org/downloads/wtc_csv.zip"
        link = requests.get(link)
        zip = zipfile.ZipFile(io.BytesIO(link.content))
        zip.extractall()
    def womenst20_csv2(self):
        link = "https://cricsheet.org/downloads/wtc_csv2.zip"
        link = requests.get(link)
        zip = zipfile.ZipFile(io.BytesIO(link.content))
        zip.extractall()
    def recent_csv(self, gender, days):
        if gender == "both" or gender == "all":
            if days == 2:
                link = "https://cricsheet.org/downloads/recently_added_2_csv.zip"
                link = requests.get(link)
                zip = zipfile.ZipFile(io.BytesIO(link.content))
                zip.extractall()
            if days == 7:
                link = "https://cricsheet.org/downloads/recently_added_7_csv.zip"
                link = requests.get(link)
                zip = zipfile.ZipFile(io.BytesIO(link.content))
                zip.extractall()
            if days == 30:
                link = "https://cricsheet.org/downloads/recently_added_30_csv.zip"
                link = requests.get(link)
                zip = zipfile.ZipFile(io.BytesIO(link.content))
                zip.extractall()
        if gender == "women" or gender == "women":
            if days == 2:
                link = "https://cricsheet.org/downloads/recently_added_2_female_csv.zip"
                link = requests.get(link)
                zip = zipfile.ZipFile(io.BytesIO(link.content))
                zip.extractall()
            if days == 7:
                link = "https://cricsheet.org/downloads/recently_added_7_female_csv.zip"
                link = requests.get(link)
                zip = zipfile.ZipFile(io.BytesIO(link.content))
                zip.extractall()
            if days == 30:
                link = "https://cricsheet.org/downloads/recently_added_30_female_csv.zip"
                link = requests.get(link)
                zip = zipfile.ZipFile(io.BytesIO(link.content))
                zip.extractall()
        if gender == "men" or gender == "male":
            if days == 2:
                link = "https://cricsheet.org/downloads/recently_added_2_male_csv.zip"
                link = requests.get(link)
                zip = zipfile.ZipFile(io.BytesIO(link.content))
                zip.extractall()
            if days == 7:
                link = "https://cricsheet.org/downloads/recently_added_7_male_csv.zip"
                link = requests.get(link)
                zip = zipfile.ZipFile(io.BytesIO(link.content))
                zip.extractall()
            if days == 30:
                link = "https://cricsheet.org/downloads/recently_added_30_male_csv.zip"
                link = requests.get(link)
                zip = zipfile.ZipFile(io.BytesIO(link.content))
                zip.extractall()
                
    def recent_csv2(self, gender, days):
        if gender == "both" or gender == "all":
            if days == 2:
                link = "https://cricsheet.org/downloads/recently_added_2_csv2.zip"
                link = requests.get(link)
                zip = zipfile.ZipFile(io.BytesIO(link.content))
                zip.extractall()
            if days == 7:
                link = "https://cricsheet.org/downloads/recently_added_7_csv2.zip"
                link = requests.get(link)
                zip = zipfile.ZipFile(io.BytesIO(link.content))
                zip.extractall()
            if days == 30:
                link = "https://cricsheet.org/downloads/recently_added_30_csv2.zip"
                link = requests.get(link)
                zip = zipfile.ZipFile(io.BytesIO(link.content))
                zip.extractall()
        if gender == "women" or gender == "women":
            if days == 2:
                link = "https://cricsheet.org/downloads/recently_added_2_female_csv2.zip"
                link = requests.get(link)
                zip = zipfile.ZipFile(io.BytesIO(link.content))
                zip.extractall()
            if days == 7:
                link = "https://cricsheet.org/downloads/recently_added_7_female_csv2.zip"
                link = requests.get(link)
                zip = zipfile.ZipFile(io.BytesIO(link.content))
                zip.extractall()
            if days == 30:
                link = "https://cricsheet.org/downloads/recently_added_30_female_csv2.zip"
                link = requests.get(link)
                zip = zipfile.ZipFile(io.BytesIO(link.content))
                zip.extractall()
        if gender == "men" or gender == "male":
            if days == 2:
                link = "https://cricsheet.org/downloads/recently_added_2_male_csv2.zip"
                link = requests.get(link)
                zip = zipfile.ZipFile(io.BytesIO(link.content))
                zip.extractall()
            if days == 7:
                link = "https://cricsheet.org/downloads/recently_added_7_male_csv2.zip"
                link = requests.get(link)
                zip = zipfile.ZipFile(io.BytesIO(link.content))
                zip.extractall()
            if days == 30:
                link = "https://cricsheet.org/downloads/recently_added_30_male_csv2.zip"
                link = requests.get(link)
                zip = zipfile.ZipFile(io.BytesIO(link.content))
                zip.extractall()

    def recent_json(self, gender, days):
        if gender == "both" or gender == "all":
            if days == 2:
                link = "https://cricsheet.org/downloads/recently_added_2_json.zip"
                link = requests.get(link)
                zip = zipfile.ZipFile(io.BytesIO(link.content))
                zip.extractall()
            if days == 7:
                link = "https://cricsheet.org/downloads/recently_added_7_json.zip"
                link = requests.get(link)
                zip = zipfile.ZipFile(io.BytesIO(link.content))
                zip.extractall()
            if days == 30:
                link = "https://cricsheet.org/downloads/recently_added_30_json.zip"
                link = requests.get(link)
                zip = zipfile.ZipFile(io.BytesIO(link.content))
                zip.extractall()
        if gender == "women" or gender == "women":
            if days == 2:
                link = "https://cricsheet.org/downloads/recently_added_2_female_json.zip"
                link = requests.get(link)
                zip = zipfile.ZipFile(io.BytesIO(link.content))
                zip.extractall()
            if days == 7:
                link = "https://cricsheet.org/downloads/recently_added_7_female_json.zip"
                link = requests.get(link)
                zip = zipfile.ZipFile(io.BytesIO(link.content))
                zip.extractall()
            if days == 30:
                link = "https://cricsheet.org/downloads/recently_added_30_female_json.zip"
                link = requests.get(link)
                zip = zipfile.ZipFile(io.BytesIO(link.content))
                zip.extractall()
        if gender == "men" or gender == "male":
            if days == 2:
                link = "https://cricsheet.org/downloads/recently_added_2_male_json.zip"
                link = requests.get(link)
                zip = zipfile.ZipFile(io.BytesIO(link.content))
                zip.extractall()
            if days == 7:
                link = "https://cricsheet.org/downloads/recently_added_7_male_json.zip"
                link = requests.get(link)
                zip = zipfile.ZipFile(io.BytesIO(link.content))
                zip.extractall()
            if days == 30:
                link = "https://cricsheet.org/downloads/recently_added_30_male_json.zip"
                link = requests.get(link)
                zip = zipfile.ZipFile(io.BytesIO(link.content))
                zip.extractall()

    def recent_yaml(self, gender, days):
        if gender == "both" or gender == "all":
            if days == 2:
                link = "https://cricsheet.org/downloads/recently_added_2.zip"
                link = requests.get(link)
                zip = zipfile.ZipFile(io.BytesIO(link.content))
                zip.extractall()
            if days == 7:
                link = "https://cricsheet.org/downloads/recently_added_7.zip"
                link = requests.get(link)
                zip = zipfile.ZipFile(io.BytesIO(link.content))
                zip.extractall()
            if days == 30:
                link = "https://cricsheet.org/downloads/recently_added_30.zip"
                link = requests.get(link)
                zip = zipfile.ZipFile(io.BytesIO(link.content))
                zip.extractall()
        if gender == "women" or gender == "women":
            if days == 2:
                link = "https://cricsheet.org/downloads/recently_added_2_female.zip"
                link = requests.get(link)
                zip = zipfile.ZipFile(io.BytesIO(link.content))
                zip.extractall()
            if days == 7:
                link = "https://cricsheet.org/downloads/recently_added_7_female.zip"
                link = requests.get(link)
                zip = zipfile.ZipFile(io.BytesIO(link.content))
                zip.extractall()
            if days == 30:
                link = "https://cricsheet.org/downloads/recently_added_30_female.zip"
                link = requests.get(link)
                zip = zipfile.ZipFile(io.BytesIO(link.content))
                zip.extractall()
        if gender == "men" or gender == "male":
            if days == 2:
                link = "https://cricsheet.org/downloads/recently_added_2_male.zip"
                link = requests.get(link)
                zip = zipfile.ZipFile(io.BytesIO(link.content))
                zip.extractall()
            if days == 7:
                link = "https://cricsheet.org/downloads/recently_added_7_male.zip"
                link = requests.get(link)
                zip = zipfile.ZipFile(io.BytesIO(link.content))
                zip.extractall()
            if days == 30:
                link = "https://cricsheet.org/downloads/recently_added_30_male.zip"
                link = requests.get(link)
                zip = zipfile.ZipFile(io.BytesIO(link.content))
                zip.extractall()
Cricsheet().recent_csv(gender="women", days=7)
