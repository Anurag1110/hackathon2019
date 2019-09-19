from django.shortcuts import render
from django.http import HttpResponse
import pyttsx3
from gtts import gTTS
import speech_recognition as sr
import urllib3
from .models import InterviewAnswer,InterviewQuestion


def index(request):
    return render(request, 'interview/index.html')


def goToCandidateProfile(request):
    return render(request, 'interview/candidateprofileview.html')


def test(request):



    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

    f = open("assesment.txt", "a")
    questions = InterviewQuestion.objects.all()
    questionCount = 0
    cu = 0
    while (questionCount < len(questions)):
        print("Question No", questionCount, ":", questions[questionCount])
        engine = pyttsx3.init()
        engine.setProperty('rate', 140)

        r = sr.Recognizer()
        with sr.Microphone() as source:
            r.adjust_for_ambient_noise(source, duration=1)
            engine.say(questions[questionCount].interview_question_text)
            engine.runAndWait()
            engine.stop()
            print("Say something!")
            r.pause_threshold = 1
            audio = r.listen(source, phrase_time_limit=10)
        try:
            response = r.recognize_google(audio)
            answer = InterviewAnswer();
            answer.question = questions[questionCount];
            answer.answer = response;
            answer.save()

            print("I think you said :'" + response + "'")
            f.write(response + "\n")
            tts = gTTS(text="I think you said " + str(response), lang='en')
            questionCount += 1
            cu = 0

        except sr.UnknownValueError:
            print("Sphinx could not understand audio ")
            cu += 1
            if (cu == 3):
                questionCount += 1
                cu = 0

        except sr.RequestError as e:
            print("Sphinx error; {0}".format(e))




    return HttpResponse("")


def goToInstructionsPage(request):
    return render(request, 'interview/instructionpage.html')



