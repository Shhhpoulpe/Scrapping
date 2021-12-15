from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

driver = webdriver.Chrome('/Users/maxime/Desktop/Code/Scrapping/selenium/chromedriver')
driver.get('https://www.youtube.com/c/TurboA/videos')
WebDriverWait(driver,20)
driver.find_elements_by_xpath(f"//*[contains(text(), 'accepte')]")[-1].click()
