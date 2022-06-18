from bs4 import BeautifulSoup as bs
import requests

url = "https://www.goodreads.com/review/list/134820979-aditirao-kalanji?utf8=%E2%9C%93&utf8=%E2%9C%93&ref=nav_mybooks&shelf=owned&title=aditirao-kalanji&per_page=infinite"

page = requests.get(url)
soup = bs(page.content, "html.parser")
#print(soup)

result = soup.find_all("a")
#print(result)
print(len(result))
