#!/usr/bin/env python
import random


class Player(object):

    def __init__(self,
                 name,
                 position,
                 goals,
                 assists,
                 plus_minus,
                 pims,
                 ppp,
                 toi):

        self.name = name
        self.position = position
        self.goals = goals
        self.assists = assists
        self.plus_minus = plus_minus
        self.pims = pims
        self.ppp = ppp
        self.toi = toi

    def __str__(self):
        msg = "name: {}, pos: {}, G: {}, A: {}"
        return msg.format(self.name, self.position, self.goals, self.assists)

    def is_defenceman(self):
        return self.position == 'D'

    def toi_in_seconds(self):
        toi = self.toi.split(':')
        return float(toi[0]) * 60 + float(toi[1])


players = []

for f in ['out.txt', '20172018.txt']:
    with open(f) as input_file:
        content = input_file.readlines()

    for line in content:
        parsed_line = line.replace('\n', '').split(',')
        if int(parsed_line[5]) >= 82:
            player = Player(parsed_line[1],
                            parsed_line[4],
                            parsed_line[6],
                            parsed_line[7],
                            parsed_line[9],
                            parsed_line[10],
                            parsed_line[13],
                            parsed_line[20])
            players.append(player)

print "{},2,forward,defenceman".format(len(players))

for player in players:
    print "{goals},{assits},{pm},{pims},{ppp},{toi},{is_dman}".format(
        goals=float(player.goals),
        assits=float(player.assists),
        pm=float(player.plus_minus),
        pims=float(player.pims),
        ppp=float(player.ppp),
        toi=float(player.toi_in_seconds()),
        is_dman=int(player.is_defenceman())
    )
