import datetime
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import calendar
import configparser


class FlightTicket():

    def getWeekNo(self, month, day):

        year = datetime.datetime.now().date().year

        firstSunday = 7 - calendar.weekday(year, month, 1)
        weekno = (day - firstSunday)//7 + 2

        return weekno, calendar.weekday(year, month, day)

    def setAirport(self, way):
        btn_no = 1 if way == 'DEPARTURE' else 2 if way == 'ARRIVAL' else None

        self.browser.find_element(
            By.XPATH, f'//*[@id="__next"]/div/div[1]/div[4]/div/div/div[2]/div[1]/button[{btn_no}]').click()
        time.sleep(1)
        self.browser.find_element(
            By.CLASS_NAME, 'autocomplete_input__1vVkF').send_keys(self.config[way]['AIRPORT'])
        time.sleep(1)
        self.browser.find_element(
            By.CLASS_NAME, 'autocomplete_search_item__2WRSw').click()
        time.sleep(1)

    def setDay(self, way):

        if way == 'DEPARTURE':
            try:
                WebDriverWait(self.browser, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="__next"]/div/div[1]/div[4]/div/div/div[2]/div[2]/button[1]'))).click()
            except Exception as e:
                print(e)
                self.browser.quit()
            time.sleep(1)
            month = int(self.config['DEPARTURE']['MONTH'])
            day = int(self.config['DEPARTURE']['DAY'])
            

        elif way == 'ARRIVAL':
            month = int(self.config['ARRIVAL']['MONTH'])
            day = int(self.config['ARRIVAL']['DAY'])

        else:
            print('Error')
            return

        weekno, weekday = self.getWeekNo(month, day)
        self.browser.find_element(
            By.XPATH, f'//*[@id="__next"]/div/div[1]/div[10]/div[2]/div[1]/div[2]/div/div[{month}]/table/tbody/tr[{weekno}]/td[{(weekday+2)}]/button').click()
        time.sleep(1)

    def __init__(self):

        self.config = configparser.ConfigParser()
        self.config.read('./config.ini')

        chrome_options = webdriver.ChromeOptions()
        self.browser = webdriver.Chrome(
            service=Service(ChromeDriverManager().install()), options=chrome_options)

    def reserve(self):

        self.browser.maximize_window()

        url = 'https://flight.naver.com/'
        self.browser.get(url)

        self.setDay('DEPARTURE')

        self.setDay('ARRIVAL')

        self.setAirport('DEPARTURE')

        self.setAirport('ARRIVAL')

        self.browser.find_element(
            By.XPATH, '//*[@id="__next"]/div/div[1]/div[4]/div/div/button').click()

        try:
            WebDriverWait(self.browser, 10).until(EC.presence_of_element_located(
                (By.XPATH, '//*[@id="__next"]/div/div[1]/div[5]/div/div[2]/div[2]/div/button'))).click()
            
            time.sleep(1)

            self.browser.find_element(
                By.XPATH, '//*[@id="__next"]/div/div[1]/div[5]/div/div[3]/div[2]/div/button').click()
            time.sleep(1)

            self.browser.find_element(
                By.XPATH, '//*[@id="__next"]/div/div[1]/div[4]/div/div[2]/div[2]/div/div[2]/a').click()
            time.sleep(1)
        except Exception as e:
            print(e)
        finally:
            time.sleep(10)
            self.browser.quit()


if __name__ == '__main__':
    ticket = FlightTicket()
    ticket.reserve()
