#!/usr/bin/env python
import time

from selenium import webdriver
from actions import Actions


def get_table_page_info():
    pages = actions.wait_for_class("-totalPages")
    return int(pages.text)


def scrap_stats_table():
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


driver = webdriver.Chrome()

actions = Actions(driver)

driver.get('http://www.nhl.com/stats/player?reportType=season&seasonFrom=20182019&seasonTo=20182019&gameType=2&filter=gamesPlayed,gte,1&sort=points,goals,assists')

total_pages = get_table_page_info()

try:
    for page in range(1, total_pages + 1):
        scrap_stats_table()

        if page != total_pages:
            actions.click_element(classname="-next")

        time.sleep(1)

finally:
    driver.close()
