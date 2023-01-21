from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from .models import *
import random

# Create your views here.
def index(request):
    context = {
        "title": "Platform"
    }
    return render(request, "platform/index.html", context)

def get_random_sublist(l, sub_length):
    if sub_length >= len(l):
        return []
    result = []
    for i in range(sub_length):
        current_index = random.randint(0, len(l) - 1)
        while l[current_index] in result:
            current_index = random.randint(0, len(l) - 1)
        result.append(l[current_index])
    return result

def check_answer(question, answer):
    # TODO
    return True

def test_view(request, theme_id):
    if request.method == "POST":
        print("GET DATA!!!")
        print(request.POST)
        correct_count = 0 # Кол-во правильных ответов
        count = 0 # Кол-во всего ответов
        for key in request.POST:
            if "question" in key:
                count += 1
                if check_answer(key, request.POST[key]):
                    correct_count += 1
        context = {
            "title": "Результаты теста",
            "correct_answer_count": correct_count,
            "question_count": count
        }
        return render(request, "platform/tests/results.html", context)
    else:
        # Получаем случайные вопросы про конфиденциальность
        questions_privacy_all = SimpleQuestion.objects.filter(correct_answer=2)
        questions_privacy_send = get_random_sublist(questions_privacy_all, 3)

        # Получаем случайные вопросы про доступность
        questions_access_all = SimpleQuestion.objects.filter(correct_answer=1)
        questions_access_send = get_random_sublist(questions_access_all, 3)

        # Получаем случайные вопросы про целостность
        questions_integrity_all = SimpleQuestion.objects.filter(correct_answer=3)
        questions_integrity_send = get_random_sublist(questions_integrity_all, 3)

        questions_send = questions_privacy_send + questions_access_send + questions_integrity_send
        print(questions_send)
        context = {
            "title": "Test на тему 1",
            "questions": questions_send,
            "randomList": [random.randint(1, 100) for i in range(100)]
        }
        return render(request, f"platform/tests/test-theme-{theme_id}.html", context)