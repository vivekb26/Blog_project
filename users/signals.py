from django.db.models.signals import post_save #method to create
from django.contrib.auth.models import User # user as sender
from django.dispatch import receiver
from .models import profile

@receiver(post_save, sender=User) #receiver decoratoe which takes post save signal from sender (User)
def create_profile(sender,instance , created,**kwargs):#create profile is receiver with given arguments
    if created: #when user is created
        profile.objects.create(user=instance)  #Profile gets created


#save profile section whenever user objects get save performed this 
@receiver(post_save,sender=User)
def save_profile(sender,instance,**kwargs): #kwargs takes any additional arguments
    instance.profile.save() 

