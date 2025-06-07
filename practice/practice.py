from bs4 import BeautifulSoup
import requests

url = 'https://en.wikipedia.org/wiki/IBM'

response = requests.get(url)

print(response.status_code)

html_content = response.text

print(html_content[:500])

soup = BeautifulSoup(html_content,'html.parser')

links = soup.find_all('a')

for link in links:
    print(link.text)