from django.db import models

# Create your models here.

class sentiment_results(models.Model):
    
    news_category = models.CharField(max_length = 255, default = '')
    news_topic = models.CharField(max_length = 255, default = '')
    news_text = models.TextField(default = "")
    news_published_at = models.DateTimeField(null = True, default = None)
    news_saved_at = models.DateTimeField(null = True, default = None)
    news_link = models.TextField(default = "")
    sentiment_score = models.FloatField(default = -999)
    sentiment_value = models.CharField(max_length = 255, default = 'none')

    def __str__(self):

        return str(self.news_topic)


class news_details(models.Model):

    news_category = models.CharField(max_length = 255, default = '')
    news_topic = models.CharField(max_length = 255, default = '')
    search_input_term = models.TextField()
    last_updated = models.DateTimeField(null = True, default = None)

    def __str__(self):
        
        return str(self.news_topic)