from django.db import models
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.contrib.auth.models import User

# Create your models here.

class Profile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE, default='')
    bio = models.TextField()
    avatar = models.ImageField(upload_to="images")
    is_verified = models.BooleanField(default=False)


#@receiver(post_save, sender=User)
#def update_user_profile(sender, instance, created, **kwargs):
 #   if created:
  #      Profile.objects.create(user=instance)
   # instance.profile.save()

class PostedImage(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="images")
    postimgdate = models.DateTimeField()

