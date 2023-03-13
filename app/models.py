from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator,MinValueValidator

PROVINCE_CHOICES=(
    ('PROVINCE 1','PROVINCE 1'),
    ('PROVINCE 2','PROVINCE 2'),
    ('PROVINCE 3','PROVINCE 3'),
    ('PROVINCE 4','PROVINCE 4'),
    ('PROVINCE 5','PROVINCE 5'),
    ('PROVINCE 6','PROVINCE 6'),
    ('PROVINCE 7','PROVINCE 7'),
)

class Customer(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    name=models.CharField(max_length=200)
    locality=models.CharField(max_length=200)
    city=models.CharField(max_length=200)
    zipcode=models.IntegerField()
    state=models.CharField(choices=PROVINCE_CHOICES,max_length=50)

    def __str__(self):
        return str(self.id)
        
    

