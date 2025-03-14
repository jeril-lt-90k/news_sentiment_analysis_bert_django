import os
from django.shortcuts import render
from django.utils import timezone

from rest_framework.views import APIView
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from sentiment_analysis import execute_core_logic as ecl


class execute_API(APIView):

    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]


    def get(self, request):

        news_api_key = os.environ['NEWS_API_KEY']
        news_api_url = os.environ['NEWS_API_URL']
        news_count = 10

        ecl.download_news_item(news_count, news_api_key, news_api_url)

        context = {
        'status': 'Logic executed!',
        'timestamp': str(timezone.now())
        }

        return render(request, 'sentiment_analysis/response.html', context)