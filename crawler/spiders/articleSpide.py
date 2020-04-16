import scrapy
import re
import psycopg2
import psycopg2.extras
from PostgreSQL.database import database


class articleSpide(scrapy.Spider):
    '''
        Scrapy web crawler that extracts article title/content, author, and publisher from one article URL
    '''
    name = "articles"


    def __init__(self, **kw):
        super(articleSpide, self).__init__(**kw)
        self.id = kw.get('id')  # id used for this data in PostgreSQL
        self.url = kw.get('url')  # one URL from user input
        self.database = database()
        self.profile = kw.get('profile') # profile of crawler for this website


    def start_requests(self):
        '''
        Scrapy built-in method to start crawling by calling parse
        '''

        yield scrapy.Request(url=self.url, callback=self.parse)

    def parse(self, response):
        '''
        Scrapy built-in method for scraping pages
        Please do not use this parse function. Scrapy will use it automatically
        :param response: a HTML response from URL
        :returns Article title, article content, author name, author page and publisher name
                will be saved in article Table (PostgreSQL) with id
                if the given url does not have website profile, None will be stored in table
        '''

        '''
        Extract article title, article content, author name, author page and publisher name from one URL
        '''

        # article title and content
        article_title = response.css(self.profile["article_title"]+"::text").get().strip()  # tested
        article_content = self.get_clean_article_contents(response.css(self.profile["article_content"]).extract()) #tested

        # publisher information
        publisher_name = self.profile["name"] # tested

        # author information
        author_name = response.css(self.profile["author_name"]+"::text").get() # tested
        author_page_link = response.css(self.profile["author_page_link"]).attrib["href"].strip("//") # tested

        # store information in PostgreSQL articles Table
        self.database.insert_article(self.id, article_title, article_content,
                                             publisher_name, author_name, author_page_link)


    def get_clean_article_contents(self, article_content_html):
        '''
        extract all article content from HTML response
        TODO: extract citations from article contents

        :param article_content_html: HTML response of article contents
        :return: pure article content without any html tags
        '''
        article_content = ""
        for paragraph in article_content_html:
            clean_paraggraph = re.sub(r'<.*?>', '', paragraph).strip()
            if clean_paraggraph != "":
                article_content += clean_paraggraph + "\n\n"
        return article_content.strip()