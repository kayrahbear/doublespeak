from rest_framework import viewsets
from DoublespeakAPI.API.serializers import *
from DoublespeakAPI.API.models import *


# Create your views here.
class CandidateViewSet(viewsets.ModelViewSet):
    queryset = Candidate.objects.all()
    serializer_class = CandidateSerializer


class SentimentViewSet(viewsets.ModelViewSet):
    queryset = Sentiment.objects.all()
    serializer_class = SentimentSerializer


class WatsonEmotionViewSet(viewsets.ModelViewSet):
    queryset = WatsonEmotionalTone.objects.all()
    serializer_class = WatsonEmotionSerializer


class WatsonPersonalityViewSet(viewsets.ModelViewSet):
    queryset = WatsonPersonalityTone.objects.all()
    serializer_class = WatsonPersonalitySerializer
