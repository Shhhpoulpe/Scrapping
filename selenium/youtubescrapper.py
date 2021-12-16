from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time
import discord
from discord.ext import tasks
from discord.ext import commands
from discord_param import discord_token

client = discord.Client()

@tasks.loop(seconds = 10) # repeat after every 10 seconds
async def myLoop():
    # Cherche la dernière vidéo
    await client.wait_until_ready()
    new_video = findLastVideo()
    global last_video
    channel = client.get_channel(741298761569009826)
    if new_video != last_video:
        print(new_video)
        last_video = new_video
        # Send a message to the channel
        await channel.send(new_video)
    else:
        print("No new video")
        await channel.send("No new video")

def findLastVideo():
    driver.refresh()
    time.sleep(10)
    WebDriverWait(driver,20)
    last_video = driver.find_element(By.ID,"video-title")
    return last_video.text

# Connect to Youtube and accept the cookies
ser = Service(r"C:\Users\maxjo\OneDrive\Bureau\Code\Scrapping\selenium\chromedriver.exe")
options = Options()
options.add_argument('--headless')
options.add_argument('--disable-gpu')
driver = webdriver.Chrome(service = ser, options=options)
driver.get('https://www.youtube.com/channel/UCJLvLnSLEoJEMUrMMqNEomQ/videos')
WebDriverWait(driver,20)
driver.find_elements(By.XPATH,"//*[contains(text(), 'accepte')]")[-1].click()

# Cherche la dernière vidéo
last_video = findLastVideo()
print(last_video)


# Démarrage de la boucle
myLoop.start()
# Token stocké dans discord_param.py
client.run(discord_token)
