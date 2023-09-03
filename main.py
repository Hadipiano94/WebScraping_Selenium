from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_driver_path = "D:/chromedriver.exe"

form_link = "https://docs.google.com/forms/d/e/1FAIpQLSdLLMsjgb_0pu32lFx62ywMqsphsBAtP4NPRSh-O2BMxvNA-w/viewform?usp=sf_link"
search_link = "https://www.zillow.com/liberty-mo/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22mapBounds%22%3A%7B%22north%22%3A52.92953336908615%2C%22east%22%3A-85.163336875%2C%22south%22%3A20.50024342502191%2C%22west%22%3A-131.745368125%7D%2C%22mapZoom%22%3A4%2C%22regionSelection%22%3A%5B%7B%22regionId%22%3A5624%2C%22regionType%22%3A6%7D%2C%7B%22regionId%22%3A20330%2C%22regionType%22%3A6%7D%5D%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22price%22%3A%7B%22max%22%3A300000%2C%22min%22%3A100000%7D%2C%22mp%22%3A%7B%22max%22%3A1508%2C%22min%22%3A503%7D%2C%22ah%22%3A%7B%22value%22%3Atrue%7D%2C%22sort%22%3A%7B%22value%22%3A%22globalrelevanceex%22%7D%2C%22beds%22%3A%7B%22min%22%3A1%7D%7D%2C%22isListVisible%22%3Atrue%7D"

driver = webdriver.Chrome()
driver.get(search_link)

sleep(3)

property_list = driver.find_elements(By.CSS_SELECTOR, "#grid-search-results ul li")
for house in property_list:
    print(house.text)

property_info = [[house.find_element(By.NAME, "address").text, house.find_element(By.NAME, "span").text, house.find_element(By.CSS_SELECTOR, "article a").value_of_css_property("href")] for house in property_list]


for house in property_info:
    driver.get(form_link)
    questions = driver.find_elements(By.CSS_SELECTOR, ".Qr7Oae")
    sleep(1)
    for i in range(len(questions)):
        questions[i].find_element(By.NAME, "input").send_keys(house[i])
        sleep(1)
    submit_button = driver.find_element(By.CSS_SELECTOR, ".e19J0b .CeoRYc")
    submit_button.click()


sleep(10)
driver.quit()
