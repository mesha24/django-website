
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.



class post(models.Model) :

    title =  models.SlugField(max_length=200,unique=True)
    content = models.TextField()
    date =models.DateTimeField(default=timezone.now)
    author =models.ForeignKey(User, on_delete=models.CASCADE)


    class Meta:
        db_table = 'post'

    def _str_(self):
        return self.title



