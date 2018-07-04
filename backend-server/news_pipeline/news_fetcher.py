###keeping fetch news from cloudAMQP####
import os
import sys
#from newspaper import Article

#import common package in parent directory
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'common'))
sys.path.append(os.path.join(os.path.dirname(__file__), 'scrapers'))

import cnn_news_scraper
from cloudAMQP_client import CloudAMQPClient

SLEEP_TIME_IN_SECONDS = 5
SCRAPE_NEWS_TASK_QUEUE_URL = "amqp://gasbxbad:tI4GyfxZg79tArnXgQiYKVXRLf_Lqrjm@llama.rmq.cloudamqp.com/gasbxbad"
SCRAPE_NEWS_TASK_QUEUE_NAME = "tap-news-scrape-task-queue"
DEDUPE_NEWS_TASK_QUEUE_URL = "amqp://gasbxbad:tI4GyfxZg79tArnXgQiYKVXRLf_Lqrjm@llama.rmq.cloudamqp.com/gasbxbad"
DEDUPE_NEWS_TASK_QUEUE_NAME = "tap-news-dedupe-task-queue"

scrape_news_queue_client = CloudAMQPClient(SCRAPE_NEWS_TASK_QUEUE_URL, SCRAPE_NEWS_TASK_QUEUE_NAME)
dedupe_news_queue_client = CloudAMQPClient(DEDUPE_NEWS_TASK_QUEUE_URL, DEDUPE_NEWS_TASK_QUEUE_NAME)

def handle_message(msg):
    if msg is None or not isinstance(msg, dict):
        print 'message is broken'
        return

    task = msg
    text = None

    #article = Article(task['url'])
    #article.download()
    #article.parse()
    #task['text'] = text
    #dedupe_news_queue_client.sendMessage(task)

    if task['source'] == 'CNN':
            print 'Scraping CNN news'
            text = cnn_news_scraper.extract_news(task['url'])
    else:
        print 'News source [%s] is not supported.' % task['source']

    task['text'] = text
    dedupe_news_queue_client.sendMessage(task)

while True:
    if scrape_news_queue_client is not None:
        msg = scrape_news_queue_client.getMessage()
        if msg is not None:
            #parse and process the task
            try:
                handle_message(msg)
            except Exception as e:
                print e
                pass
            scrape_news_queue_client.sleep(SLEEP_TIME_IN_SECONDS)