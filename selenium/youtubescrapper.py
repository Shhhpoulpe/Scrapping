from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time

def findLastVideo():
    driver.refresh()
    time.sleep(10)
    WebDriverWait(driver,20)
    last_video = driver.find_element(By.ID,"video-title")
    return last_video.text

# Connect to Youtube and accept the cookies
ser = Service('/Users/maxime/Desktop/Code/Scrapping/selenium/chromedriver')
driver = webdriver.Chrome(service = ser)
driver.get('https://www.youtube.com/c/TurboA/videos')
WebDriverWait(driver,20)
driver.find_elements(By.XPATH,"//*[contains(text(), 'accepte')]")[-1].click()

# Cherche la dernière vidéo

last_video = findLastVideo()
print(last_video)

while True:
    new_video = findLastVideo()
    if new_video != last_video:
        print(new_video.text)
        last_video = new_video
    else:
        print("No new video")