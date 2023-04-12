import requests
from requests import get
from bs4 import BeautifulSoup
import urllib.request # to download images
import re
import os # to make a directory
import csv
import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import StaleElementReferenceException


driver = webdriver.Chrome(ChromeDriverManager().install())


df_tweets = pd.read_csv('data/tweet_c.csv')

print(df_tweets)
# Navigate to the Twitter page
# start_index = 2684 + 1474 + 1235
start_index = 1214
# [start_index:]
tweet_data_ids = list(df_tweets['Id'])[start_index:]
# Wait for the page to fully load
timeout = 10  # seconds
wait = WebDriverWait(driver, timeout)

for i in range(len(tweet_data_ids)):
    try:

        if i % 400 == 0:
            driver.quit()
            driver = webdriver.Chrome(ChromeDriverManager().install())
            timeout = 10  # seconds
            wait = WebDriverWait(driver, timeout)
            driver.refresh()

        link = 'https://twitter.com/Cobratate/status/' + str(tweet_data_ids[i])
        driver.get(link)

        while True:
            try:
                tweet_divs = wait.until(
                    EC.presence_of_all_elements_located((By.XPATH, '//div[@data-testid="tweetText"]')))

                _data = []
                j = 0
                for tweet_div in tweet_divs:
                    if j != 0:
                        df_d = df_tweets[df_tweets['Id'] == tweet_data_ids[i]]
                        df_d = df_d.reset_index(drop=True)
                        if len(df_d) > 0 and tweet_div is not None and len(tweet_div.text.strip()) > 0:
                            _data.append({
                                "Company_Name": df_d.loc[0, 'Company'],
                                "Tweet": tweet_div.text,
                                "Parent_Id": df_d.loc[0, 'Id'],
                                "Tweet_Date_Time": df_d.loc[0, 'Tweet Date'],
                            })
                    j += 1

                if len(_data) == 0:
                    print(f"Misssing data for {tweet_data_ids[i]}")
                else:
                    tweet_df = pd.DataFrame(_data)
                    tweet_df = tweet_df.drop_duplicates()
                    tweet_df.to_csv('data/tweet_with_replies_all.csv', mode='a', header=False, index=False)
                    print(_data)

                print(f"{i} / {len(tweet_data_ids)}")

                break
            except StaleElementReferenceException:
                driver.quit()
                time.sleep(20)
                driver = webdriver.Chrome(ChromeDriverManager().install())
                timeout = 10  # seconds
                wait = WebDriverWait(driver, timeout)
                driver.refresh()
                continue


    except TimeoutException:
        print(f"Timeout error occurred while scraping data for tweet {tweet_data_ids[i]}")
        continue

    # Print the text of each div element


    # Close the browser window
driver.quit()


    # print(_data)

# for pet_link in tweet_text:
#     print(pet_link.get_attribute('href'))
#     with open('pet_links.txt', 'a') as f:
#         f.write(pet_link.get_attribute('href'))
#         f.write('\n')
