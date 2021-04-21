from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class profile(models.Model):
    user= models.OneToOneField(User,on_delete=models.CASCADE)
    image = models.ImageField(default='Default.jpg', upload_to='Profile_pics')

    def __str__(self):
        return f'{self.user.username} Profile '

    
