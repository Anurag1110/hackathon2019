from django.conf.urls import include, url
from . import views

app_name = 'interview'

urlpatterns = [

    url(r'^$', views.index, name='index'),
    url(r'^candidateProfile/$', views.goToCandidateProfile, name='goToCandidateProfile'),
    url(r'^test/$', views.test, name='test'),
    url(r'^candidateProfile/instructions/$', views.goToInstructionsPage, name='goToInstructionsPage'),


]
