from django.db import models
from apps.titles.models import Title
from django.contrib.auth.models import User


class UserRate(models.Model):
    rate = models.IntegerField()
    title_id = models.ForeignKey(Title, on_delete=models.CASCADE, related_name='rates')
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name='rates')
