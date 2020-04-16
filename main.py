from Testing.test_article import *
from Testing.test_authorCard import *
from Testing.test_publisherCard import *
from Testing.test_infoMediator import *
from infoMediator import infoMediator
import hashlib


if __name__ == '__main__':


    #test_profile_author()

    server = infoMediator()

    server.start()


    #url="www.nytimes.com"

    #print(str(hashlib.md5(url.encode()).hexdigest()))
