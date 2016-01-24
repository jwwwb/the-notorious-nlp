import webcrawler as wc
import numpy as np

def main():
    crawler = wc.Crawler('The-notorious-big')
    crawler.crawl()
    print crawler.lyrics

if __name__ == '__main__':
    main()

