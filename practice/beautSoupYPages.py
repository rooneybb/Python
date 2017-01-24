import requests
from bs4 import BeautifulSoup

url = "http://www.yellowpages.com/search?search_terms=tech+&geo_location_terms=Chicago%2C+IL"
r = requests.get(url)

soup = BeautifulSoup(r.content, "html.parser")

links = soup.find_all("a")

for link in links:
    if "http" in link:
        print ("%s, %s", %s(link.get("href"), link.text))
