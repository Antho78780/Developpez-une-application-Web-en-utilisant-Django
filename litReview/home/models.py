from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from account.models import User


class Ticket(models.Model):
    title = models.CharField(max_length=128, verbose_name='Title')
    description = models.TextField(max_length=128, blank=True, verbose_name='Description')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(null=True, blank=True)
    time_created = models.DateTimeField(auto_now_add=True)
    


class Review(models.Model):
    ticket = models.ForeignKey(to=Ticket, on_delete=models.CASCADE)
    rating = models.PositiveSmallIntegerField(
        # validates that rating must be between 0 and 5
        validators=[MinValueValidator(0), MaxValueValidator(5)], verbose_name='Rating')
    headline = models.CharField(max_length=128, verbose_name='Headline')
    body = models.CharField(max_length=8192, blank=True, verbose_name='Title')
    user = models.ForeignKey(
        User, on_delete=models.CASCADE)
    time_created = models.DateTimeField(auto_now_add=True)


class UserFollows(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='following')
    followed_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='followed_by')

    class Meta:
        unique_together = ('user', 'followed_user', )
    
    def __str__(self) -> str:
        return f"{self.user} - {self.followed_user}"
