import zmq
import json
from article import article
from authorCard import authorCard

class infoMediator:
    '''
     Mediator Design Pattern:
     class infoMediator is the core mediator to
        handle client(URL) and producer(author/publisher/citations crawling class)
    '''

    def __init__(self):

        # TCP connection on local host 5555
        context = zmq.Context()
        self.socket = context.socket(zmq.REP)
        self.socket.bind("tcp://127.0.0.1:5555")

        # status indicator
        self.URL_status = False
        self.URL = None

        # Information variables
        self.article_content = None
        self.author_card = None

    def start(self):
        '''


        :return:
        '''
        while(True):
            command = self.socket.recv()
            self.control_center(command)


    def control_center(self, command):
        '''

        :param command: a string, command messsage from the server
        '''

        '''
        request for processing user's search query: Article URL
        @ wait for command: "URL (Article URL)" eg "URL www.google.com"
        @ send "Okey" if URL is accessible and processed by crawler
        @ send "Failed" if URL is not accessible or crawling system faile
        '''
        if "URL" in command:
            self.URL = command.split(" ")[1]
            self.process_URL()
            if self.URL_status:
                self.socket.send("Okey")
            else:
                self.socket.send("Failed")

            return
        '''
        request for getting article content
        @ wait for command: "Article"
        @ send JSON String"{article_title, article_content, author_name, publisher_name}" 
        @ send "None"  if there is no URL processed first.
        '''
        if command == "Article" and self.URL_status:
            article_cotent = self.get_article_content()
            self.socket.send(article_cotent)

            return

        '''
        request for getting author's cards
        @ wait for command: "Author card"
        @ send JSON String "{author_name, author_introduction, author_reliability_score, author_bias_score}"
        @ send "None" if there is no URL processed first or failed to crawl the information
        '''
        if command == "Author card" and self.URL_status:
            author_card = self.get_author_card()
            self.socket.send(author_card)

            return


        '''
        @ send "Error" if command is not recognized 
        '''
        self.socket.send("Error")

        return


    def process_URL(self):
        '''
        Set up article class to process and store information in self.article_content
        set up author card class to process and store in self.author_card

        :return: set self.URL_status to True if the article is crawled successfully
                    Otherwise, set self.URL_status to False
        '''

        # set up article class
        new_article = article(self.URL)
        article_result = new_article.get()
        if article_result is not None:
            self.URL_status = True
            # store article information to self.article_content
            self.article_content = dict()
            self.article_content["article_title"] = article_result["article_title"]
            self.article_content["article_content"] = article_result["article_content"]
            self.article_content["author_name"] = article_result["author_name"]
            self.article_content["publisher_name"] = article_result["publisher_name"]

            # set up author card class
            new_author_card = authorCard(article_id=article_result["article_id"],
                                         author_page_link=article_result["author_page_link"],
                                         profile=article_result["profile"],
                                         author_name=article_result["author_name"])
            author_result = new_author_card.get()

            # store author information to self.author_card
            if author_result is not None:
                self.author_card = dict()
                self.author_card["author_name"] = author_result["author_name"]
                self.author_card["author_introduction"] = author_result["author_intro"]
                self.author_card["author_reliability_score"] = author_result["author_reliability"]
                self.author_card["author_bias_score"] = author_result["author_bias"]
            else:
                self.author_card = None
        else:
            self.article_content = dict()
            self.URL_status = False


    def get_article_content(self):
        '''
        return make article_content into a json string
        :return: a json string
        '''
        if self.article_content is not None:
            return json.dumps(self.article_content)
        else:
            return "None"


    def get_author_card(self):
        '''

        :return: a json string of self.author_card if crawling and analysis are succesful
                    Otherwise return None
        '''
        if self.author_card is not None:
            return json.dumps(self.author_card)
        else:
            return "None"

