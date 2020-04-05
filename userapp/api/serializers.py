from rest_framework import serializers
from userapp.models import *




class Activity_PeriodsSerializer(serializers.ModelSerializer):

    class Meta:
        exclude = ('id',)
        model = Activity_Periods

class MembersSerializers(serializers.ModelSerializer):

    class Meta:
        fields = ['userid','real_name','tz','activity_periods']
        model = Members
    activity_periods = Activity_PeriodsSerializer(read_only=True, many=True)


