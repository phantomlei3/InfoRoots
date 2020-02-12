import re

def clean_authors(authors):
    new_authors = set()
    name_pattern = re.compile(r'[A-Za-z]{2,30}( [A-Za-z]{2,30})?')

    for author in authors:
        if "Written By" in author:
            continue
        if "By" in author:
            new_authors.add(author.replace("By", "").strip())
        elif re.findall(name_pattern, author.strip()):
            new_authors.add(author.strip())

    return list(new_authors)