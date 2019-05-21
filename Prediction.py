from pyknow import *
import schema
from bs4 import BeautifulSoup
import json
import requests
import time
from random import randint
from textblob import TextBlob


""".declare() is what fires another rule to run"""


class Action(Fact):
    pass

class Company(Fact):
    #"""Company name"""
    name = Field(str, mandatory=True)
    #score = Field(int, default=0, mandatory=False)
    pass

class Results(Fact):
    #price = Field(str, mandatory=True)
    price = Field(schema.Or('up','down'))

class ValidAnswer(Fact):
    answer = Field(str, mandatory=True)

class Prediction(KnowledgeEngine):

    @DefFacts()
    def game_rules(self, is_nerd=False):
        """Declare game rules and valid input keys for the user."""
        self.valid_answers = dict()

        yield Results(price='up')
        yield Results(price='down')
        yield ValidAnswer(answer='AAPL')
        yield ValidAnswer(answer='AMZN')
        yield ValidAnswer(answer='GOOG')


    @Rule()
    def startup(self):
        print("Stock Prediction App:")
        self.declare(Action('get-input'))


    @Rule(Action('get-input'))
    def get_input(self):
        res = input("Enter the desired stock symbol you want to predict\n").upper()
        self.declare(Company(name=res))
        #self.declare(Company(name=res))
    #
    # FUNCTIONS THAT DO THE NECESSARY STEPS TO LOOK UP INFO AND CALCULATE SCORE TO PREDICT STOCK
    #


    @Rule(Company(name='AAPL'))
    def predictAAPL(self):
        
        print("Predicting stock for Apple...")
        print("Looking up necessary stock info")

        # You can put any query you want into the parameter like: "Google stocks" and it'll return relevant articles for that query.
        # We can use this to query for all the necessary information to predict this stock
        query = "Apple"
        print("Querying ", query)
        relevantSummaries = self.scrape_news_summaries(query)

        finalTotalPolarity = 0
        finalTotalSubjectivity = 0
        totalPolarity = 0
        totalSubjectivity = 0
        numLines = 0
        for summary in relevantSummaries:
            wiki = TextBlob(summary)
            print(summary) 
            totalPolarity += wiki.sentiment.polarity
            totalSubjectivity += wiki.sentiment.subjectivity
            numLines += 1 

        finalTotalPolarity += totalPolarity
        finalTotalSubjectivity += totalSubjectivity/numLines
        print ("Sentiment Polarity: ",totalPolarity)
        print ("Sentiment Subjectivity: ",totalSubjectivity/numLines)

        print("\n")

        totalPolarity = 0
        totalSubjectivity = 0
        numLines = 0        
        query = "Apple stocks"
        print("Querying ", query)
        relevantSummaries = self.scrape_news_summaries(query)
        for summary in relevantSummaries:
            wiki = TextBlob(summary)
            print(summary)  
            totalPolarity += wiki.sentiment.polarity
            totalSubjectivity += wiki.sentiment.subjectivity
            numLines += 1 

        finalTotalPolarity += totalPolarity
        finalTotalSubjectivity += totalSubjectivity/numLines
        print ("Sentiment Polarity: ", totalPolarity)
        print ("Sentiment Subjectivity: ",totalSubjectivity/numLines)

        print("\n")

        totalPolarity = 0
        totalSubjectivity = 0
        numLines = 0  
        query = "Apple market"
        print("Querying ", query)
        relevantSummaries = self.scrape_news_summaries(query)
        for summary in relevantSummaries:
            wiki = TextBlob(summary)
            print(summary)
            totalPolarity += wiki.sentiment.polarity
            totalSubjectivity += wiki.sentiment.subjectivity
            numLines += 1 


        finalTotalPolarity += totalPolarity
        finalTotalSubjectivity += totalSubjectivity/numLines
        print ("Sentiment Polarity: ",totalPolarity)
        print ("Sentiment Subjectivity: ",totalSubjectivity/numLines)

        totalPolarity = 0
        totalSubjectivity = 0
        numLines = 0 
        query = "Apple Geopolitical Situation"
        print("Querying ", query)
        relevantSummaries = self.scrape_news_summaries(query)
        for summary in relevantSummaries:
            wiki = TextBlob(summary)
            print(summary)
            totalPolarity += wiki.sentiment.polarity
            totalSubjectivity += wiki.sentiment.subjectivity
            numLines += 1

        finalTotalPolarity += totalPolarity
        finalTotalSubjectivity += totalSubjectivity/numLines 
        print ("Sentiment Polarity: ", totalPolarity)
        print ("Sentiment Subjectivity: ", totalSubjectivity/numLines)

        totalPolarity = 0
        totalSubjectivity = 0
        numLines = 0 
        query = "Apple iPhone"
        print("Querying ", query)
        relevantSummaries = self.scrape_news_summaries(query)
        for summary in relevantSummaries:
            wiki = TextBlob(summary)
            print(summary)
            totalPolarity += wiki.sentiment.polarity
            totalSubjectivity += wiki.sentiment.subjectivity
            numLines += 1 

        finalTotalPolarity += totalPolarity
        finalTotalSubjectivity += totalSubjectivity/numLines
        print ("Sentiment Polarity: ", totalPolarity)
        print ("Sentiment Subjectivity: ", totalSubjectivity/numLines)

        print ("Calculating final score to predict if stock price would go up or down")
        print ("Combined Sentiment Polarity: ", finalTotalPolarity)
        print ("Overall Sentiment Subjectivity: ", finalTotalSubjectivity/5)


    @Rule(Company(name='AMZN'))
    def predictAMZN(self):
        print("Predicting stock for Amazon...")
        print("Looking up necessary stock info")

        finalTotalPolarity = 0
        finalTotalSubjectivity = 0
        totalPolarity = 0
        totalSubjectivity = 0
        numLines = 0 
        query = "Amazon"
        print("Querying ", query)
        relevantSummaries = self.scrape_news_summaries(query)
        for summary in relevantSummaries:
            wiki = TextBlob(summary)
            print(summary)  
            totalPolarity += wiki.sentiment.polarity
            totalSubjectivity += wiki.sentiment.subjectivity
            numLines += 1 
        finalTotalPolarity += totalPolarity
        finalTotalSubjectivity += totalSubjectivity/numLines
        print ("Sentiment Polarity: ", totalPolarity)
        print ("Sentiment Subjectivity: ", totalSubjectivity/numLines)

        print("\n")

        totalPolarity = 0
        totalSubjectivity = 0
        numLines = 0 
        query = "Amazon stocks"
        print("Querying ", query)
        relevantSummaries = self.scrape_news_summaries(query)
        for summary in relevantSummaries:
            wiki = TextBlob(summary)
            print(summary)  
            totalPolarity += wiki.sentiment.polarity
            totalSubjectivity += wiki.sentiment.subjectivity
            numLines += 1 
        finalTotalPolarity += totalPolarity
        finalTotalSubjectivity += totalSubjectivity/numLines
        print ("Sentiment Polarity: ", totalPolarity)
        print ("Sentiment Subjectivity: ", totalSubjectivity/numLines)

        print("\n")

        totalPolarity = 0
        totalSubjectivity = 0
        numLines = 0 
        query = "Amazon market"
        print("Querying ", query)
        relevantSummaries = self.scrape_news_summaries(query)
        for summary in relevantSummaries:
            wiki = TextBlob(summary)
            print(summary)  
            totalPolarity += wiki.sentiment.polarity
            totalSubjectivity += wiki.sentiment.subjectivity
            numLines += 1 
        finalTotalPolarity += totalPolarity
        finalTotalSubjectivity += totalSubjectivity/numLines
        print ("Sentiment Polarity: ", totalPolarity)
        print ("Sentiment Subjectivity: ", totalSubjectivity/numLines)
        
        print("\n")
 
        totalPolarity = 0
        totalSubjectivity = 0
        numLines = 0 
        query = "Amazon firestick"
        print("Querying ", query)
        relevantSummaries = self.scrape_news_summaries(query)
        for summary in relevantSummaries:
            wiki = TextBlob(summary)
            print(summary)  
            totalPolarity += wiki.sentiment.polarity
            totalSubjectivity += wiki.sentiment.subjectivity
            numLines += 1 

        finalTotalPolarity += totalPolarity
        finalTotalSubjectivity += totalSubjectivity/numLines
        print ("Sentiment Polarity: ", totalPolarity)
        print ("Sentiment Subjectivity: ", totalSubjectivity/numLines)

        print ("Calculating final score to predict if stock price would go up or down")
        print ("Combined Sentiment Polarity: ", finalTotalPolarity)
        print ("Overall Sentiment Subjectivity: ", finalTotalSubjectivity/4)

    @Rule(Company(name='GOOG'))
    def predictGOOG(self):
        print("Predicting stock for Google...")
        print("Looking up necessary stock info")

        finalTotalPolarity = 0
        finalTotalSubjectivity = 0
        totalPolarity = 0
        totalSubjectivity = 0
        numLines = 0 
        query = "Google"
        print("Querying ", query)
        relevantSummaries = self.scrape_news_summaries(query)
        for summary in relevantSummaries:
            wiki = TextBlob(summary)
            print(summary)  
            totalPolarity += wiki.sentiment.polarity
            totalSubjectivity += wiki.sentiment.subjectivity
            numLines += 1 
        finalTotalPolarity += totalPolarity
        finalTotalSubjectivity += totalSubjectivity/numLines
        print ("Sentiment Polarity: ", totalPolarity)
        print ("Sentiment Subjectivity: ", totalSubjectivity/numLines)

        print("\n")

        totalPolarity = 0
        totalSubjectivity = 0
        numLines = 0 
        query = "Google stocks"
        print("Querying ", query)
        relevantSummaries = self.scrape_news_summaries(query)
        for summary in relevantSummaries:
            wiki = TextBlob(summary)
            print(summary)  
            totalPolarity += wiki.sentiment.polarity
            totalSubjectivity += wiki.sentiment.subjectivity
            numLines += 1 
        finalTotalPolarity += totalPolarity
        finalTotalSubjectivity += totalSubjectivity/numLines
        print ("Sentiment Polarity: ", totalPolarity)
        print ("Sentiment Subjectivity: ", totalSubjectivity/numLines)

        print("\n")

        totalPolarity = 0
        totalSubjectivity = 0
        numLines = 0 
        query = "Google market"
        print("Querying ", query)
        relevantSummaries = self.scrape_news_summaries(query)
        for summary in relevantSummaries:
            wiki = TextBlob(summary)
            print(summary)  
            totalPolarity += wiki.sentiment.polarity
            totalSubjectivity += wiki.sentiment.subjectivity
            numLines += 1 
        finalTotalPolarity += totalPolarity
        finalTotalSubjectivity += totalSubjectivity/numLines
        print ("Sentiment Polarity: ", totalPolarity)
        print ("Sentiment Subjectivity: ", totalSubjectivity/numLines)

        print("\n")

        totalPolarity = 0
        totalSubjectivity = 0
        numLines = 0 
        query = "Google g pixel"
        print("Querying ", query)
        relevantSummaries = self.scrape_news_summaries(query)
        for summary in relevantSummaries:
            wiki = TextBlob(summary)
            print(summary)  
            totalPolarity += wiki.sentiment.polarity
            totalSubjectivity += wiki.sentiment.subjectivity
            numLines += 1 
        finalTotalPolarity += totalPolarity
        finalTotalSubjectivity += totalSubjectivity/numLines
        print ("Sentiment Polarity: ", totalPolarity)
        print ("Sentiment Subjectivity: ", totalSubjectivity/numLines)

        print ("Calculating final score to predict if stock price would go up or down")
        print ("Combined Sentiment Polarity: ", finalTotalPolarity)
        print ("Overall Sentiment Subjectivity: ", finalTotalSubjectivity/4)

    def scrape_news_summaries(self, s):
        time.sleep(randint(0, 2))  # relax and don't let google be angry
        r = requests.get("http://www.google.co.uk/search?q=" + s + "&tbm=nws")
        content = r.text
        news_summaries = []
        soup = BeautifulSoup(content, "html.parser")
        st_divs = soup.findAll("div", {"class": "st"})
        for st_div in st_divs:
            news_summaries.append(st_div.text)
        return news_summaries


    @Rule(Action('Query'),
          Company(name="name"<<W()),
          Fact(factname="factname"<<W()))
    def query(self,factname):

        finalTotalPolarity = 0
        finalTotalSubjectivity = 0
        totalPolarity = 0
        totalSubjectivity = 0
        numLines = 0 
        query = factname + " stocks"
        print("Querying ", query)
        relevantSummaries = self.scrape_news_summaries(query)
        for summary in relevantSummaries:
             wiki = TextBlob(summary)
             print(summary)  
             totalPolarity += wiki.sentiment.polarity
             totalSubjectivity += wiki.sentiment.subjectivity
             numLines += 1 
        finalTotalPolarity += totalPolarity
        finalTotalSubjectivity += totalSubjectivity/numLines

        print ("Sentiment Polarity: ", totalPolarity)
        print ("Sentiment Subjectivity: ", totalSubjectivity/numLines)

        totalPolarity = 0
        totalSubjectivity = 0
        numLines = 0 
        query = factname + " market"
        print("Querying ", query)
        relevantSummaries = self.scrape_news_summaries(query)
        for summary in relevantSummaries:
            wiki = TextBlob(summary)
            print(summary)  
            totalPolarity += wiki.sentiment.polarity
            totalSubjectivity += wiki.sentiment.subjectivity
            numLines += 1 
        
        finalTotalPolarity += totalPolarity
        finalTotalSubjectivity += totalSubjectivity/numLines

        print ("Sentiment Polarity: ", totalPolarity)
        print ("Sentiment Subjectivity: ", totalSubjectivity/numLines)

        print("\n")

        totalPolarity = 0
        totalSubjectivity = 0
        numLines = 0 
        query = factname + " Geopolitical data"
        print("Querying ", query)
        relevantSummaries = self.scrape_news_summaries(query)
        for summary in relevantSummaries:
            wiki = TextBlob(summary)
            print(summary)  
            totalPolarity += wiki.sentiment.polarity
            totalSubjectivity += wiki.sentiment.subjectivity
            numLines += 1 
        finalTotalPolarity += totalPolarity
        finalTotalSubjectivity += totalSubjectivity/numLines

        print ("Sentiment Polarity: ", totalPolarity)
        print ("Sentiment Subjectivity: ", totalSubjectivity/numLines)

        print ("Calculating final score to predict if stock price would go up or down")
        print ("Combined Sentiment Polarity: ", finalTotalPolarity/3)
        print ("Overall Sentiment Subjectivity: ", finalTotalSubjectivity/3)


    @Rule(Company(name="name" <<W()),
          NOT (Company(name='GOOG')),
          NOT (Company(name='AMZN')),
          NOT (Company(name='AAPL')))
    def predict(self, name):
        print("Conducting Sentiment Analysis . . . ")
        self.declare(Fact(factname=name))        
        self.declare(Action('Query'))

"""takes company name. returns the current stock price for company"""
def pullStock(name):
    ticker = name
    url = "https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={0}&outputsize=full&apikey=LBG3YII29JOX2SSU".format(
        ticker)
    response = requests.get(url)
    json_loaded = json.loads(response.text)
    if ('Error Message' in json_loaded.keys()):
        print(json.dumps("Error: Please input correct stock symbol."))
    else:
        #summaryDataList = []
        timeSeries = json_loaded["Time Series (Daily)"]
        #xList = list(timeSeries.keys())
        yListValues = list(timeSeries.values())

        for i in range(len(yListValues)):
            return float(yListValues[i]['4. close'])


engine = Prediction()
engine.reset()
engine.run()
