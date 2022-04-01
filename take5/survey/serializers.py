from rest_framework import serializers

from survey.models import *

class SurveyQuestionSerializer(serializers.ModelSerializer):
    alternatives = serializers.StringRelatedField(many=True)

    class Meta:
        model = SurveyQuestion
        fields = ['text', 'alternatives', 'date']

class SurveySerializer(serializers.ModelSerializer):
    questions = SurveyQuestionSerializer(many=True, read_only=True)
    
    class Meta:
        model = Survey
        fields = ['id', 'name', 'description', 'date', 'questions']