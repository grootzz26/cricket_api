from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Stream(models.Model):
    stream = models.CharField(max_length=50)

    def __str__(self):
        return self.stream

class PlayerDetails(models.Model):
    name = models.ForeignKey(User, on_delete=models.CASCADE, unique=True)
    style = models.ForeignKey(Stream, on_delete=models.CASCADE)
    strike_rate = models.FloatField(default=0)
    economy = models.FloatField(blank=True, null=True)
    fifties = models.IntegerField(default=0)
    hundreds = models.IntegerField(default=0)
    best_wickets = models.IntegerField(default=0)

    def __str__(self):
        return str(self.name) + '--' + str(self.style)

class matchNo(models.Model):
    match = models.CharField(max_length=50)

    def __str__(self):
        return self.match

class matchDetails(models.Model):
    match_no = models.ForeignKey(matchNo, on_delete=models.CASCADE, related_name='matchNo', null=True)
    player = models.ForeignKey(User, on_delete=models.CASCADE)
    runs = models.IntegerField(blank=True, null=True)
    balls = models.IntegerField(blank=True, null=True)
    wickets = models.IntegerField(blank=True, null=True)
    overs = models.FloatField(blank=True, null=True)

    def __str__(self):
        return str(self.match_no)


