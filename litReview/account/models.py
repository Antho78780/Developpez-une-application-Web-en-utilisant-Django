from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    username = models.CharField(max_length=40, unique=True)
    followed = models.ManyToManyField("self", through="flux.UserFollows",through_fields=["followed_user", "user",], symmetrical=False)
    
    USERNAME_FIELD = "username"