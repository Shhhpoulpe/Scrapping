import requests
from bs4 import BeautifulSoup

# URL de la page a scrapper

page = requests.get("https://www.youtube.com/c/TurboA/videos", cookies={'CONSENT': 'YES+42'})

# Récupération de la page HTML depuis le javascript
# page_js = requests.get(url).text
# page_js = page_js.text.split("\n")

text_file = open("test.html", "w")
n = text_file.write(str(page.text))
text_file.close()

soup = BeautifulSoup(page._content, "html.parser")
test = soup.find_all("div", {"class": "ytd-grid-video-renderer"})
# for test2 in test.find_all('div'):
# i = 0
#     i+=1
#     print('test')

print(test)