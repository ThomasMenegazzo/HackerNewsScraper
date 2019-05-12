import urllib2
import scrapy
import pandas as pd

start_page = ‘https://news.ycombinator.com/'
page = urllib2.urlopen(quote_page)
soup = BeautifulSoup(page, ‘html.parser’)

def parse(self, response):
        for title in response.css('.post-header>h2'):
            yield {'title': title.css('a ::text').get()}

        for next_page in response.css('a.next-posts-link'):
            yield response.follow(next_page, self.parse)