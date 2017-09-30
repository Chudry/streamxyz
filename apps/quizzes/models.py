from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify


class QuizModel(models.Model):
    """ quiz is a collection of questions
    """
    name = models.CharField(max_length=255)
    slug = models.SlugField(default='quiz', max_length=300)
    description = models.TextField(default='')
    keywords = models.CharField(max_length=255, null=True, blank=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User, related_name='user_quizzes')
    private = models.BooleanField(default=False)
    blacklist = models.BooleanField(default=False)
    views = models.IntegerField(default=0)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(QuizModel, self).save(*args, **kwargs)

    def __str__(self):
        return '%s [%s]' % (self.name, self.author)

    class Meta:
        db_table = 'quiz'
        verbose_name = 'Quiz'
        verbose_name_plural = 'Quizzes'
        ordering = ['-views']


class QuestionModel(models.Model):
    """ question """
    QUESTION_TYPES = (
        ('mcq_single', "MCQ with single option correct"),
        ('mcq_multiple', "MCQ with one or more options correct"),
    )

    quiz = models.ForeignKey(QuizModel)

    question = models.TextField(default='')
    question_type = models.CharField(max_length=255, choices=QUESTION_TYPES)

    option_a = models.TextField(default='')
    option_b = models.TextField(default='')
    option_c = models.TextField(default='')
    option_d = models.TextField(default='')

    option_a_correct = models.BooleanField(default=False)
    option_b_correct = models.BooleanField(default=False)
    option_c_correct = models.BooleanField(default=False)
    option_d_correct = models.BooleanField(default=False)

    explanation = models.TextField(default='')

    order_index = models.IntegerField(default=0)

    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):

        if not self.pk:
            count = QuestionModel.objects.filter(
                quiz=self.quiz).count()
            self.order_index = count + 1
        super(QuestionModel, self).save(*args, **kwargs)

    def __str__(self):
        return '%s [%s]' % (self.quiz, self.order_index)

    class Meta:
        db_table = 'question'
        verbose_name = 'Question'
        verbose_name_plural = 'Questions'
        ordering = ['order_index']
