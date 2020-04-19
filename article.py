

from multiprocessing import Process
import hashlib
import json
import unidecode

from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from PostgreSQL.database import database
from NELA.NELAdapter import NELAdapter
import os
from langdetect import detect

class article:
    '''
     class article represent any article that is available to access online
        and all information will be stored in PostgreSQL tables
     Each article has
        URL, the http/https web link of article
        article_id, md5 value converted by URL and stored as key in PostgreSQL table
        article_title, string
        article_content, string
        publisher_name, string
        author_name, string
    '''

    def __init__(self, url):
        '''
        :param url: the url of article link
        :param check_citations, boolean that requires article to check citations
        '''
        self.url = url
        self.article_id = str(hashlib.md5(url.encode()).hexdigest())
        self.db = database()
        self.website_profiles = json.load(open("website_profiles/profiles.json"))


    def get(self):
        '''

        main function to get article information in article class

        :param conn_string: a string for psycopg2 connection setup
        :param website_profiles: a json dictionary that
                                contains all crawling information for every publisher website
        :return a json dictionary that contains
                { "article_id":   ,
                "profile": ,
                "article_title": ,
                "article_content":  ,
                "publisher_name":   ,
                "author_name":   ,
                "author_page_link":  ,
                "article_reliability":    ,
                "article_bias"    }

                if article is accessible to extract and store information
                None if website profiles does not contain the profile for this article's publisher website
        '''

        article_dict = dict()

        # get article website profile
        try:
            url_domain = self.url.split("/")[2].strip()
        except:
            return None
        if self.url.split("/")[2].strip() in self.website_profiles:
            profile = self.website_profiles[url_domain]
        else:
            return None

        # check if article exists in the database
        article_info = self.db.lookup_article(self.article_id)
        if article_info is None:
            # crawl article information
            p = Process(target=thread_article_crawl, args=(self.article_id, self.url, profile))
            p.start()
            p.join()
            article_info = self.db.lookup_article(self.article_id)

        try:
            article_dict["article_id"] = self.article_id
            article_dict["profile"] = profile
            article_dict["article_title"] = article_info[0]
            article_dict["article_content"] = article_info[1]
            article_dict["publisher_name"] = article_info[2]
            article_dict["author_name"] = article_info[3]
            article_dict["author_page_link"] = article_info[4]
        except:
            return None

        # if the article is not in English, it will not have any credibility scores
        if detect(article_dict["article_title"]) == "en":
            # check if article credibility exists in the database
            article_credibility = self.db.lookup_article_credibility(self.article_id)
            if article_credibility is None:
                # obtain article credibility information through NELAdapter
                # solve unicode issue by ignoring unrecognized codes
                NELA_title = unidecode.unidecode(article_dict["article_title"])
                NELA_content = unidecode.unidecode(article_dict["article_content"])
                NELA_article = NELAdapter(NELA_title, NELA_content)
                self.db.insert_article_credibility(self.article_id, NELA_article.get_reliability_score(), NELA_article.get_bias_score())
                article_credibility = self.db.lookup_article_credibility(self.article_id)

            article_dict["article_reliability"] = article_credibility[0]
            article_dict["article_bias"] = article_credibility[1]
        else:
            article_dict["article_reliability"] = -1
            article_dict["article_bias"] = -1

        return article_dict


def thread_article_crawl(id, url, profile, check_citations):
    '''
    A helper thread function for article crawl
    :param profile: a profile of publisher website that this article belongs to
    :param conn_string: a psycopg2 connection setup string
    '''
    process = CrawlerProcess(get_project_settings())
    process.crawl('articles', id=id, url=url, profile=profile)
    process.start()


