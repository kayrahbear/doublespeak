from django.conf.urls import url, include
from rest_framework import routers
from DoublespeakAPI.API.views import *

router = routers.DefaultRouter()

router.register(r'candidate', CandidateViewSet)
router.register(r'sentiment', SentimentViewSet)
router.register(r'watsonemotion', WatsonEmotionViewSet)
router.register(r'watsonpersonality', WatsonPersonalityViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
