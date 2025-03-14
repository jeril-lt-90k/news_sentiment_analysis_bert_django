from django.utils import timezone
import requests
from transformers import pipeline

from .models import news_details
from .models import sentiment_results


import logging
logger = logging.getLogger(__name__)


def calculate_sentiment(text_to_analyze):
    
    sentiment_pipeline = pipeline("sentiment-analysis", model = "ProsusAI/finbert")
    result = sentiment_pipeline(text_to_analyze)[0]

    sentiment_score = result['score']
    sentiment_value = result['label']
    
    return sentiment_score, sentiment_value


def download_news_item(news_item_count, news_api_key, news_api_url):


    headers = {'X-Api-Key': news_api_key}
    
    news_details_table = news_details.objects.values('news_category', 'news_topic', 'search_input_term').order_by('news_category')


    for row in news_details_table:

        news_category = row['news_category']
        news_topic = row['news_topic']
        search_input = row['search_input_term']

        returned_response = None

        try:
            
            parameters = {'country': 'us', 'category': news_category, 'q': search_input, 'pageSize': news_item_count}

            returned_response = requests.get(news_api_url, headers = headers, params = parameters).json()

        except:

            logger.exception('Error fetching news item for topic: ' + news_topic)
            continue


        for news_item in returned_response["articles"]:
                    
            if sentiment_results.objects.filter(news_text = news_item['title']).exists():

                continue

            else:
                
                sentiment_score, sentiment_value = calculate_sentiment(news_item['title'])

                current_datetime = str(timezone.now().isoformat())
                sentiment_result_object = sentiment_results(news_category = news_category, news_topic = news_topic, news_text = news_item['title'], news_published_at = news_item['publishedAt'], news_saved_at = current_datetime, news_link = news_item['url'], sentiment_score = sentiment_score, sentiment_value = sentiment_value)
                sentiment_result_object.save()

                news_details.objects.filter(search_input_term = search_input).update(last_updated = current_datetime)