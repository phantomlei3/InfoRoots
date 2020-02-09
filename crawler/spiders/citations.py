import scrapy
import json
from crawler.spiders.clean_author import *
import unidecode


class CitationSpide(scrapy.Spider):
    name = "citations"

    def __init__(self, **kw):
        super(CitationSpide, self).__init__(**kw)
        self.url = kw.get('url')
        self.max_depth = kw.get('max_depth')

    def start_requests(self):
        # create output file
        open('result.json', 'w')
        open('info.json', 'w')

        yield scrapy.Request(url=self.url, callback=self.parse,
                             meta={'parent': 'None', 'depth': 0, "prevp": None, "citation_index": None, "cited_words": None})

    # helper function
    # remove social media share links and redundant links
    def remove_share(self, para_cits):
        clean_citations = list()
        for cits in para_cits:
            clean_citation = list()
            for link, cited_words in cits:
                if "facebook?linkurl" in link:
                    continue
                if "twitter?linkurl" in link:
                    continue
                if "twitter.com" in link:
                    continue
                if ".facebook.com" in link:
                    continue
                if "amazon.com" in link:
                    continue
                if "google_plus?linkurl" in link:
                    continue
                if "share" in link:
                    continue
                # not a format of url
                if "http" not in link:
                    continue
                # avoid videos
                if "youtube" in link:
                    continue
                clean_citation.append((link, cited_words))
            clean_citations.append(clean_citation)

        return clean_citations


    # get all paragraph html class from response
    # each paragraph contains text and its citations
    # return a list of [ "paragraph text", [citations] ]
    def get_paragraph_from_response(self, content, profile):
        # get a list of paragraphs
        paragraphs = content.xpath(profile["paragraphs"]).extract()

        # create tags for regex and get the cited words
        citation_tag = re.compile(r'<a.*?href=\"(.*?)\".*?>(.*?)</a>')

        # clean up paragraphs by removing profile["paragraph"] html tags
        results = list()

        for paragraph in paragraphs:
            # remove twice for re weird bugs
            clean_paragraph = re.sub(r'<.*?>', '', paragraph).strip()

            # unicode converison
            clean_paragraph = unidecode.unidecode(clean_paragraph)
            citations = re.findall(citation_tag, paragraph)
            new_citations = list() # clean up cited words
            for link, cited_words in citations:
                new_cited_words = re.sub(r'<.*?>', '', cited_words).strip()
                new_cited_words = unidecode.unidecode(new_cited_words)
                new_citations.append((link, new_cited_words))
            results.append((clean_paragraph, new_citations))

        return results

    # write json result to target file
    def write_json(self, file_path, json_data):
        with open(file_path, 'a') as output_file:
            output_file.write(json.dumps(json_data))
            output_file.write('\n')


    def parse(self, response):

        # verify the URL by Profiles.json
        profiles = json.load(open("Profiles_v2.json", "r"))
        response_profile = None
        for domain, profile in profiles.items():
            if domain in response.url:
                response_profile = profile
                break

        # if it is a pdf file, treat it as normal nodes
        pdf_file_tag = False
        if "pdf" in response.url:
            pdf_file_tag = True

        # If not in profiles, return
        if response_profile is None:
            return None

        # verify the URL by checking if content existed
        content = response.css(response_profile["content"])
        # if content does not exist just treated it as a normal nodes
        # Save node data and link information but without processing any citations
        # and return
        if len(content) == 0 or pdf_file_tag:
            title = response.css("title::text").get()
            # open output file to save node data
            article_data = dict()
            article_data['parent'] = response.meta['parent']
            article_data['self'] = response.url
            article_data['authors'] = []
            article_data['organization'] = response_profile['organization']
            article_data['title'] = unidecode.unidecode(title)
            self.write_json('result.json', article_data)

            citation_index = response.meta["citation_index"]
            # save link information
            link_data = dict()
            link_data['parent'] = response.meta['parent']
            link_data['child'] = response.url
            link_data['cited_words'] = response.meta['cited_words']
            link_data['parent_sims'] = [(response.meta["prevp"][citation_index], 1.0)]  # give paragraphs with default score 1.0
            link_data['child_sims'] = []

            self.write_json('info.json', link_data)

            return None

        # extract paragraph contents w/ citations from article
        paragraphs_with_cits = self.get_paragraph_from_response(content, response_profile)
        documents = [document for document, cits, in paragraphs_with_cits]
        para_citations = [cits for document, cits, in paragraphs_with_cits] # citations for each paragraph (can be empty)
        # clean citation
        para_citations = self.remove_share(para_citations)

        # extract authors/title/organization
        authors = response.css(response_profile["authors"]).extract()
        authors = clean_authors(authors) # clean authors
        title = response.css("title::text").get()

        # open output file to save node data
        article_data = dict()
        article_data['parent'] = response.meta['parent']
        article_data['self'] = response.url
        article_data['authors'] = authors
        article_data['organization'] = response_profile['organization']
        article_data['title'] = unidecode.unidecode(title)
        self.write_json('result.json', article_data)

        # IMPORTANT FEATURE SECTION BELOW:
        # Generate link information between source and its cited sources if it is not the starter source
        depth = response.meta['depth']
        prev_documents = response.meta["prevp"]
        if prev_documents is not None:
            # save link information
            link_data = dict()
            link_data['parent'] = response.meta['parent']
            link_data['child'] = response.url
            link_data['cited_words'] = response.meta['cited_words']
            link_data['parent_sims'] = [(prev_documents[index], str(score)) for index, score in parent_sims]  # give paragraphs
            link_data['child_sims'] = [(documents[index], str(score)) for index, score in child_sims]  # give paragraphs
            self.write_json('info.json', link_data)

            # Important: continue search for more citations in child_sims if depth not reached
            if depth < self.max_depth:
                sims_documents = [d for d, _ in link_data['child_sims']]
                for i, datum in enumerate(sims_documents):
                    index = documents.index(datum)
                    for url, cited_words in para_citations[index]:
                        yield scrapy.Request(url=url, callback=self.parse,
                                             meta={'parent': response.url, 'depth': depth + 1, "prevp": sims_documents,
                                                   "citation_index": i, "cited_words": cited_words})

        # starter source: search all links in citations
        else:
            for i, cits in enumerate(para_citations):
                for url, cited_words in cits:
                    yield scrapy.Request(url=url, callback=self.parse,
                            meta={'parent': response.url, 'depth': depth + 1,
                                  "prevp": documents, "citation_index": i, "cited_words": cited_words})







