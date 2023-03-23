from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.contrib.auth.decorators import login_required

from .models import *
import random

# Create your views here.
def index(request):
    themes = Theme.objects.all()

    context = {
        "title": "Platform",
        "themes": themes
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

def check_test1_answer(question, answer):
    print(f"Вопрос: {question}, ответ: {answer}")
    try:
        answer = int(answer)
        question_id = int(question.split("-")[1])
        q = SimpleAnswer.objects.get(pk=question_id)
        print(q.correct_answer)
        if q.correct_answer == answer:
            return True
        else:
            return False
    except Exception as e:
        print(e)
        return False

def get_test_theme_1_questions():
    question_count = 1
    # Получаем случайные вопросы про конфиденциальность
    questions_privacy_all = SimpleQuestion.objects.filter(correct_answer=2)
    questions_privacy_send = get_random_sublist(questions_privacy_all, question_count)

    # Получаем случайные вопросы про доступность
    questions_access_all = SimpleQuestion.objects.filter(correct_answer=1)
    questions_access_send = get_random_sublist(questions_access_all, question_count)

    # Получаем случайные вопросы про целостность
    questions_integrity_all = SimpleQuestion.objects.filter(correct_answer=3)
    questions_integrity_send = get_random_sublist(questions_integrity_all, question_count)

    return questions_privacy_send + questions_access_send + questions_integrity_send

def get_test_theme_2_questions():
    questions = SimpleQuestion.objects.filter(correct_answer=4)
    return questions

@login_required(login_url="login")
def test_view(request, theme_id):
    if request.user.is_authenticated:
        print("Пользователь зашел")
        print(request.user.username)
    else:
        print("Пользователь не зашел")

    if request.method == "POST":
        correct_count = 0 # Кол-во правильных ответов
        count = 0 # Кол-во всего ответов
        if theme_id == 1: # Проверка ответов на 1 тест
            print(request.POST)
            for key in request.POST:
                if "question" in key:
                    count += 1
                    if check_test1_answer(key, request.POST[key]):
                        correct_count += 1
        elif theme_id == 2: # Проверка ответов на 2 тест
            pass
        context = {
            "title": "Результаты теста",
            "correct_answer_count": correct_count,
            "question_count": count
        }
        return render(request, "platform/tests/results.html", context)
    else:
        context = {"title": f"Тест на тему {theme_id}"}
        if theme_id == 1:
            questions_send = get_test_theme_1_questions()
            context["questions"] = questions_send
            context["randomList"] = [random.randint(1, 100) for i in range(100)]
            
        if theme_id == 2:
            questions_send = get_test_theme_2_questions()
            context["questions"] = questions_send
            context["randomList"] = [random.randint(1, 100) for i in range(100)]
            context["measures"] = Measure.objects.all().order_by("-pk")
            
        
        return render(request, f"platform/tests/test-theme-{theme_id}.html", context)