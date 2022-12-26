import os
import logging
import requests, random, time
from datetime import datetime, timedelta
from bs4 import BeautifulSoup
import pytz
from dotenv import load_dotenv
from links import LINKS
from utils import set_output, api_telegram


# Load .env file
load_dotenv()


# LOGGING
logging.basicConfig(filename='logs.log', level=logging.INFO, format="")


# CONSTANTS
RANDOM_DELAY = random.randint(5, 20)
SEPARATOR = "-" * 80
TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
TELEGRAM_CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")
TIMEZONE = pytz.timezone("Europe/Rome")


# MAIN
while True:
    now = datetime.now(tz=TIMEZONE)
    now_formatted = now.strftime('%d/%m/%Y %H:%M')
    print(f"{now_formatted:^80}")
    print(SEPARATOR)
    logging.info(now_formatted)
    logging.info(SEPARATOR)
    for link in LINKS:
        if link["active"]:
            try:
                response = requests.get(link["url"], timeout=5)
                soup = BeautifulSoup(response.text, "html.parser")

                if link["type"] == "id":
                    availability = soup.find(id=link["typeKey"])
                else:
                    availability = soup.find(class_=link["typeKey"])

                list_result = []
                if availability != None:
                    for text in availability.stripped_strings:
                        list_result.append(text)
                    if link["noStockString"] in list_result:
                        title = link["name"]
                        body = "RX 7900 XTX is out of stock"
                        extradata = list_result
                        result = set_output(title, body, extradata)
                    else:
                        title = link["name"]
                        body = "RX 7900 XTX is in stock"
                        extradata = list_result
                        result = set_output(title, body, extradata)
                        url = api_telegram(TELEGRAM_TOKEN, TELEGRAM_CHAT_ID, result)
                        requests.get(url, timeout=10)
                else:
                    result = set_output(link["name"], "Request failed", "None")
                print(result["colored"])
                logging.info(f"{result['plain']}")
            except Exception as error:
                result = set_output(link["name"], type(error).__name__, "None")
                print(result["colored"])
                logging.info(result["plain"])
    delay = RANDOM_DELAY * 60
    delay = 3
    next_check = (now + timedelta(seconds=delay)).strftime('%d/%m/%Y %H:%M')
    msg_check = f"Next check at {next_check}"
    print(f"{msg_check:^80}")
    print(SEPARATOR)
    print(("\n" * 3))
    time.sleep(delay)