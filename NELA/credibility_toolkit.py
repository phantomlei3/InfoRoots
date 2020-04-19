import os
from threading import Thread, Lock

import NELA.Compute_all_features as Compute_all_features
import NELA.feature_selector as feature_selector
import NELA.fake_filter as fake_filter
import NELA.bias_filter as bias_filter
import NELA.subjectivity_classifier as subjectivity_classifier
from collections import OrderedDict

basepath = os.path.dirname(os.path.realpath(__file__))
featurepath = os.path.join(basepath, "out")

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

def parse_text(title, text):
  info = OrderedDict()
  info["source"] = "unknown"

  info["title"] = title
  info["text"] = text

  parse_info(info)

  return info["classifiers"]

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



  #feature creation and selection
  Compute_all_features.start(info["title"], info["text"], info["source"], featurepath)
  feature_selector.feature_select(featurepath)

  #classifiers
  # Set to threading
  threads = []

  threads.append(Thread(target=add_classifier, args=(info, "fake_filter", fake_filter.fake_fitler, featurepath,)))
  threads.append(Thread(target=add_classifier, args=(info, "bias_filter", bias_filter.bias_fitler, featurepath,)))
  # threads.append(Thread(target=add_classifier, args=(info, "subjectivity_classifier", subjectivity_classifier.subjectivity, info["title"], info["text"],)))

  for t in threads:
    t.daemon = True
    t.start()

  for t in threads:
    t.join()
