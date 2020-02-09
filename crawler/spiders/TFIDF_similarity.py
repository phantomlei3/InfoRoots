from nltk.tokenize import RegexpTokenizer
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
from gensim import models
from gensim import corpora
from gensim import similarities


def get_tokens(text):
    lowers = text.lower()    # remove the punctuation
    tokenizer = RegexpTokenizer(r'\w+')
    tokens = tokenizer.tokenize(lowers)
    # remove irrelevant stop words
    filtered_tokens = [w for w in tokens if not w in stopwords.words('english')]
    return filtered_tokens

def stem_tokens(tokens):
    stemmer = PorterStemmer()
    stemmed = []
    for item in tokens:
        stemmed.append(stemmer.stem(item))
    return stemmed

# @requires two variables:
#   documents contain multiple contexts to test its similarities source
#   context is just one context being tested by context in documents
# @returns a list of (paragraph_index, similarity_score)
def similarity_query(documents, context, sorted_score=True):
    texts = [stem_tokens(get_tokens(document)) for document in documents]

    dictionary = corpora.Dictionary(texts)
    corpus = [dictionary.doc2bow(text) for text in texts]

    # tfidf = models.TfidfModel(corpus)
    # I change the model here because TFIDF cannot cope with one paragraph case since its equations.
    # I change it temporarily to LSI
    tfidf = models.LsiModel(corpus, id2word=dictionary, num_topics=2)
    corpus_tfidf = tfidf[corpus]

    context_bow = dictionary.doc2bow(stem_tokens(get_tokens(context)))
    context_tfidf = tfidf[context_bow]

    # sims contain (paragraph_index, score)
    index = similarities.MatrixSimilarity(corpus_tfidf)
    sims = index[context_tfidf]

    # the return result can be in the order of score or in the order of index
    if sorted_score:
        sims = sorted(enumerate(sims), key=lambda item: -item[1])
    else:
        sims = sorted(enumerate(sims), key=lambda item: item[0])

    return sims



