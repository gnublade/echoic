from django.db import models

from django.contrib.auth.models import User

class Recording(models.Model):

    url = models.URLField()
    duration = models.FloatField()
    recorded_at = models.DateTimeField(auto_now_add=True)
    recorded_by = models.ForeignKey(User)
