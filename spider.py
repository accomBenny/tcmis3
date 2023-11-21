import requests
from bs4 import BeautifulSoup
url = "https://www1.pu.edu.tw/~tcyang/course.html"
Data = requests.get(url)
Data.encoding = "utf-8"

sp = BeautifulSoup(Data.text, "html.parser")
result=sp.select(".team-box")

info = ""
for item in result:
	info+=item.text+"<br>"
	info += item.find("a").get("href")+"<br></br>"
print(info)
