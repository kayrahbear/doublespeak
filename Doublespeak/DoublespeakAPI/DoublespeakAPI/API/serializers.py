from rest_framework import serializers
from DoublespeakAPI.API.models import *


class CandidateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Candidate
        exclude = ()


class SentimentSerializer(serializers.ModelSerializer):
    candidate = serializers.CharField(source="candidate.candidate_name")
    id = serializers.IntegerField(read_only=True)

    class Meta:
        model = Sentiment
        exclude = ()


class WatsonEmotionSerializer(serializers.ModelSerializer):
    candidate = serializers.CharField(source="candidate.candidate_name")
    id = serializers.IntegerField(read_only=True)

    class Meta:
        model = WatsonEmotionalTone
        exclude = ()


class WatsonPersonalitySerializer(serializers.ModelSerializer):
    candidate = serializers.CharField(source="Candidate.candidate_name")
    id = serializers.IntegerField(read_only=True)

    class Meta:
        model = WatsonPersonalityTone
        exclude = ()
