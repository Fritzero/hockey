#!/usr/bin/env python

from bs4 import BeautifulSoup
from string import ascii_lowercase


class Points(object):
    def __init__(self, goals=0, assists=0):
        self.goals = goals
        self.assists = assists
        self.total = self.goals + self.assists


class BirthPlace(object):
    def __init__(self, city, country, state=""):
        self.city = city
        self.country = country
        self.state = state


class Stats(object):
    def __init__(self,
                 games_played,
                 points,
                 pims,
                 seasons,
                 years):
        self.games_played = games_played
        self.points = points
        self.pims = pims
        self.seasons = seasons
        self.years = years


class Player(object):
    def __init__(self,
                 name,
                 position,
                 birthdate,
                 birthplace,
                 stats):
        self.name = name
        self.position = position
        self.birthdate = birthdate
        self.birthplace = birthplace
        self.stats = stats


class Entry(object):
    def __init__(self, player, stats):
        self.player = player
        self.stats = stats


for letter in ascii_lowercase[:1]:
    with open("html_out/html_{}".format(letter), 'r') as f:
        soup = BeautifulSoup(f, "html.parser")
        table_rows = soup.findAll("tr")
        for table_row in table_rows:
            value = ""
            columns = table_row.findAll("td")
            for col in columns:
                if not value:
                    value = col.text
                else:
                    value = value + "," + col.text
            if value:
                print value
