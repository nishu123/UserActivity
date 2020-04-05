from django.db import models
from django.conf import settings


class Activity_Periods(models.Model):
    start_time=models.DateTimeField(null=True, blank=True)
    end_time=models.DateTimeField(null=True, blank=True)


class Members(models.Model):
    userid = models.CharField(max_length=256, blank=False,primary_key=True)
    real_name = models.CharField(max_length=256, blank=True)
    tz = models.CharField(max_length=256, blank=True)
    activity_periods = models.ManyToManyField("Activity_Periods", blank=True, related_name="activity_periods")

