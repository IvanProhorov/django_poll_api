from django.urls import path, include

from .views import (ChoicesView, PollsView, VotesView)

api_v1 = [
    path('votes/<int:user_id>/', VotesView.as_view(), name='get_votes'),
    path('choices/<int:choice_id>/', ChoicesView.as_view(),
         name='get_choices'),
    path('polls/<int:poll_id>/', PollsView.as_view(), name='get_polls'),

]
urlpatterns = [
    path('v1/', include(api_v1)),
]
