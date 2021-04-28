import json

from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.views import View

from api.models import Poll, Vote, Choice
from api.serializers import VoteSerializer, ChoiceSerializer, PollSerializer


class ChoicesView(View):
    def post(self, request):
        req = json.loads(request.body)
        choices_id = req.get('id')
        if choices_id is not None:
            choice = get_object_or_404(Choice, pk=choices_id)
            _, created = Choice.objects.get_or_create(
                user=request.user.id, choice=choice)
            return JsonResponse({'success': created})
        return JsonResponse({'success': False}, status=400)

    def get(self, request, choice_id):
        if choice_id is not None:
            choices = Choice.objects.filter(pk=choice_id)
            serializer = ChoiceSerializer(choices, many=True)
            return JsonResponse(serializer.data, safe=False)
        return JsonResponse({'success': False}, status=400)

    def delete(self, request, choices_id):
        recipe = get_object_or_404(Choice, choice=choices_id,
                                   user=request.user)
        recipe.delete()
        return JsonResponse({'success': True})


class PollsView(View):
    def post(self, request):
        req = json.loads(request.body)
        poll_id = req.get('id')
        if poll_id is not None or request.user.is_superuser:
            poll = get_object_or_404(Poll, pk=poll_id)
            _, created = Poll.objects.get_or_create(
                user=request.user, poll=poll)
            return JsonResponse({'success': created})
        return JsonResponse({'success': False}, status=400)

    def get(self, request, poll_id):
        if poll_id is not None:
            polls = Poll.objects.filter(pk=poll_id)
            serializer = PollSerializer(polls, many=True)
            return JsonResponse(serializer.data, safe=False)
        return JsonResponse({'success': False}, status=400)

    def delete(self, request, poll_id):
        if request.user.is_superuser:
            poll = get_object_or_404(Poll, poll=poll_id,
                                     user=request.user)
            poll.delete()
            return JsonResponse({'success': True})
        return JsonResponse({'success': False}, status=400)


class VotesView(View):
    def get(self, request, user_id):
        if user_id is not None:
            votes = Vote.objects.filter(user__id=user_id)
            serializer = VoteSerializer(votes, many=True)
            return JsonResponse(serializer.data, safe=False)
        return JsonResponse({'success': False}, status=400)
