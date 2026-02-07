from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now

# Create your models here.


class Post(models.Model):
    sno=models.AutoField(primary_key=True)
    title=models.CharField(max_length=255)
    author=models.CharField(max_length=14)
    views=models.IntegerField(default=0)
    slug=models.CharField(max_length=130)
    timeStamp=models.DateTimeField(blank=True)
    time = models.TimeField(auto_now_add=True)
    thumbnail = models.CharField(max_length=200, blank=True, null=True)
    content=models.TextField()

    def __str__(self):
        return self.title + " by " + self.author



class BlogComment(models.Model):
    sno= models.AutoField(primary_key=True)
    comment=models.TextField()
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    post=models.ForeignKey(Post, on_delete=models.CASCADE)
    parent=models.ForeignKey('self',on_delete=models.CASCADE, null=True )
    timestamp= models.DateTimeField(default=now)
    
    def __str__(self):
        return self.comment[0:13] + "..." + " by" + " " + self.user.username
    
from django.contrib.auth.models import User
from django.db import models

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.CharField(max_length=200, default="avatars/user.png")

    def __str__(self):
        return self.user.username


# AUTO CREATE PROFILE
from django.db.models.signals import post_save
from django.dispatch import receiver

@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
