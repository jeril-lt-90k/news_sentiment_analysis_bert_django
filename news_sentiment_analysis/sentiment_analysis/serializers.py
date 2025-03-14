from rest_framework import serializers
from .models import sentiment_results


class sentimentResultsSerializer(serializers.ModelSerializer):

    class Meta:

        model = sentiment_results
        fields = '__all__'
