import sys
import os
import re
import uuid
import time
from threading import Thread, Lock

import Compute_all_features as Compute_all_features
import feature_selector as feature_selector

import fake_filter as fake_filter
#import classifiers.bias_filter as bias_filter
#import classifiers.community_filter as community_filter
#import classifiers.subjectivity_classifier as subjectivity_classifier
#import scraper.url_scraper as scrape
import bulk_scraper as bulk_scraper

#from screenshot import get_screenshot
from collections import OrderedDict
import json

basepath = os.path.dirname(os.path.realpath(__file__))
featurepath = os.path.join(basepath, "out")

'''
urls = [
  "http://mondoweiss.net/2017/10/businesses-hurricane-boycott/"
]
'''

lock = Lock()

def add_classifier(info, name, func, *args):
  result = func(*args)

  lock.acquire()

  if "classifiers" not in info:
    info["classifiers"] = []
    info["cindex"] = OrderedDict()

  info["cindex"][name] = len(info["classifiers"])

  info["classifiers"].append({
    "name":name,
    "result":result
  })

  lock.release()

'''
def parse_url(output, url):
  info = OrderedDict()
  info["url"] = url

  if url:
    try:
      info["title"], info["text"], info["source"] = scrape.scrape(url)
    except:
      print "WARNING: Unable to scrape:", url
      return

  else:
    info["text"] = "FAKE FAKE FAKE Clinton is terrible Mainstream media sucks. The real patriots can see this FRAUD!"
    info["title"] = "BREAKING Fraudulent Clinton Votes Discovered By The Tens Of Thousands, wait until you see this! Those dems are at it again."
    info["source"] = "unknown"

  # Try to get the thumbnail
  #fname = re.sub("[^0-9a-z_]", "", info["title"].replace(" ", "_").lower()[:50]) + ".png"
  #fname = info["source"] + "_" + fname
  #path = os.path.join("web", "static", fname)
  #try:
  #  #if not os.path.isfile(path):
  #  #  get_screenshot(path, url)
  #  info["screenshot"] = os.path.join("static", fname)
  #except:
  #  pass

  parse_info(output, info)
'''

def parse_text(title, text):
  info = OrderedDict()
  #info["url"] = str(uuid.uuid4())
  #info["source"] = "unknown"

  info["title"] = title
  info["text"] = text

  parse_info(info)

def parse_info(info):
  info["title"] = info["title"].strip()
  info["text"] = info["text"].strip()
  info["source"] = info["source"].strip()

  if not info["title"] or not info["text"]:
    raise ValueError("WARNING: Unable to parse: ", info["url"])
    return

  if len(info["text"]) < 100:
    raise ValueError("WARNING: URL text too short: ", info["url"])
    return

  print
  print info["url"]
  print info["title"]
  print info["source"]

  start_time = time.time()

  #feature creation and selection
  Compute_all_features.start(info["title"], info["text"], info["source"], featurepath)
  feature_selector.feature_select(featurepath)

  #classifiers

  if True: # Set to true for threading, false otherwise
    threads = []
    threads.append(Thread(target=add_classifier, args=(info, "fake_filter", fake_filter.fake_fitler, featurepath,)))
    '''
    threads.append(Thread(target=add_classifier, args=(info, "bias_filter", bias_filter.bias_fitler, featurepath,)))
    threads.append(Thread(target=add_classifier, args=(info, "community_filter", community_filter.community_fitler, featurepath,)))
    threads.append(Thread(target=add_classifier, args=(info, "subjectivity_classifier", subjectivity_classifier.subjectivity, info["title"], info["text"],)))
    '''

    for t in threads:
      t.daemon = True
      t.start()

    for t in threads:
      t.join()

  else:
    add_classifier(info, "fake_filter", fake_filter.fake_fitler, featurepath)
    #add_classifier(info, "bias_filter", bias_filter.bias_fitler, featurepath)
    #add_classifier(info, "community_filter", community_filter.community_fitler, featurepath)
    #add_classifier(info, "subjectivity_classifier", subjectivity_classifier.subjectivity, info["title"], info["text"])

  for val in info["classifiers"]:
    print val["name"], ":", val["result"]

  print "Parsing took %.4f seconds" % (time.time() - start_time)
  print
  print info

  #output["urls"].append(info)


def source_test():
  source_result_dict = {}
  data = bulk_scraper.bulk_scraper()
  for key in data.keys():
    fake_source_results = []
    bias_source_results = []
    for source, article, url in data[key]:
      try:
        Compute_all_features.start(article[0], article[1], article[2], featurepath)
      except ValueError:
        continue
      feature_selector.feature_select(featurepath)
      f = fake_filter.fake_fitler(featurepath)
      b = bias_filter.bias_fitler(featurepath)
      fake_source_results.append(f[0][0])
      bias_source_results.append(b[0][0])
    reliable_arts = [1 for r in fake_source_results if r == 'Credibile Writing Style']
    unbiased_arts = [1 for r in bias_source_results if r == 'UnBiased Writing Style']
    per_reliable = float(sum(reliable_arts)) / len(fake_source_results)
    per_unbiased = float(sum(unbiased_arts)) / len(bias_source_results)
    source_result_dict[key] = (source, per_reliable, per_unbiased, url)
  return source_result_dict

# Main
if __name__ == "__main__":
    '''
  output = OrderedDict()
  json_filename = os.path.join("static", "output.json")

  if len(sys.argv) > 1 and os.path.isfile(sys.argv[1]):
    with open(sys.argv[1], 'r') as f:
      urls = []
      for url in f.readlines():
        urls.append(url)

  output["urls"] = []

  for url in urls:
    try:
      parse_url(output, url)
    except Exception as e:
      print e

  with open(json_filename, 'w') as outfile:
    json.dump(output, outfile, indent=2)
    '''
    