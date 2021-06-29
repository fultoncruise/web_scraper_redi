import requests
from bs4 import BeautifulSoup
import pandas as pd
import matplotlib.pyplot as plt

movie_page = "https://www.imdb.com/search/title/?groups=top_250&sort=user_rating"

movie_page_html = requests.get(movie_page, headers = {"Accept-Language": "en-US"})

movie_soup = BeautifulSoup(movie_page_html.content, 'html.parser')

filtered = movie_soup.find_all('div', {"class": "lister-item mode-advanced"})



for i in filtered:
    title = i.find('h3')
    name = title.find('a').text
    year = title.find('span', {"class": "lister-item-year"}).text

    rating_bar = i.find('div', {"class": "ratings-imdb-rating"})
    rating =  rating_bar.find('strong').text
    print(name, " ", year , " ", rating)


    movie_records = []
for i in filtered:
    title = i.find('h3')
    name = title.find('a').text
    year = title.find('span', {"class": "lister-item-year"}).text

    rating_bar = i.find('div', {"class": "ratings-imdb-rating"})
    rating =  rating_bar.find('strong').text

    movie_records.append({'Movie_Name': name, 'Year':year, 'Ratings':rating})

movie_df = pd.DataFrame(movie_records)
movie_df.head()
