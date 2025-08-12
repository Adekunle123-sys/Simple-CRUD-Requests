from django.db import models
from user.models import User

# Create your models here.
STATUS = ((0, 'Draft'), (1, 'Publish'))
class Item(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user')
    status = models.IntegerField(choices=STATUS, default=0)
