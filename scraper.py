#!/usr/bin/env python

from selenium import webdriver
from actions import Actions


driver = webdriver.Chrome()

actions = Actions(driver)

driver.get('http://www.nhl.com/stats/player?reportType=season&seasonFrom=20182019&seasonTo=20182019&gameType=2&filter=gamesPlayed,gte,1&sort=points,goals,assists')

try:
    actions.wait_for_element("stats-page-body")

    table = driver.find_elements_by_id("stats-page-body")

    player_rows = table[0].find_elements_by_class_name("rt-tr-group")

    for player_row in player_rows:
        columns = player_row.find_elements_by_class_name("rt-td")
        row = ""
        for col in columns:
            if not row:
                row = col.text
            else:
                row = row + "," + col.text

        print row

finally:
    driver.close()
