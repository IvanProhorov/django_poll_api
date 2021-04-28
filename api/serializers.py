from rest_framework import serializers

from .models import Vote, Choice, Poll


class VoteSerializer(serializers.ModelSerializer):
    class Meta:
        fields = "__all__"
        model = Vote


class ChoiceSerializer(serializers.ModelSerializer):
    class Meta:
        fields = "__all__"
        model = Choice


class PollSerializer(serializers.ModelSerializer):
    class Meta:
        fields = "__all__"
        model = Poll
