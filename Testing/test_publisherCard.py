from article import article
from publisherCard import publisherCard


def test_profile_publisher():
    url = "https://www.nytimes.com/2020/02/17/world/asia/coronavirus-westerdam-cambodia-hun-sen.html?action=click&module=Top%20Stories&pgtype=Homepage"
    test_article = article(url)
    article_result = test_article.get()
    test_author = publisherCard(article_result["profile"])
    print(test_author.get())