
## What is Wildcard?
Wildcard is a project that allows you to pursue a topic of interest to gain XP within the 42 program. It should take about 50 hours to complete, including the GitHub and environment set-up.

<!-- BACKGROUND INFORMATION -->
## Introduction to Web Scraping in Healthcare 

The Internet stores a massive amount of information that can be extracted and analyzed. The process of obtainig this data from websites is known as web scraping. Web scraping can be done manually but it is most often performed via an automated process implemented using a bot or web crawler.

In the context of healthcare, most of what happens occurs outside the doctor's office. In fact, we are in a doctor's office for only a fraction of our life. According to the [2016 Physician Compensation Report](https://www.medscape.com/features/slideshow/compensation/2016/public/overview?src=wnl_physrep_160401_mscpedit&uac=232148CZ&impID=1045700&faf=1), doctors spend an average of 13-16 minutes with each patient, which is minimal compared to our lifespan.

As a result, web scraping is a way to quickly obtain data from people, such as customer feedback, potential suicidial ideations, and potential outbreaks. One Canadian company, BlueDot, using web scraping to detect the coronavirus outbreak several days before it was initially announced by the World Health Organization (WHO) and Centers for Disease Control and Prevention (CDC). In particular,this artificial intelligence (AI) company scours ["foreign-language news reports, animal and plant disease networks, and official proclamations"](https://www.wired.com/story/ai-epidemiologist-wuhan-public-health-warnings/) to provide infectious disease warnings to you.

Twitter, amongst many websites, is an excellent platform to display one's opinion toward a subject in an unbiased, natural manner. Since this social media platform is easy to access and public, it is a gold mine for extracting data, especially in terms of surveying public opinion about a particular healthcare product. 

## What is the Purpose of This Project?

This Python project will use [Tweepy Library](https://www.tweepy.org/) and [Twitter API](http://docs.tweepy.org/en/latest/api.html#API.search) tools to scrape Twitter tweets in order to create a tweet analysis of healthcare-related topic. After discovering how BlueDot used web scraping to quickly assess the potential outbreak of coronavairus, I became more interested in the applications of data mining and web scraping from nontraditional sources. This project therefore scrapes Twitter tweets to introduce twitter scaping. In addition, there are bonus functions such as analyzing the emotional state of the collected data and outputing graphical displays. 

## Utilizing a Twitter Scraper to Analyze Healthcare Data

In order to start scraping information from Twitter, you need a tool that enables Python to communicate with the Twitter platform. There are many packages and libraries that can bridge the conenction from code to the plaftform, but two particular tools in mind are BeautifulSoup and Tweepy. These tools are useful for webscraping and can extract tweets. 

The particular library that we are going to use for this product is Tweepy. This library is:
1. Easy-to-use
2. Has access to Twitter API
3. Can extract tweets real-time

<!-- PROJECT OUTLINE -->
## Project Outline: 

**1. Stream Live Tweets**

To stream live tweets, we need to first develop a Twitter application to access Twitter APIs using [http://apps.twitter.com/](http://apps.twitter.com/). We will obtain 2 keys (API key and API secret key) and 2 tokens (access token and access token secret) to have a unique identification to authenticate each API request. We will then import a StreamListener and OAuthHandler to authenticate the access and listen to live tweets. Running the code will output a dictionary for the tweets is a JSON file format.

<a href="https://gifyu.com/image/7FgE"><img src="https://s4.gifyu.com/images/twitter_streamingebfc7af3894b0c1c.gif" alt="twitter_streamingebfc7af3894b0c1c.gif" width="200" height="200"/></a>
<a href="https://gifyu.com/image/7FgE"><img src="https://s4.gifyu.com/images/twitter_streamingebfc7af3894b0c1c.gif" alt="twitter_streamingebfc7af3894b0c1c.gif" width="200" height="200"/></a>
<a href="https://gifyu.com/image/7FgE"><img src="https://s4.gifyu.com/images/twitter_streamingebfc7af3894b0c1c.gif" alt="twitter_streamingebfc7af3894b0c1c.gif" width="200" height="200"/></a>
<a href="https://gifyu.com/image/7FgE"><img src="https://s4.gifyu.com/images/twitter_streamingebfc7af3894b0c1c.gif" alt="twitter_streamingebfc7af3894b0c1c.gif" width="200" height="200"/></a>

**2. Cursor and Pagination**

To obtain tweets via search query, a cursor based pagination will be used to provide a record based on a unique identifier. A cursor acts as a pointer to the next record for the query. A Twitter client will be  used with the Twitter API's functions to query the results and a Cursor  will then facilitate in the retrieval of data. The data will then be returned in a list. 

<img src="./media/cursor_pagination.png" alt="cursor_pagination.png"/>

**3. Analyzing Tweet Data**

To analyze tweets, you need to install pandas and NumPy. Pandas is a data manipulation tool in Python that will allow us to store the streamed tweets into a dataframe, which could then be used to analyze the data. NumPy is a numerical and mathematical library of Python that aids in data analysis and manipulation. The data obtained from streaming the tweets was extracted and placed into a dataframe for further analysis.

<img src="./media/analyzed_tweet_data.png" alt="analyzed_tweet_data.png"/>

**4. Visualizing Tweet Data [Bonus]** 

To visualize the data, we will then derive graphical outputs using the data frame obtained from analyzing the tweet. Using the NumPy and pandas, it is easy to manipulate the data and produce a visual display. Below is an example of the Twitter username @USUhealthsci's Likes vs. Retweets over several days.

<img src="./media/USU_dataframe.png" alt="USU Data Frame"/> 

<img src="./media/USU_time_series_plot.png" alt="USU Time Series Plot"/>

Below is an example of a Word Cloud developed from the query "COVID19."

<img src="./media/word_cloud.png" alt="COVID19 Word Cloud" width="400" height="200"/>

**5. Sentiment Analysis [Bonus]**

To obtain the sentiment analysis, we are going to use TextBlob, which is a natural language processing framework trained to analyze sentiment of text.

After a coronavirus query was conducted, below is an example of the text that received a positive sentiment:

<img src="./media/sentimental_trump_tweet.png" alt="Trump Tweet about Coronavirus"/>

Below is an example of the terminal sentiment analysis. The tweet is on id #1.

<img src="./media/sentimental_terminal_analysis.png" alt="Terminal Analysis of Coronavirus Tweet Queries"/>

<!-- GETTING STARTED -->
## Getting Started

### Clone
`git clone https://github.com/VictoriaNguyenMD/42-wildcard.git`

### Set-Up

Updating Python

`brew update`

`brew upgrade python`

Installing Packages

`pip3 install tweepy`

`pip3 install pandas`

`pip3 install numpy`

`pip3 install matplotlib`

`pip3 install wordcloud`

`pip3 install textblob`

### API Keys
In the `twitter_credentials.py` file, replace the values inside the `""` with your specific Twitter App tokens and keys. This wil contain variables that contain the user credentials to access Twitter API.

```
ACCESS_TOKEN = ""
ACCESS_TOKEN_SECRET = ""
CONSUMER_KEY = ""  
CONSUMER_SECRET = ""
```

### Running the Code

`python -W ignore tweepy_streamer.py`

Within this `tweepy_streamer.py`, under the main function at the bottom of the page, you can uncomment multiple lines with the Python multi-line quotes and import the appropriate library to test other example code. For instance, one example basecode is below:

```shell
    # Example Code #7: Time series plot using function
    # This code will use TweetVisualizer function to graph the plot
    """
    twitter_client = TwitterClient("USUhealthsci")
    tweets = twitter_client.get_user_timeline_tweets(100)
    
    tweet_analyzer = TweetAnalyzer()
    df = tweet_analyzer.tweets_to_dataframe(tweets) 

    tweet_visualizer = TweetVisualizer()
    y_values="likes"
    tweet_visualizer.plot_time_series(df, y_values)
    """
```

<!-- ERROR MESSAGES -->

## Error Messages
**`unable to import 'tweepy'pylint(import-error)`**

In your terminal, type `python -V` to obtain the version of your using VS Code, type CMD + SHIFT + P to open the Command Palette. Type `Python: Select Interpreter` and choose the  python interpreter that appropriately matches the version you are using.

**`401` Status Code Error when running `python tweepy_streamer.py`**

You may have made a mistake in copying the Access Tokens from [apps.twitter.com](http://apps.twitter.com/). Regenerate an Access token and copy the token into the `twitter-credentials.py` file.

**`Your installed Python is incomplete. Attempting to use lzma compression will result in Runtime Error`**

`brew reinstall xz` is suppoed to have lzma, such that when you use `import lzma`, there should be no errors. However, there is a warning when you run your python code. To silence the warning, run the code using `python -W ignore tweepy_stream.py` 

**`tweepy.error.TweepError: Twitter error response: status code = 429`**

The 429 code is returned when a request cannot be served due to reaching the application’s rate limit. You have to wait for the limit to rese. According to the [Twitter Webstite](https://developer.twitter.com/en/docs/basics/rate-limiting), there are two initial buckets available for GET requests: 15 calls every 15 minutes, and 180 calls every 15 minutes.

**`import` error**

If there is an importation error, at the top of the code, write `import ______` with teh `______` being the missing import library.

**Code keeps on running and doesn't stop**

The listener is listening for the tweets. You can type `CTRL + C` or `CTRL + D`. If this doesn't work, try `killall -9 python3.`  If this does not work, refer to this aritcle on [how to force quit via terminal](https://www.hongkiat.com/blog/force-quit-mac-app/).

<!-- REFELCTION -->
## Reflection
This code is far from complete but introduced me to the basics of web development. I spent around 75 hours deciding on a project, figuring out how I want to approach the project, looking up resources, coding the project, and then debugging numerous errors. The errors listed above were just a few amongst many errors. 

Some feature endeavors include creating a graphical display to input the query items rather than manually altering the code and including more functions.

<!-- CONTRIBUTING -->
## Contributing
Contributions are what make the open source community such an amazing place to be learn, inspire, and create. Any contributions you make are **greatly appreciated**.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/DesignFeature`)
3. Commit your Changes (`git commit -m 'Add some DesignFeature'`)
4. Push to the Branch (`git push origin feature/DesignFeature`)
5. Open a Pull Request

<!-- LICENSE -->
## License

[The MIT License (MIT)](https://choosealicense.com/licenses/mit/)
Copyright © 2020

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the “Software”), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

## References
1. [Web Scraping](https://en.wikipedia.org/wiki/Web_scraping)
2. [Tweet Visualization and Sentiment Analysis](https://www.youtube.com/watch?v=1gQ6uG5Ujiw) @vprusso
3. [Tweepy Documentation](http://docs.tweepy.org/en/latest/)
4. [Python Environment](https://realpython.com/intro-to-pyenv/#why-use-pyenv)
5. [Tweepy Error Messages](https://developer.twitter.com/en/docs/basics/response-codes)
