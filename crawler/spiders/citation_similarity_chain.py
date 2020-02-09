from crawler.spiders.TFIDF_similarity import *
import sys
'''
Author: Lei Luo
Idea: I want to compare content similarity between two sources back and forth to find 
        relevant paragraphs between two sources. I will call the method "back and forth similarity".
Description: Helper functions for citations crawler
'''

# @requires two variables:
#   parent_paras: a list of paragraphs from source A
#   child_paras : a list of paragraphs from source B
#   citations_index: the index of citations in parent_paras from source A to source B
# @returns two variables:
#   parent_sims: a list of (paragraphs index, sim scores) in source A that are content-similar to %child_paras%
#   child_sims: a list of (paragraphs index, sim scores) in source B that are content-similar to %parent_sims%
# For the design simplicity and user experience, the return paragraphs should be in sequential paragraphs in original context
def back_and_forth_similarity(parent_paras, child_paras, citations_index):

    # step 1: find relevant paragraphs in parent_paras to child_paras
    child_context = " ".join(child_paras)
    parent_sims = None

    sims = similarity_query(parent_paras, child_context, False)
    parent_sims = relevant_sequential_paragraphs(sims, citations_index)


    # step 2: find relevant paragraphs in child_paras to parent_sims
    temp_paras = [parent_paras[index] for index, score in parent_sims]
    parent_sims_context = " ".join(temp_paras)
    sims = similarity_query(child_paras, parent_sims_context, False)
    # use the top score similarity index as citations_index for child_sims
    temp_index = sorted(sims, key=lambda item: -item[1])[0][0]
    child_sims = relevant_sequential_paragraphs(sims, temp_index)


    return parent_sims, child_sims

# Helper function
# @requires two variables
#   sims: its similarity query from TFIDF
#   citations_index: the index of citations in parent_paras from source A to source B
# @returns a list of relevant paragraphs (paragraphs index, sim scores) in sequential order
def relevant_sequential_paragraphs(sims, citations_index):
    relevant_results = list()

    decresed_sim_threshold = 0.10 # Arbitrary number
    limit_length = 2 # maximum length of relevant paragraphs

    sims_score = [score for _, score in sims]

    # use source score as one utility for similarity
    source_score = sims_score[citations_index]

    # go up for more relevant paragraphs
    for index in range(citations_index-1, -1, -1):
        # if score is larger, directly add
        if sims_score[index] >= source_score:
            relevant_results.append(sims[index])
        # make sure decreased similarities percentage is lower than decresed_sim_threshold
        else:
            decreased = (source_score - sims_score[index]) / source_score
            if decreased < decresed_sim_threshold:
                relevant_results.append(sims[index])
            else:
                break # once found large gap in similarity, it is the break point

        # reach length, return directly
        if len(relevant_results) >= limit_length:
            relevant_results.append(sims[citations_index]) # must add self
            return relevant_results

    # add self
    relevant_results.append(sims[citations_index])

    # go down for more relevant paragraphs
    for index in range(citations_index+1, len(sims)):
        # if score is larger, directly add
        if sims_score[index] >= source_score:
            relevant_results.append(sims[index])
        # make sure decreased similarities percentage is lower than 0.25 (Arbitrary number)
        else:
            decreased = (source_score - sims_score[index])/ source_score
            if decreased < decresed_sim_threshold:
                relevant_results.append(sims[index])
            else:
                break # once found large gap in similarity, it is the break point

        # reach length, return directly
        if len(relevant_results) >= limit_length:
            return relevant_results

    return relevant_results
