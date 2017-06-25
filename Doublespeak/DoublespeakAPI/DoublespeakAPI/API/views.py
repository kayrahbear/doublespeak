from rest_framework.response import Response
from rest_framework import views, viewsets, status
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


class GetSentimentbyCandidateID(views.APIView):
    def get(self, request, candidate_id, format=None):

        # req_body= json.loads(request.body.decode())
        # print("\n\n{}".format(req_body['deck']))

        sentiment = Sentiment.objects.filter(candidate=candidate_id)
        serializer = SentimentSerializer(sentiment, many=True)

        try:

            return Response(serializer.data, content_type='application/json')
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)


class GetEmotionbyCandidateID(views.APIView):
    def get(self, request, candidate_id, format=None):

        # req_body= json.loads(request.body.decode())
        # print("\n\n{}".format(req_body['deck']))

        emotion = WatsonEmotionalTone.objects.filter(candidate=candidate_id)
        serializer = WatsonEmotionSerializer(emotion, many=True)

        try:

            return Response(serializer.data, content_type='application/json')
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)


class GetPersonalitybyCandidateID(views.APIView):
    def get(self, request, candidate_id, format=None):

        # req_body= json.loads(request.body.decode())
        # print("\n\n{}".format(req_body['deck']))

        personality = WatsonPersonalityTone.objects.filter(Candidate=candidate_id)
        serializer = WatsonPersonalitySerializer(personality, many=True)

        try:

            return Response(serializer.data, content_type='application/json')
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)
