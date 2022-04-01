from rest_framework import viewsets

from survey.models import *
from survey.serializers import SurveySerializer


class SurveyViewset(viewsets.ModelViewSet):
    #Bad, bad queryset! 5 queries? No cookie for you!
    #queryset = Survey.objects.all() 
    #Good queryset! 3 queries, take a cookie:
    queryset = Survey.objects.prefetch_related('questions', 'questions__alternatives').all()
    serializer_class = SurveySerializer
