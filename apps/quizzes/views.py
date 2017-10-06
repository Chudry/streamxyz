
from django.shortcuts import render

# Create your views here.
from django.views import View
from django.core.cache import cache


from quizzes.models import QuizModel, QuestionModel, AnswerModel
from subscribers.models import SubscriberModel


class QuizList(View):

    def get(self, request):
        context = {
            'quizzes': QuizModel.objects.filter(
                private=False, blacklist=False)[0:50]
        }
        return render(request, 'quizzes/list.html', context)


class QuizDetail(View):

    def get(self, request, pk, slug):
        quiz = QuizModel.objects.get(id=pk)
        question_qs = QuestionModel.objects.filter(quiz=quiz)
        answers = None
        questions = [(question, answers) for question in question_qs]
        client_address = request.META.get('REMOTE_ADDR', None)
        if client_address:
            hit_key = '%s-%s-%s' % (client_address, 'quiz', quiz.id)
            if cache.get(hit_key, None) is None:
                quiz.views = quiz.views + 1
                quiz.save()
                cache.set(hit_key, '1', 60*60*1)  # 1 hour

        context = {
            'quiz': quiz,
            'questions': questions
        }

        return render(request, 'quizzes/detail.html', context)

    def post(self, request, pk, slug):

        quiz = QuizModel.objects.get(id=pk)
        question_qs = list(QuestionModel.objects.filter(quiz=quiz))
        score = 0
        questions = []

        email = request.POST.get('email', '')
        name = request.POST.get('name', '')
        interest = request.POST.get('interest', '')

        for question in question_qs:
            answers = {}
            option_a_answer = request.POST.get(
                'question_%s_option_a_answer' % question.order_index) == 'on'
            option_b_answer = request.POST.get(
                'question_%s_option_b_answer' % question.order_index) == 'on'
            option_c_answer = request.POST.get(
                'question_%s_option_c_answer' % question.order_index) == 'on'
            option_d_answer = request.POST.get(
                'question_%s_option_d_answer' % question.order_index) == 'on'

            if (question.option_a_correct == option_a_answer and
                    question.option_b_correct == option_b_answer and
                    question.option_c_correct == option_c_answer and
                    question.option_d_correct == option_d_answer):
                score = score + 1

            answers = {
                'option_a_answer': option_a_answer,
                'option_b_answer': option_b_answer,
                'option_c_answer': option_c_answer,
                'option_d_answer': option_d_answer
            }
            questions.append((question, answers))

        if email:
            AnswerModel.objects.create(
                quiz=quiz,
                email=email,
                score=score)
            SubscriberModel.objects.create(
                email=email,
                name=name,
                interest=interest)
        context = {
            'show_answer': True,
            'answers': answers,
            'score': score,
            'quiz': quiz,
            'questions': questions
        }

        return render(request, 'quizzes/detail.html', context)
