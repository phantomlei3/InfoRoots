from article import article

def test_profile_article():
    url = "https://www.nytimes.com/2020/02/17/world/asia/coronavirus-westerdam-cambodia-hun-sen.html?action=click&module=Top%20Stories&pgtype=Homepage"
    test_article = article(url)
    result = test_article.get()
    print(result)

def test_non_profile_article():
    pass

