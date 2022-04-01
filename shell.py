from survey.models import *

#Primeiro Survey
first_survey = Survey(name = 'Refrigerantes', description= 'Pesquisa de mercado sobre refrigerantes')
first_survey.save()


#As SurveyQuestions
flavors = ['cola', 'laranja', 'limão']
questions = [SurveyQuestion(survey= first_survey, text= f'Com que frequência você consome refrigerantes de {flavor}?') for flavor in flavors]
SurveyQuestion.objects.bulk_create(questions)


#Suas respectivas SurveyQuestionAlternatives
choices = ['Muita', 'Pouca', 'Nunca']
for n in range(len(questions)):
    SurveyQuestionAlternative.objects.bulk_create([SurveyQuestionAlternative(question=SurveyQuestion.objects.get(pk=n+1),  text=choice) for choice in choices])