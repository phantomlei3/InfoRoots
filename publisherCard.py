
import hashlib
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from multiprocessing import Process
from PostgreSQL.database import database

class publisherCard:

    '''
    publisherCard represents one publisher card that describe one publisher's information
    It communicated with database mediator to obtain data and invoke scrapy crawler to extract information.
    It contains all functions related to build publisher card on the user interface.
    Existing features:
    - get publisher' introduction
    - get publisher' article lists -> publisher' credibility scores
    '''

    def __init__(self, profile):
        '''
        The initiator of publisherCard only assigns variables from outside and create database mediator

        :param profile: a profile of publisher website that this article belongs to

        '''
        self.publisher_name = profile["name"]
        self.publisher_id = str(hashlib.md5(profile["domain"].encode()).hexdigest()) # author_id is primary key in author Table
        self.profile = profile
        self.db = database() # database mediator

    def get(self):
        '''
        The main function in publisherCard to check if publisher information exists in publishers table
        If not existed, utilize publisher crawler to obtain information
        :return: a json dictionary that contains:
                "'publisher_name':  "
                "'publisher_intro':   "
                "'publisher_reliability_score':   ""
        :return None if any error existed in crawler and database
        '''

        publisher_dict = dict()

        # check if the author information exists in the database
        publisher_info = self.db.lookup_publisher(self.publisher_id)
        # use crawler to generate results in database
        if publisher_info is None:
            self.process_publisher()
            publisher_info = self.db.lookup_publisher(self.publisher_id)
            # if something wrong with crawler, return None
            if publisher_info is None:
                return None

        publisher_dict["publisher_name"] = self.publisher_name
        publisher_dict["publisher_intro"] = publisher_info[0]
        publisher_dict["publisher_reliability_score"] = publisher_info[1]

        return publisher_dict

    def process_publisher(self):
        '''
        helper function for get
        use scrapy crawler to store author information
        '''
        # create crawler to obtain author information
        p = Process(target=thread_publisher_crawl, args=(self.publisher_id, self.profile))
        p.start()
        p.join()


# helper thread function for publisher crawler
def thread_publisher_crawl(id, profile):
    '''

    :param id: the unique md5 value of publisher URL
    :param profile: a profile of publisher website that this article belongs to
    '''
    process = CrawlerProcess(get_project_settings())
    process.crawl('authors', id=id, profile=profile)
    process.start()
