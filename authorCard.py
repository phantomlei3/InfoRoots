
import hashlib
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from multiprocessing import Process
from PostgreSQL.database import database
from article import article


class authorCard:

    '''
    authorCard represents one author card that describe one author from one article.
    It communicated with database mediator to obtain data and invoke scrapy crawler to extract information.
    It contains all functions related to build author card on the user interface.
    Existing features:
    - get authors' introduction
    - get authors' article lists -> authors' credibility scores
    '''

    def __init__(self, article_id, author_page_link, profile, author_name):
        '''
        The initiator of authorCard only assigns variables from outside and create database mediator

        :param article_id: the unique md5 value of article URL
        :param author_page_link: the URL of author page link
        :param profile: a profile of publisher website that this article belongs to
        :param author_name: author name from the article
        '''
        self.article_id = article_id
        self.author_name = author_name
        self.author_page_link = author_page_link
        self.author_id = str(hashlib.md5(author_name.encode()).hexdigest()) # author_id is primary key in author Table
        self.profile = profile
        self.db = database() # database mediator


    def get(self):
        '''
        The main function in authorCard to check if author information exists in authors table
        If not existed, utilize authors crawler to obtain information
        :return: a json dictionary that contains:
                "'author_name':  "
                "'author_intro':   "
                "'author_reliability':   "
                "'author_bias':    "
                "'author_link':   "
        :return None if any error existed in crawler and database
        '''

        author_dict = dict()

        # check if the author information exists in the database
        author_info = self.db.lookup_author(self.author_id)
        # use crawler to generate results in database
        if author_info is None:
            self.process_author()
            author_info = self.db.lookup_author(self.author_id)
            # if something wrong with crawler, return None
            if author_info is None:
                return None

        author_dict["author_name"] = author_info[0]
        author_dict["author_intro"] = author_info[1]
        author_article_list = author_info[2]

        # check if the author credibility information exists in the database
        author_credibility = self.db.lookup_author_credibility(self.author_id)
        if author_credibility is None:
            # use article class to generate credibility in database
            self.process_author_credibility(author_article_list)
            author_credibility = self.db.lookup_author_credibility(self.author_id)

        author_dict["author_reliability"] = author_credibility[0]
        author_dict["author_bias"] = author_credibility[1]
        author_dict["author_link"] = self.author_page_link

        return author_dict

    def process_author(self):
        '''
        helper function for get
        use scrapy crawler to store author information
        '''
        # create crawler to obtain author information
        p = Process(target=thread_author_crawl, args=(self.author_id, self.author_page_link, self.author_name,
                                                      self.profile))
        p.start()
        p.join()

    def sum_list_scores(self, score_list):
        '''
        :return:
        '''

        print(score_list)
        avg_score = 0
        score_length = 0
        for score in score_list:
            if score >= 0:
                avg_score += score
                score_length += 1

        if score_length != 0:
            return avg_score / score_length
        else:
            return -5



    def process_author_credibility(self, author_article_list):
        '''
        helper function for get
        use scrapy crawler to store author credibility information
        and NELA tool to generate credibility scores

        :param author_article_list, a list of article link from this author
        '''
        # use at most recently 3 article to generate reliability and bias score for author
        accumlated_reliability= list()
        accumlated_bias = list()
        for article_link in author_article_list:
            # get article credibility to process
            each_article = article(article_link)
            article_result = each_article.get()
            print(article_link)

            if article_result is None:
                continue

            if article_result["article_reliability"] >= 0:
                accumlated_reliability.append(article_result["article_reliability"])
                accumlated_bias.append(article_result["article_bias"])

            if len(accumlated_reliability) >= 3:
                break

        if len(accumlated_reliability) != 0:

            avg_reliability = self.sum_list_scores(accumlated_reliability)
            avg_bias = self.sum_list_scores(accumlated_bias)
        else:
            # -1 represents Not available reliability/bias
            avg_reliability = -100
            avg_bias = -100
        self.db.insert_author_credibility(self.author_id, avg_reliability, avg_bias)


# helper thread function for author crawler
def thread_author_crawl(id, url, author_name, profile):
    '''

    :param id: the unique md5 value of article URL
    :param url: the URL of article
    :param author_name: author name from the article
    :param profile: a profile of publisher website that this article belongs to
    :param database: a psycopg2 connection setup string
    '''
    process = CrawlerProcess(get_project_settings())
    process.crawl('authors', id=id, author_page_link=url, author_name=author_name, profile=profile)
    process.start()




