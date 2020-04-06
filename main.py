from Testing.test_article import *
from Testing.test_authorCard import *
from infoMediator import infoMediator

if __name__ == '__main__':

    server = infoMediator()

    server.start()
