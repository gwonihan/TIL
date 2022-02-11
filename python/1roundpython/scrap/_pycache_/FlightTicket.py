from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


import configparser
import datetime
import calendar


class FlightTicket():
    def __init__(self):
        self.config = configparser.ConfigParser()
        self.config.read('./config.ini')

        chrome_options = webdriver.ChromeOptions()
        self.brower = webdriver.Chrome(
            service=Service(ChromeDriverManager().install()), options=chrome_options)
        # self.browser = webdriver.Chrome('./chromedriver.exe')

    def getWeekNo(self, month, day):
        year = datetime.datetime.now().date().year
        
        firstweekDay = calendar.weekday(year,month, 1)
        firstSunday = 7 - firstweekDay
        weekno = (day - firstSunday)//7 + 2

        return weekno, calendar.weekday(year, month, day)

    def setDay(self, way):
        if way == 'DEPARTURE':
                WebDriverWait(self.browser, 10).until(EC.presence_of_all_elements_located((By.XPATH,
                '//*[@id="__next"]/div/div[1]/div[4]/div/div/div[2]/div[2]/button[1]'))).click()
                month = int(self.config['DEPARTUR']['MONTH'])
                day = int(self.config['DEPARTRUE']['DAY'])

                weekno, weekday = self.getWeekNo(month, day)

                self.browser.find_element(By.XPATH, 
                f'//*[@id="__next"]/div/div[1]/div[11]/div[2]/div[1]/div[2]/div/div[{month}]/table/tbody/tr[{weekno}]/td[{(weekday + 2)%7}]/button').click()


    def reserve(self):
        self.browser.maximize_window()
        
        url = 'https://flight.naver.com/'
        self.browser.get(url)

        self.setDay('DEPARTURE')

        #얼마나 기다릴 것인지

         

if __name__ == '__main__':
    ticket = FlightTicket()
    ticket.reserve()