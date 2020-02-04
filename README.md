# InfoRoots
A Software Design & Documentation Project at RPI 
### Team Members
- Siwen Zhang
- Joseph Om
- Jianing Lin
- Lei Luo

### Vision Statements
##### Executive Summary
Fake news is prevalent over the internet, especially on climate change and vaccinations. The online average readers do not have enough time and knowledge to identify false information.  InfoRoots uses automated information retrieval to fight against fake news and misinformation. Our web platform facilitates users to investigate online news and articles by providing analytic information about authors, publishers, and contents. By using InfoRoots, users will make accurate judgments on false information with small effort. 

##### Market Potential
Fact-checking is the traditional approach to intervene in fake news. Fact-checking websites provide analytic reviews of news and factual claims by using journalism experts. [PolitiFact](https://www.politifact.com/), [Snopes](https://www.snopes.com/), and [FactCheck.org](https://www.factcheck.org/) are three mainstream fact-checking organizations, providing fact-checked articles on their websites. Instead of focusing on articles, [NewsGuard](https://www.newsguardtech.com/) generates professional reviews of online news sources and publishers. Users can use [NewsGuard](https://www.newsguardtech.com/)’s browser extension to check reviews of publishers when reading news and articles. Since professional fact-checking requires a large amount of time, they cannot cover every claim and article over the internet. Crowdsourcing and machine learning are relatively new approaches to this market. [Our.news](https://our.news/) is developing browser extension to provide readers both publishers’ information and crowdsourcing reviews. It is not effective due to a small user group so far. InfoRoots will be an innovative business based on machine learning in this market.

##### Stakeholders
InfoRoots has two groups of project stakeholders: team instructors and team members. Team instructors consist of one overall supervisor and several teaching assistants. In InfoRoots’ team instructors, John Sturman is the overall supervisor. Charly Huang and Vaishnavi Neema are two teaching assistants. Their responsibility is to facilitate InfoRoots to successfully develop and launch to its market. As an experienced project manager, John Sturman offers courses on the design and development of InfoRoots to team members. Two teaching assistances provide feedback to the deliverables of InfoRoots. 

In team members, there are four undergraduate students. They are Siwen Zhang, Joseph Om, Jianing Lin, and Lei Luo. Under the Scrum framework, Lei Luo functions as both the project owner and Scrum Master. All team members function as designers and programmers to develop the InfoRoots web platform.


#####Major Features
InfoRoots web platform is designed to investigate online articles. When online readers enter one article link on InfoRoots, they will see three major features that can help them determine whether the contents in the article are false. 

The first feature is the authors’ information. It presents not only the background information of authors from Wikipedia sources but also reliability scores measured by our machine learning algorithm. The algorithm produces scores based on examining recent articles written by the authors. 

The second feature is the publisher’s information. It offers the professional publisher ratings from non-partisan fact-checking organizations, such as NewsGuard. Besides, it also presents the ratings of other publishers that generate similar content. Our users can evaluate the credibility of information by comparing different publishers.

The third feature is the citation and content analysis. The analysis system pinpoints all citations in the original article and extracts relevant paragraphs from these citations. The relevant paragraphs are shown to readers when they click at each citation. As our users read through the article on InfoRoots, they can check two reliability factors. The first one is whether the cited information came from reliable publishers. The second one is whether the content in the citations is presented accurately in the original article. 


#####Major Risks
InfoRoots has two potential risks. The first risk is related to the completion of InfoRoots. Each proposed feature requires a certain level of knowledge on machine learning and data scraping. Since all team members have little experience in developing major features mentioned above, they will spend the majority of their time exploring and researching phase. The final deliverable might contain uncompleted features. Shorter work cycles can mitigate this risk as it allows agile reviews and revises on developing features. 

The second risk is that all proposed features require a lot of computation powers. To test major features, InfoRoots might spend a lot of money on subscribing to cloud computing services. If one of the major features costs expensive computing resources, the team might revise the expensive feature in order to save money. That is, three major features are highly subjected to changes.


