from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from multiprocessing import Process
import json

# thread function for citations_crawl
# crawl all citations
def thread_crawl(url, max_depth):
    process = CrawlerProcess(get_project_settings())
    process.crawl('citations', url=url, max_depth=max_depth)
    process.start()

# Helper function for d3_output_json
# Process similarity information from info.json
# Similarity information is to provide information to each links in the graph
# @returns a dictionary that contains the following structure
# { source index: [{"target":target index,
#                   "parent_sims": parent similar paragraphs,
#                   "child_sims": child similar paragraphs
#                   }, ....]
# ...}
def process_info_json(nodes_name):
    result = dict()
    with open("info.json") as input_file:
        for line in input_file:
            if line == "":
                continue
            datum = json.loads(line)
            # get corresponding index from nodes_name and info datum
            source = nodes_name.index(datum["parent"])
            target = nodes_name.index(datum["child"])
            # create new list if source not existed in result before
            if str(source) not in result.keys():
                result[str(source)] = list()
            # info datum is converted datum put in the list
            info_datum = dict()
            info_datum["target"] = target
            info_datum["parent_sims"] = datum["parent_sims"]
            info_datum["child_sims"] = datum["child_sims"]
            info_datum["cited_words"] = datum["cited_words"]
            result[str(source)].append(info_datum)
    return result


# convert input json data (both result and info json) file folder to d3 format
def d3_output_json(display_author=True, display_organization=True):
    result = dict()
    result["nodes"] = list()
    result["links"] = list()

    # create dictionary to store result.json
    data = dict()
    index = 0
    with open("result.json") as input_file:
        for line in input_file:
            if line == "":
                continue
            datum = json.loads(line)
            data[str(index)] = datum
            index += 1

    # create Nodes based on data
    # prepare link information for creating
    # Type assign:
    # Main Article: 0
    # Cited Article: 1
    # Author: 2
    # Organization: 2
    link_info = list()
    for index, datum in data.items():
        # avoid repetitive nodes
        repetitive_check = [existed["name"] for existed in result["nodes"]]
        if datum["self"] in repetitive_check:
            continue
        # add new node
        node = dict()
        node["name"] = datum["self"]
        node["title"] = datum["title"]
        if datum["parent"] == "None":
            node["group"] = 0
        else:
            node["group"] = 1
        result["nodes"].append(node)

        # add link between parent and self
        if datum["parent"] != "None":
            link_info.append((datum["parent"], datum["self"], 1.0))

        if display_author:
            # add link info between new node and author node and organization node
            # create author node and organization node (avoid repetitive node)
            for author in datum["authors"]:
                link_info.append((datum["self"], author, 0.0))
                if author not in repetitive_check:
                    author_node = dict()
                    author_node["name"] = author
                    author_node["title"] = author
                    author_node["group"] = 3
                    result["nodes"].append(author_node)

        if display_organization:
            link_info.append((datum["self"], datum["organization"], 0.0))
            if datum["organization"] not in repetitive_check:
                organization_node = dict()
                organization_node["name"] = datum["organization"]
                organization_node["title"] = datum["organization"]
                organization_node["group"] = 2
                result["nodes"].append(organization_node)


    # create links based on link info
    # for author node and organization node: give weight 0.0
    # for citations node: give weight 1.0 + ### (min(sim_scores in parent_sims)) ### NOT IMPLEMENTED
    node_names = [existed["name"] for existed in result["nodes"]]
    for source, target, weight in link_info:
        link = dict()
        link["source"] = node_names.index(source)
        link["target"] = node_names.index(target)
        link["weight"] = weight
        result["links"].append(link)

    # visualization json files
    with open("static/visualization.json", "w") as outfile:
        json.dump(result, outfile)

    # link sim information files
    sim_result = process_info_json(node_names)
    with open("static/similarity_info.json", "w") as outfile:
        json.dump(sim_result, outfile)


# crawl all citations of url
# generate d3 data json file
def citations_crawl(url, max_depth):
    p = Process(target=thread_crawl, args=(url, max_depth))
    p.start()
    p.join()


# print the sum of two variables
def fool(a, b):
    '''
    :param a, a integer
           b, a integer

    '''

    print(a+b)



if __name__ == '__main__':
    citations_crawl("https://www.nationalgeographic.com/science/2019/11/earth-tipping-point/#close", 2)
    d3_output_json(True, False)