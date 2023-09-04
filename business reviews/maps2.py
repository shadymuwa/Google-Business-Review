import pandas as pd
import numpy as np
import warnings
warnings.filterwarnings("ignore")
# import matplotlib.pyplot as plt
# import seaborn as sns
# from datetime import datetime as dt

# import plotly.express as px
# import plotly.graph_objects as go
# import nbformat

# from urllib.request import urlopen
# import json

# import requests
# from bs4 import BeautifulSoup

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC

import time

from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver

from pathlib import Path

URL =  "https://www.google.com/search?q=Homestead+high+school+rating&oq=Homestead+high+school+rating&gs_lcrp=EgZjaHJvbWUyBggAEEUYOdIBCDc2NTdqMGo3qAIAsAIA&sourceid=chrome&ie=UTF-8#"
URL = "https://www.google.com/maps/place/Miami+Valley+Hospital/@39.7454533,-84.1881836,17z/data=!3m1!5s0x884086a826496aeb:0xd02b21d2331c0faa!4m8!3m7!1s0x884084029d34c775:0x7fdb37e4b374b852!8m2!3d39.7454533!4d-84.1856087!9m1!1b1!16s%2Fm%2F04cr78q?entry=ttu"
def get_data(driver):
    print('Get Data...')
    more_elements = driver.find_elements(By.XPATH, '//button[@class="w8nwRe kyuRq"]')
    for list_more_element in more_elements:
        list_more_element.click()

    elements = driver.find_elements(By.XPATH, '//div[@class="jftiEf fontBodyMedium "]')
    for element in elements:
        print(element)
    print("Number of Elements Found: " + str(len(elements)))
    print("Number of Elements Found: " , elements)
    # lst_data = []
    # for data in elements:
    #     name = data.find_element(By.XPATH, './/div[@class="d4r55 "]').text
    #     try:
    #         text = data.find_element(By.XPATH, './/div[@class="MyEned"]/span[1]').text
    #     except:
    #         text = ""
    #     score = data.find_element(By.XPATH, './/span[@class="kvMYJc"]').get_attribute("aria-label")
    #     date = data.find_element(By.XPATH, './/span[@class="rsqaWe"]').text

    #     lst_data.append([name, text, score, date])

    # return lst_data


def counter():
    result = driver.find_element(By.CLASS_NAME, "jANrlb").find_element(By.CLASS_NAME, "fontBodySmall").text
    result = result.replace(',', '')
    result = result.split(' ')
    result = result[0].split('\n')
    print("Number of Surveys: " + result[0])
    return int(int(result[0])/10)+1


def scrolling(counter):
    print('Scrolling...')
    scrollable_div = driver.find_element(By.XPATH, '//div[@class="e07Vkf kA9KIf"]')
    for _i in range(counter):
        scrolling = driver.execute_script(
            'document.getElementsByClassName("dS8AEf")[0].scrollTop = document.getElementsByClassName("dS8AEf")[0].scrollHeight',
            scrollable_div
        )
        time.sleep(3)


def write_to_xlsx(data):
    print('Write to CSV...')
    cols = ["name", "comment", "rating", "date"]
    df = pd.DataFrame(data, columns=cols)

    filepath= Path('homestead_GoogleReviews.csv')
    filepath.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(filepath)


if __name__ == "__main__":

    print('Starting...')
    options = webdriver.ChromeOptions()
    options.add_argument("--no-sandbox")
    options.add_argument("--headless")
    options.add_argument("--lang=en-US")
    #options.add_experimental_option('prefs', {'intl.accept_languages': 'en,en_US'})
    driver = webdriver.Chrome(options = options)

    driver.get(URL)
    time.sleep(5)

    counter = counter()
    scrolling(counter)

    data = get_data(driver)
    driver.close()

    write_to_xlsx(data)
    print('Done!')
