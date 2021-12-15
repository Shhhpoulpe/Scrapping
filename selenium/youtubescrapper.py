from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

driver = webdriver.Chrome('/Users/maxime/Desktop/Code/Scrapping/selenium/chromedriver')
driver.get('https://www.youtube.com/c/TurboA/videos')
WebDriverWait(driver,20).until(EC.frame_to_be_available_and_switch_to_it((By.ID,"yDmH0d")))
driver.find_element_by_xpath("//*[contains(text(), 'J'ACCEPTE')]").click()
