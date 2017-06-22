from rest_framework import serializers
from DoublespeakAPI.API.models import *


class CandidateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Candidate
        exclude = ()


class SentimentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sentiment
        exclude = ()


class WatsonEmotionSerializer(serializers.ModelSerializer):
    class Meta:
        model = WatsonEmotionalTone
        exclude = ()


class WatsonPersonalitySerializer(serializers.ModelSerializer):
    class Meta:
        model = WatsonPersonalityTone
        exclude = ()