# testing
if __name__ == '__main__':
    context = '''The majority of the carbon emission reduction pledges for 2030 that 184 countries made under the Paris Agreement aren't nearly enough to keep global warming well below 3.6 degrees Fahrenheit (2 degrees Celsius). Some countries won't achieve their pledges, and some of the world's largest carbon emitters will continue to increase their emissions, according to a panel of world-class climate scientists. Their report, "The Truth Behind the Paris Agreement Climate Pledges," warns that by 2030, the failure to reduce emissions will cost the world a minimum of $2 billion per day in economic losses from weather events made worse by human-induced climate change. Moreover, weather events and patterns will hurt human health, livelihoods, food, and water, as well as biodiversity. On Monday, November 4, the Trump Administration submitted a formal request to officially pull the United States out of the 2015 Paris Agreement next November. Every nation in the world has agreed "to undertake ambitious efforts to combat climate change," according to language in the pact. "Countries need to double and triple their 2030 reduction commitments to be aligned with the Paris target," says Sir Robert Watson, former chair of the Intergovernmental Panel on Climate Change and co-author of the report that closely examined the 184 voluntary pledges under the Paris Agreement. "We have the technology and knowledge to make those emissions cuts, but what's missing are strong enough policies and regulations to make it happen," Watson says in an interview. "Right now the world is on a pathway to between 3 and 4 degrees C (5.5 and 7F) by the end of the century." That pathway risks triggering natural feedbacks such as massive thawing of permafrost or widespread forest die-offs, which could lead to additional uncontrollable warming. Scientists have called this the Hothouse Earth scenario, where sea levels rise 30 to 200 feet (10 to 60 meters) and large parts of the planet become uninhabitable. Changing that future requires reaching the Paris Agreement climate target of well below 2 degrees C. Global emissions need to be halved by next decade and net-zero by mid century, says energy economist Nebojsa Nakicenovic, former CEO of the International Institute for Applied System Analysis (IIASA) in Austria. However, the report's analysis of the 184 pledges for 2030 found that almost 75 percent were insufficient. In fact, the world's first and fourth biggest emitters, China and India, will have higher emissions in 2030. The U.S. is the second largest and its pledge is too low. It's also in doubt, given the Trump Administration's withdrawal from the accord. Russia, the fifth largest emitter, hasn't even bothered to make a pledge. Only the European Union, the third largest emitter, pledged to reduce emissions by at least 40 percent by 2030 and is expected to reach a near 60 percent reduction. The beauty of this report is that it very easy to see which countries are leading and which are lagging, says Watson. "We're already experiencing big impacts from climate change. Waiting to act just locks us into higher temperatures and worsening impacts," he says. (See a report card on which countries are reaching their climate targets.) The report is published by the Universal Ecological Fund, a nonprofit that focuses on providing accessible information on climate science in the hopes of inspiring people to push for climate action. It provides "yet another solid piece of science-based evidence to justify" calls by the public for greater action by governments and businesses, says climate scientist Bill Hare of Berlin-based Climate Analytics. Hare wasn't involved in the report but is a contributor to the Climate Action Tracker, which does scientific analysis of pledges and climate policies. Hare notes that poorer nations cannot make deep emission cuts without the long-promised funding and technical support promised by the world's rich nations. Watson agrees, saying industrialized nations have largely caused the climate problem and must support less-developed countries. "We need everyone on board to solve this," he says. All countries need to step up, accept that global emissions must reach net zero by 2050 and take very large steps to make it happen, says Niklas Hohne of the NewClimate Institute for Climate Policy and Global Sustainability in Germany. Stepping up means major improvements in energy efficiency, while closing 2,400 coal plants and replacing them with renewables within the next decade. This is not only possible; it would be cost-effective. But 250 new coal power plants are under construction around the world, the report found. "Leaders need to adopt new policies to close coal-fired power plants and promote renewable and carbon-free power sources," says James McCarthy, professor of oceanography at Harvard University. Current government efforts will not substantially slow climate change, McCarthy says in a statement. A global climate emergency This widespread failure to act on the existential threat posed by climate change has prompted more than 11,000 scientists from 153 countries to sign a "World Scientists' Warning of a Climate Emergency" declaration. Published independently of the climate pledge report, the declaration begins: "Scientists have a moral obligation to clearly warn humanity of any catastrophic threat and 'tell it like it is.'" Published today as a paper in the journal Bioscience, it includes six critical steps to lessen the worst impacts of climate change and 29 "vital signs" to track progress. These vital signs are in the form of graphs that document various human activities over the last 40 years that have contributed to climate change, such as energy consumption, deforestation, and air transportation. The graphs also include the resulting climate impacts, such as rising levels of CO2 and sea ice loss. Avoiding "untold human suffering" requires an immense increase in the scale of emissions reductions, the declaration warns. That includes reducing meat consumption and food waste, as well as massively increasing energy efficiency through renewable energy. The climate solutions in the paper aren't new, acknowledges lead author William Ripple of Oregon State University. But by listing the solutions as a set of six crucial steps, along with "simple graphical indicators showing where we were 40 years ago and how things have changed," the authors hope these will be easily understood by anyone, says Ripple. "Citizens everywhere need to become more politically involved and policymakers need to make dramatic improvements in their climate action plans," he says. The public is becoming more involved; millions participated in September's global climate strikes. Many countries, states, and provinces, cities, and businesses are responding to those demands for increased action on climate, he says. The 2020 U.S. election will be about climate change, Ripple says. "It already is." U.S. wants climate action "Abandoning the Paris Agreement is cruel to future generations," says Andrew Steer, President &amp; CEO of the World Resources Institute about the Trump Administration's move to officially pull the U.S. out of the agreement. The U.S. will lose out on the jobs and much stronger economy that a low-carbon future will bring, Steer says in a statement. The Trump Administration is sending the world "a catastrophic message in a moment of great urgency," says May Boeve, Executive Director of 350.org, a large grassroots activist group. "...a majority of people in the United States understand the need to address this crisis head on," Boeve says in a statement. An August 2019 poll found that 71 percent of U.S. voters want the federal government to do more to address climate change. A similar majority believe it will have a positive impact on the economy and jobs. A year from now--Nov 4, 2020--the U.S. will be officially out of the Paris Agreement. That is one day after the presidential election. The U.S. could re-enter the pact within 30 days of a request to the United Nations.'''
    documents = ['Global governments plan to produce 120 percent more fossil fuels by 2030, drastically at odds with the 2.7 degrees Fahrenheit (1.5 degrees Celsius) warming limit they all agreed to under the 2015 Paris Climate Agreement. All major fossil fuel-producing nations--including the United States, China, Russia, Saudi Arabia, India, Canada, and Australia--have ambitious plans to increase production, according to a new report by leading research organizations and the United Nations.']

    print(similarity_query(documents, context, False))




