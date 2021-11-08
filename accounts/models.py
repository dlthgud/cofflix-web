from django.db import models

# Create your models here.


class User(models.Model):
    userId = models.CharField(max_length=11)
    userPw = models.CharField(max_length=20)
    userEmail = models.EmailField(max_length=128, blank=False)

    def __str__(self):
        return f'{self.userId}: {self.userPw}: {self.userEmail}'
