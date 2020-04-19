'''
NELAdapter is designed to use NELA toolkit library through Adapter Pattern Design
The NELA toolkit has a chaotic structure, but we need its functionality in the compatible way
to generate bias scores and reliability scores for article.

NELA toolkits does not have any class, so we will directly use its function to fit in our functionality.

'''

from NELA.credibility_toolkit import parse_text
import math


class NELAdapter:

    def __init__(self, article_title, article_content):
        # decode title and content
        decoded_article_title = article_title.encode("gbk", 'ignore').decode("gbk", "ignore")
        decoded_article_content = article_content.encode("gbk", 'ignore').decode("gbk", "ignore")
        self.NELA = parse_text(decoded_article_title, decoded_article_content)


    def scale_factor(self, value):
        new_value = value * 2 - 1
        if new_value < 0:
            return 0
        return new_value

    def get_reliability_score(self):
        '''
        The higher score mean more reliable writing
        :return: reliability score of one article based on NELA
        '''
        for item in self.NELA:
            if item["name"] == "fake_filter":
                return self.scale_factor(item["result"][1][1])

    def get_bias_score(self):
        '''
        The higher score mean more bias writing
        :return: bias score of one article based on NELA
        '''
        for item in self.NELA:
            if item["name"] == "bias_filter":
                return self.scale_factor(item["result"][0][1])

