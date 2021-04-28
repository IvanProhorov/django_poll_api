import datetime

from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Poll(models.Model):
    name = models.CharField(max_length=255, verbose_name='poll name')
    start_date = models.DateField(auto_now_add=True, verbose_name='start date')
    finish_date = models.DateField(default=datetime.date.today(),
                                   verbose_name='finish date')
    description = models.CharField(max_length=1000, verbose_name='description '
                                                                 'pool')

    class Meta:
        verbose_name = "poll"
        verbose_name_plural = "polls"


class Choice(models.Model):
    TEXT = 'T'
    ONE_OPTION = 'O'
    MANY_OPTIONS = 'M'
    QUESTION_ANSWER_CHOICES = (
        (TEXT, 'text'),
        (ONE_OPTION, 'one option'),
        (MANY_OPTIONS, 'many options'),
    )
    text = models.CharField(max_length=255, verbose_name='text question')
    type_choice = models.CharField(max_length=1,
                                   choices=QUESTION_ANSWER_CHOICES,
                                   default=ONE_OPTION)
    text_choice = models.CharField(max_length=255, verbose_name='choice')

    class Meta:
        verbose_name = "choice"
        verbose_name_plural = "choices"


class Vote(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    poll = models.ForeignKey(Poll, on_delete=models.CASCADE)
    choice = models.ForeignKey(Choice, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "vote"
        verbose_name_plural = "votes"

    def __str__(self):
        return f'{self.user.username}-{self.poll.name} -' \
               f' {self.choice.text_choice}'
