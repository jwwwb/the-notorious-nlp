from bs4 import BeautifulSoup 
import pandas as pd
import scrapy
from urlparse import urljoin
import requests

class Crawler:
    def __init__(self, artist='The-notorious-big'):
        self.artist = artist
        self.lyrics = []
        
    def crawl(self):
        BASE_URL = 'http://genius.com'
        artist_url = 'http://genius.com/artists/' + self.artist
        response = requests.get(artist_url, headers={'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.153 Safari/537.36'})
        soup = BeautifulSoup(response.text, 'lxml')
        for song_link in soup.select('ul.song_list > li > a'):
            print song_link
            link = urljoin(BASE_URL, song_link['href'])
            response = requests.get(link)
            soup = BeautifulSoup(response.text)
            # print soup
            # lyrics = soup.find('div', class_='lyrics').text.strip()
            # self.lyrics.append(lyrics)
            # tokenize `lyrics` with nltk

