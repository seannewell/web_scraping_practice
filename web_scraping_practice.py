# web_scraping_practice.py
#
# This is a .py file that scrapes information from the
# blog page on runwayaudio.com and turns it into a
# .csv file that can be opened in Excel
import requests
from bs4 import BeautifulSoup
from csv import writer

response = requests.get('https://runwayaudio.com/blogs/news')

soup = BeautifulSoup(response.text,'html.parser')

posts = soup.findAll(class_='article')

with open('RunwayBlogPosts.csv', 'w') as csv_file:
        csv_writer = writer(csv_file)
        headers = ['Title', 'Link', 'Date', 'Author']
        csv_writer.writerow(headers)

        for post in posts:
            title = post.find('h2').get_text().replace('\n','')
            link = post.find('a')['href']
            author = post.find(class_='author').get_text().replace('by','').replace(' ','',1)
            post.find(class_='author').replace_with('')
            date = post.find(class_='iconmeta time').get_text().replace('\n','').replace(' ','')
            csv_writer.writerow([title, link, date, author])
