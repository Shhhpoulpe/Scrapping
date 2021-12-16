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

# Création de PoulpoTron3.0
client = discord.Client()

# Création de l'objet selenium headless
ser = Service(r"C:\Users\maxjo\OneDrive\Bureau\Code\Scrapping\selenium\chromedriver.exe")
options = Options()
options.add_argument('--headless')
options.add_argument('--disable-gpu')
driver = webdriver.Chrome(service = ser, options=options)

# Connect to Youtube and accept the cookies
driver.get('https://www.youtube.com/channel/UCJLvLnSLEoJEMUrMMqNEomQ/videos')
WebDriverWait(driver,20)
driver.find_elements(By.XPATH,"//*[contains(text(), 'accepte')]")[-1].click()

# Boucle discord de 10 secondes
@tasks.loop(seconds = 10)
async def myLoop():
    # Attends que le bot soit connecté
    await client.wait_until_ready()
    new_video = findLastVideo()
    global last_video
    channel = client.get_channel(741298761569009826)
    # Envoie un message si la dernière vidéo est différente de la dernière vidéo envoyée
    if new_video != last_video:
        print(new_video)
        last_video = new_video
        await channel.send(new_video)
    else:
        print("No new video")

# Cherche la dernière vidéo
def findLastVideo():
    driver.refresh()
    time.sleep(10)
    WebDriverWait(driver,20)
    last_video = driver.find_element(By.ID,"video-title")
    return last_video.text

# Cherche la dernière vidéo
last_video = findLastVideo()
print(last_video)


# Démarrage de la boucle
myLoop.start()
# Token stocké dans discord_param.py
client.run(discord_token)
