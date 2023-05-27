import requests
from bs4 import BeautifulSoup
response = requests.get('https://www.example.com/')
if response.status_code == 200:
  soup = BeautifulSoup(response.content, "html.parser")
  soup_list = soup.find_all("a")
  for i in soup_list:
      href = i.get("href")
      print(href)
      if href.startswith("https://"):
        print(i)
else:
    print("НЕ має підключення:" , response.status_code)