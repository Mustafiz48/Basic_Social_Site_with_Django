from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

# Create your models here.
class Message(models.Model):
    author = models.ForeignKey(User, related_name='author_messages', on_delete=models.CASCADE)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.author.user.username


    def last_10_messages():
        return Message.object.order_by('-timestamp').all()[:10]
