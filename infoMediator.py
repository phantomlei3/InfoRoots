import zmq

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


        self.URL_status = False
        self.URL = None

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
        @ send JSON String"{article_title, article_name, article_content, author_name, publisher_name}" 
        @ send "None"  if there is no URL processed first.
        '''
        if command == "Article":
            article_cotent = self.get_article_content()
            self.socket.send(article_cotent)

            return

        '''
        request for getting author's cards
        @ wait for command: "Author card"
        @ send JSON String "{author_name, author_introduction, author_reliability_score, author_bias_score}"
        @ send "None" if there is no URL processed first.
        '''
        if command == "Author card":
            author_card = self.get_author_card()
            self.socket.send(author_card)

            return


        '''
        @ send "Error" if command is not recognized 
        '''
        self.socket.send("Error")

        return





    def process_URL(self):
        return True


    def get_article_content(self):
        pass


    def get_author_card(self):
        pass

