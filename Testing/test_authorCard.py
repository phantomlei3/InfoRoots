from article import article
from authorCard import authorCard

def test_profile_author():
    url = "https://www.nytimes.com/2020/02/17/world/asia/coronavirus-westerdam-cambodia-hun-sen.html?action=click&module=Top%20Stories&pgtype=Homepage"
    test_article = article(url)
    article_result = test_article.get()
    test_author = authorCard(article_result["article_id"], article_result["author_page_link"],
                             article_result["profile"], article_result["author_name"])
    print(test_author.get())


def test_non_profile_author():
    pass