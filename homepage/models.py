from django.db import models
from django.contrib.auth.models import User
# Create your models here.


CHOICES = (
    ("DRAMA","DRAMA"),
    ("ANIMATION","ANIMATION"),
    ("SERIES","SERIES"),
    ("TV SHOW","TV SHOW"),
)


class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    pic = models.ImageField(upload_to='profile')
    date = models.DateTimeField(auto_now_add=True)
    
    
    def __str__(self) -> str:
        return f'user: {self.user.username} date:{self.date}'




class Movie(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='image')
    video = models.FileField(upload_to='movie')
    
    
    def __str__(self) -> str:
        return f'USER :{self.title}'
    







class Comments(models.Model):
    post = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie,on_delete=models.CASCADE)
    
    
    
    def __str__(self) -> str:
        return f'user {self.user.username} movie: {self.movie.title} comment:{self.post}'









