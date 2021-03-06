from rest_framework import serializers
from board.models import Meeting, Reply

class MeetingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Meeting
        fields = [
            'pk',
            'visitor',
            'manager',
            'meetingDate',
            'contact',
            'comment',
            'location'
        ]