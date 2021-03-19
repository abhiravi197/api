from django.db import models
from django.contrib.auth.models import User



class Profile(models.Model):
    name=models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    age=models.IntegerField()
    phone=models.CharField(max_length=10)
    address=models.TextField(max_length=200)

    def __str__(self):
        return self.name.username

class post(models.Model):
    title=models.CharField(max_length=50)
    content=models.TextField(max_length=5000)
    author=models.ForeignKey(Profile,on_delete=models.CASCADE,null=True)
    publish=models.DateField(auto_now=True)


    def __str__(self):
        return self.title
