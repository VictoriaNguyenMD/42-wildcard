
## What is Wildcard?

<!-- BACKGROUND INFORMATION -->
## Introduction to Web Scraping in Healthcare 

The Internet stores a massive amount of information that can be extracted and analyzed. The process of obtainig this data from websites is known as web scraping. Web scraping can be done manually but it is most often performed via an automated process implemented using a bot or web crawler.

In the context of healthcare, most of what happens occurs outside the doctor's office. In fact, we are in a doctor's office for only a fraction of our life. According to the [2016 Physician Compensation Report](https://www.medscape.com/features/slideshow/compensation/2016/public/overview?src=wnl_physrep_160401_mscpedit&uac=232148CZ&impID=1045700&faf=1), doctors spend an average of 13-16 minutes with each patient, which is minimal compared to our lifespan.

As a result, web scraping is a way to quickly obtain data from people, such as customer feedback, potential suicidial ideations, and potential outbreaks. One Canadian company, BlueDot, using web scraping to detect the coronavirus outbreak several days before it was initially announced by the World Health Organization (WHO) and Centers for Disease Control and Prevention (CDC). In particular,this artificial intelligence (AI) company scours ["foreign-language news reports, animal and plant disease networks, and official proclamations"](https://www.wired.com/story/ai-epidemiologist-wuhan-public-health-warnings/) to provide infectious disease warnings to you.

Twitter, amongst many websites, is an excellent platform to display one's opinion toward a subject in an unbiased, natural manner. Since this social media platform is easy to access and public, it is a gold mine for extracting data, especially in terms of surveying public opinion about a particular healthcare product. 

In this project, we will scrape Twitter to create a tweet visualization and sentiment analysis to analyze healthcare-related Tweets using Python. 

## Utilizing a Twitter Scraper to Analyze 

In order to start scraping information from Twitter, you need a tool that enables Python to communicate with the Twitter platform. There are many packages and libraries that can bridge the conenction from code to the plaftform, but two particular tools in mind are BeautifulSoup and Tweepy. These tools are useful for webscraping and can extract tweets. 

The particular library that we are going to use for this product is Tweepy. This library is:
1. Easy-to-use
2. Has access to Twitter API
3. Can extract tweets real-time

<!-- PROJECT OUTLINE -->
## Project Outline: 

**1. Stream Live Tweets**
To stream live tweets, we need to first develop a Twitter application to access Twitter APIs using [http://apps.twitter.com/](http://apps.twitter.com/). We will obtain 2 keys (API key and API secret key) and 2 tokens (access token and access token secret) to have a unique identification to authenticate each API request. We will then import a StreamListener and OAuthHandler to authenticate the access and listen to live tweets. Running the code will output a dictionary for the tweets is a JSON file format.

[Streaming Live Tweets](media/streaming.gif)

**2. Cursor and Pagination**

**3. Analyzing Tweet Data**

**4. Visualizing Tweet Data**

**5. Sentiment Analysis**

<!-- GETTING STARTED -->
## Getting Started

### Clone
`git clone https://github.com/VictoriaNguyenMD/42-wildcard.git`

### Set-Up

**Brew Installation**

For this project, we will use `pip` instead of `brew`; however, if you are a 42 student, make sure you have `brew` installed. If you do not have brew, message @Kane to receive the brew instructions. Otherwise, you can also install brew below:
```
mkdir $HOME/.brew && curl -fsSL https://github.com/Homebrew/brew/tarball/master | tar xz --strip 1 -C $HOME/.brew
mkdir -p /tmp/.$(whoami)-brew-locks
mkdir -p $HOME/.brew/var/homebrew
ln -s /tmp/.$(whoami)-brew-locks $HOME/.brew/var/homebrew/locks
export PATH="$HOME/.brew/bin:$PATH"
brew update && brew upgrade
```
Afterwards, in your main directory, vim `.zshrc` and add the following lines:
```
mkdir -p /tmp/.$(whoami)-brew-locks
export PATH="$HOME/.brew/bin:$PATH"
```

**Tweepy Insallation**

`pip install tweepy`

### API Keys
In the `twitter_credentials.py` file, replace the values inside the "" with your specific Twitter App tokens and keys. This wil contain variables that contain the user credentials to access Twitter API.

```
ACCESS_TOKEN = ""
ACCESS_TOKEN_SECRET = ""
CONSUMER_KEY = ""  
CONSUMER_SECRET = ""
```

<!-- USAGE EXAMPLES -->
## Usage

<!-- ERROR MESSAGES -->

## Error Messages
1. **`unable to import 'tweepy'pylint(import-error)`**

In your terminal, type `python -V` to obtain the version of your using VS Code, type CMD + SHIFT + P to open the Command Palette. Type `Python: Select Interpreter` and choose the python interpreter that appropriately matches the version you are using.

2. **`401` Status Code Error when running `python tweepy_streamer.py`**

You may have made a mistake in copying the Access Tokens from [apps.twitter.com](http://apps.twitter.com/). Regenerate an Access token and copy the token into the `twitter-credentials.py` file.

<!-- CONTRIBUTING -->
## Contributing
Contributions are what make the open source community such an amazing place to be learn, inspire, and create. Any contributions you make are **greatly appreciated**.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/DesignFeature`)
3. Commit your Changes (`git commit -m 'Add some DesignFeature'`)
4. Push to the Branch (`git push origin feature/DesignFeature`)
5. Open a Pull Request

### References
1. [Web Scraping](https://en.wikipedia.org/wiki/Web_scraping)
2. [Tweet Visualization and Sentiment Analysis](https://www.youtube.com/watch?v=1gQ6uG5Ujiw)
3. [Tweepy Documentation](http://docs.tweepy.org/en/latest/)
