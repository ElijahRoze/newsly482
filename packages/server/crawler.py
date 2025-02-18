import time
import feedparser
import requests

from .db import list_feed_sources, save_news_article
from .recommendation import parse_inputs
from .thesaurus import thesaurus

def is_valid_url(url):
    try:
        # Download the headers of the url and check if they have an iframe policy or a content
        # security policy. If they have any of those, it will not load in our iframe and so
        # we can mark this url as invalid.
        r = requests.head(url, allow_redirects=True)
        content_exists = 'content-security-policy' in r.headers
        frame_exists = 'x-frame-options' in r.headers
        return content_exists is False and frame_exists is False
    except Exception as ex:
        print(ex)
        return False

def crawl_feeds():
    # Get a list of feeds
    srcs = list_feed_sources()
    indexed = []
    # Get all the machine learning inputs
    inputs = parse_inputs()
    urls = []

    # For each feed, we will extract information about it
    for src in srcs:
        d = feedparser.parse(src['feed_url'])
        # For each entry in the feed...
        for entry in d.entries:

            # Copy the machine learning inputs
            news_article_weights = inputs.copy()
            
            # And match each word in the title of the article with the machine learning input.
            # This will create a HashMap of inputs that represent the news article so we can 
            # eventually feed it into the recommendation engine.
            for word in str(entry.title).lower().split(' '):
                related = thesaurus(word)
                for key in related:
                    if key in news_article_weights:
                        news_article_weights[key] += 1
            
            # If we have already seen this link, skip it
            if entry.link in urls:
                continue

            urls.append(entry.link)

            # Check if the news article is valid and if it is, save the news article to the database
            if is_valid_url(entry.link):
                return_code = save_news_article(
                    entry.title,
                    entry.link,
                    news_article_weights
                )

            # Wait a little, so we don't spam the websites
            time.sleep(0.05)