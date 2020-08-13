import requests
from bs4 import BeautifulSoup

url= (
        f"https://www.imdb.com/search/title?title_type="
        f"feature&sort=num_votes,desc&count=10"
    )

soup = BeautifulSoup(requests.get(url).text, "html.parser")

for x in soup.findAll("div", class_="lister-item mode-advanced"):
    print("\n" + x.h3.a.text) # movie's name
    print(x.find("span", attrs={"class": "genre"}).text) # movie genre
    print(x.strong.text) # movie's rating
    print((x.find("span", attrs={"class": "runtime"}).text)) # movie's runtime
    mov_li = ("https://www.imdb.com/" + x.h3.a['href'])
    print(mov_li)
    
    soup1 = BeautifulSoup(requests.get(mov_li).text, "html.parser")

    for y in soup1.findAll("div", class_="summary_text"):
        print(y.text.strip()) # movie's plot
    print ('*' * 100)

