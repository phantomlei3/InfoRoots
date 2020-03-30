'''
NELAdapter is designed to use NELA toolkit library through Adapter Pattern Design
The NELA toolkit has a chaotic structure, but we need its functionality in the compatible way
to generate bias scores and reliability scores for article.

NELA toolkits does not have any class, so we will directly use its function to fit in our functionality.

'''

from NELA.credibility_toolkit import parse_text


class NELAdapter:

    def __init__(self, article_title, article_content):
        self.NELA = parse_text(article_title, article_content)

    def get_reliability_score(self):
        '''
        The higher score mean more reliable writing
        :return: reliability score of one article based on NELA
        '''
        for item in self.NELA:
            if item["name"] == "fake_filter":
                return item["result"][1][1]

    def get_bias_score(self):
        '''
        The higher score mean more bias writing
        :return: bias score of one article based on NELA
        '''
        for item in self.NELA:
            if item["name"] == "bias_filter":
                return item["result"][1][1]

