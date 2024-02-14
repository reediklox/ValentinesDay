from django.db import models


class User(models.Model):
    login = models.CharField(max_length=16, unique=True)

class ValentineMessage(models.Model):
    
    __CHOICES__ = {'y': "Yes", 'n': "NO"}
    
    sender = models.ForeignKey(User, on_delete=models.CASCADE)
    question = models.CharField(max_length=100)
    recipient_name = models.CharField(max_length=16)
    answer = models.CharField(max_length=100, null=True, default=None)
    
    @property
    def recipient(self):
        return User.objects.get(login=self.recipient)