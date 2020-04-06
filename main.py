from Testing.test_article import *
from Testing.test_authorCard import *

if __name__ == '__main__':


    test_urls = [
        "https://www.nytimes.com/2020/02/17/world/asia/coronavirus-westerdam-cambodia-hun-sen.html?action=click&module=Top%20Stories&pgtype=Homepage",
        "https://www.sfchronicle.com/business/article/SF-expects-record-number-of-cruise-ships-in-2020-15063202.php",
        "https://www.latimes.com/world-nation/story/2020-02-17/la-na-austin-texas-california-homeless"
    ]

    test_author_urls = [
        "https://www.nytimes.com/by/hannah-beech",
        "https://www.sfchronicle.com/author/shwanika-narayan/"
    ]

    # test_profile_article()
    test_profile_author()
