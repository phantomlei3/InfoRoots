import hashlib
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from multiprocessing import Process
from PostgreSQL.database import database
from article import article


class citationsNetwork:
    '''
        citationsNetwork represents all citations in one article
        It communicated with database mediator to obtain data and invoke scrapy crawler to extract information.
        It contains all functions related to build citations network on the user interface.
        '''

    def __init__(self, article_id):
        '''
        The initiator of citationsNetwork only assigns variables from outside and create database mediator

        '''
        self.article_id = article_id
        self.db = database()

    def get(self):
        '''
        The main function in citationsNetwork to check if publisher information exists in citations table
        And use Article class to obtain information for each citation link
        :return: a json dictionary that contains:
                'article_paragraphs':  []
                'citation_links':   []
                'citation_info': {'link': {'article_title', 'article_content', 'article_credibility'}}
        :return None if article is not in database
        '''

        json_dict = dict()

        # extract information from database
        citation_results = self.db.lookup_citation(self.article_id)
        if citation_results is not None:
            article_paragraphs = citation_results[0]
            citation_links = citation_results[1]

            # obtain specific info for each citation link
            ## TODO: Advance parallel processing
            ## NOW: limit three citations only (for convenience)
            citation_info = dict()
            count = 0
            for i in range(len(citation_links)):
                one_info = dict()
                # skip non-existed citations
                if citation_links[i] == "None" or count >= 3:
                    citation_links[i] = "None"
                    continue
                cited_article = article(citation_links[i])
                article_result = cited_article.get()
                if article_result is not None:
                    # create inner dict to store information for one citation
                    one_info['article_title'] = article_result['article_title']
                    one_info['article_content'] = article_result['article_content']
                    one_info['article_credibility'] = article_result['article_reliability']
                    citation_info[citation_links[i]] = one_info
                    count += 1
                else:
                    # delete non-profile citation link
                    citation_links[i] = "None"

            json_dict['article_paragraphs'] = article_paragraphs
            json_dict['citation_links'] = citation_links
            json_dict['citation_info'] = citation_info

            return json_dict
        else:
            return None







