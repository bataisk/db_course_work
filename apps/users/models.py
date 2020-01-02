from django.db import models
from django.contrib.auth.models import User
from apps.titles.models import Title


class UserRate(models.Model):
    rate = models.IntegerField()
    title = models.ForeignKey(Title, on_delete=models.CASCADE, related_name='rates')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='rates')
