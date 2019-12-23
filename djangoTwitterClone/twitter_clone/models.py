from django.db import models

# Create your models here.

class Tweet(models.Model):
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    text = models.CharField(max_length=160)
    created_at = models.DateTimeField(auto_now_add=True)

class Follow(models.Model):
    user = models.ForeignKey('auth.User', related_name='friends', on_delete=models.CASCADE)
    target = models.ForeignKey('auth.User', related_name='followers',
                               on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'target')
