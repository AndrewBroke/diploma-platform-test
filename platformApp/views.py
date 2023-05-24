from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect

from .models import *
import random

# Create your views here.
def index(request):
    themes = Theme.objects.all()

    context = {
        "title": "Platform",
        "themes": themes,
        "profile": Profile.objects.get(user=request.user)
    }
    return render(request, "platform/index.html", context)

def redirect_view(request):
    response = redirect('/platformApp')
    return response


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
    questions1 = SimpleQuestion.objects.filter(correct_answer=4)
    questions2 = SimpleQuestion.objects.filter(correct_answer=5)
    return (questions1 | questions2)[:2]

def get_test_theme_4_questions():
    q1 = SimpleQuestion.objects.get(pk = 28)
    q2 = SimpleQuestion.objects.get(pk = 29)
    q3 = SimpleQuestion.objects.get(pk = 30)
    q4 = SimpleQuestion.objects.get(pk = 31)
    q5 = SimpleQuestion.objects.get(pk = 32)
    return [q1, q2, q3, q4, q5]


def check_test_2_answers(post):
    count = 0
    correct_count = 0

    for key in post:
        if not "question" in key and not "measure" in key:
            continue
        
        if "question" in key and not "measure" in key:
            count += 1
            question_id = int(key.split("-")[1])
            answer_id = int(post[key])
            # Проверка простого ответа
            try:
                q = SimpleQuestion.objects.get(pk=question_id)
                if q.correct_answer.pk == answer_id:
                    # Первый ответ верный
                    for key1 in post:
                        if "measure" in key1:
                            measure_question = int(key1.split("-")[-1])
                            if measure_question == question_id:
                                measure_id = int(post[key1])
                                relation = Test2Relations.objects.get(question=q)
                                if measure_id == relation.measure.pk:
                                    correct_count += 1
                    
            except Exception as e:
                pass
    return (count, correct_count)

def check_test_3_answers(post):
    flag = SimpleQuestion.objects.get(pk=33).correct_answer.text
    if "flag" not in post:
        return (1, 0)
    recieved_flag = post["flag"]
    if flag == recieved_flag:
        return (1, 1)
    else:
        return (1, 0)

def check_test_5_answers(post):
    flag = SimpleQuestion.objects.get(pk=34).correct_answer.text
    if "flag" not in post:
        return (1, 0)
    recieved_flag = post["flag"]
    if flag == recieved_flag:
        return (1, 1)
    else:
        return (1, 0)
    
def check_test_4_answers(post):
    count = 0
    correct_count = 0
    for key in post:
        if "question" in key:
            count += 1
            question_id = key.split("-")[-1]
            try:
                question = SimpleQuestion.objects.get(pk=question_id)
                if post[key] == question.correct_answer.text:
                    correct_count += 1
            except Exception as e:
                continue
    return (count, correct_count)

def set_test_results(user, results):
    profile = Profile.objects.get(user=user)
    tests = profile.tests
    if tests == None:
        tests = {}
        tests[results["theme_name"]] = f"{results['correct_count']}/{results['count']}"
        profile.tests = tests
        profile.save()
    
    if results["theme_name"] in tests:
        return
    
    tests[results["theme_name"]] = f"{results['correct_count']}/{results['count']}"
    profile.tests = tests
    profile.save()

@login_required(login_url="login")
def test_view(request, theme_id):
    if request.method == "POST":
        correct_count = 0 # Кол-во правильных ответов
        count = 0 # Кол-во всего ответов
        if theme_id == 1: # Проверка ответов на 1 тест
            
            for key in request.POST:
                if "question" in key:
                    count += 1
                    if check_test1_answer(key, request.POST[key]):
                        correct_count += 1
        elif theme_id == 2: # Проверка ответов на 2 тест
            count, correct_count = check_test_2_answers(request.POST)
        elif theme_id == 3: # Проверка ответов на 3 тест
            count, correct_count = check_test_3_answers(request.POST)
        elif theme_id == 4: # Проверка ответов на 4 тест
            count, correct_count = check_test_4_answers(request.POST)
        elif theme_id == 5:
            count, correct_count = check_test_5_answers(request.POST)

        context = {
            "title": "Результаты теста",
            "correct_answer_count": correct_count,
            "question_count": count
        }
        set_test_results(request.user, {"count": count, "correct_count": correct_count, "theme_name": Theme.objects.get(pk=theme_id).name})
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
        if theme_id == 4:
            questions_send = get_test_theme_4_questions()
            context["questions"] = questions_send
            
        
        return render(request, f"platform/tests/test-theme-{theme_id}.html", context)
    

def theory_view_test(request):
    context = {
        "title": "Теория проверка"
    }
    return render( request, "platform/theory/theory-test.html", context)

def theory_view(request, theme_id):
    theory = Theory.objects.get(pk=theme_id)
    context = {
        "title": theory.theme.name,
        "theory": theory
    }
    return render(request, "platform/theory/theory.html", context)