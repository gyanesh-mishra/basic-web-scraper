import time
from selenium import webdriver
import slack
import sys
import requests
import os

URL = os.getenv('URL', 'Please provide a valid URL')
XPATH = os.getenv(
    'XPATH', "//*[@id='page-top']/main/ui-view/section/div[3]/div[2]/div/div[2]")
SLACKBOT_TOKEN = os.getenv('SLACKBOT_TOKEN', 'Please provide a valid token')
SLACKBOT_CHANNEL = os.getenv(
    'SLACKBOT_CHANNEL', 'Please provide a valid channel')


def check_xpath():
    # Setup headless chrome
    options = webdriver.ChromeOptions()
    options.add_argument('headless')
    driver = webdriver.Chrome(options=options)

    # Navigate to given URL
    driver.get(URL)
    # Wait for webpage to load
    time.sleep(10)

    # Find XPATH element and inform if found
    elements_to_find = driver.find_elements_by_xpath(XPATH)
    if elements_to_find:
        for element in elements_to_find:
            send_slack_message(element.text)
        return True

    return False


def send_slack_message(text):

    client = slack.WebClient(SLACKBOT_TOKEN)

    response = client.chat_postMessage(
        channel=SLACKBOT_CHANNEL,
        text=text)


# Check every 5 minutes
while True:
    if check_xpath():
        break
    time.sleep(300)
