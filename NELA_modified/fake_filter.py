import warnings
warnings.filterwarnings("ignore")

from sklearn import preprocessing
import pickle
import os
import numpy as np

DIRNAME = os.path.dirname(__file__)

def fake_fitler(featurepath):
    #print "Predicting reliability"
    with open(os.path.join(featurepath, "fake_features.csv")) as data:
        data.readline()
        x_test = data.readline().strip().split(",")

    X_test = []
    x_test = tuple([float(x) for x in x_test])
    x_test = np.array(x_test).reshape(1, -1)

    # load the model from disk
    loaded_model = pickle.load(open(os.path.join(DIRNAME, 'resources', 'FAKE_FILTER_MODEL.sav'), 'rb'), encoding="latin1")

    styles = ["Unreliable Writing Style", "Reliable Writing Style"]
    result = loaded_model.predict_proba(x_test)[0]

    # combine results with writing styles list
    result = [(styles[i], x) for i,x in enumerate(result)]


    print (result)

    return result
