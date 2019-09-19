from django.db import models


class InterviewQuestion(models.Model):

    interview_question_name = models.CharField(max_length=250)
    interview_question_text = models.TextField()


class InterviewAnswer(models.Model):
    question = models.ForeignKey(InterviewQuestion,on_delete=models.CASCADE)
    answer = models.TextField()







