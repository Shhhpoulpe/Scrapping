from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time

# Connect to Youtube and accept the cookies
ser = Service('/Users/maxime/Desktop/Code/Scrapping/selenium/chromedriver')
driver = webdriver.Chrome(service = ser)
driver.get('https://www.youtube.com/c/TurboA/videos')
WebDriverWait(driver,20)
driver.find_elements(By.XPATH,"//*[contains(text(), 'accepte')]")[-1].click()

# Cherche la dernière vidéo

WebDriverWait(driver,20)
last_video = driver.find_element(By.ID,"video-title")
print(last_video.text)

while True:
    driver.refresh()
    time.sleep(10)
    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "video-title")))
    new_video = driver.find_element(By.ID,"video-title")
    if new_video.text != last_video.text:
        print(new_video.text)
        last_video = new_video
    else:
        print("No new video")