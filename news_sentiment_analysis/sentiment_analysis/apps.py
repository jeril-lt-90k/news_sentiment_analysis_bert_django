from django.apps import AppConfig


class SentimentAnalysisConfig(AppConfig):
    
    default_auto_field = "django.db.models.BigAutoField"
    name = "sentiment_analysis"

    def ready(self):

        import sentiment_analysis.signals