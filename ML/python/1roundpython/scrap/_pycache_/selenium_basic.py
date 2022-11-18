from selenium import webdriver

browser = webdriver.Chrome('./chromedriver.exe')
# browser.get('http://naver.com')

# browser.find_element_by_class_name('link_login').click()

# browser.back()
# browser.forward()
# browser.refresh() #refresh : 새로고침

from selenium.webdriver.common.keys import Keys

# 검색창에 멀티캠퍼스 입력하기
# query = browser.find_element_by_id('query')
# query.send_keys('멀티캠퍼스')
# query.send_keys(Keys.ENTER)

# tag = browser.find_element_by_tag_name('a')
# print(tag)

# tags = browser.find_elements_by_tag_name('a')
# for tag in tags:
#     print(tag.get_attribute('href'))

browser.get('http://daum.net')

query = browser.find_element_by_name('q')
query.send_keys('멀티캠퍼스')
# query.send_keys(Keys.ENTER)

browser.find_element_by_xpath('//*[@id="daumSearch"]/fieldset/div/div/button[2]').click()

browser.quit()