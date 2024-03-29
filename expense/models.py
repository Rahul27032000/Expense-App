from django.db import models
from django.contrib.auth.models import User

# Create your models here.
TYPE = (
    ("Positive",'Positive'),
    ('Negative','Negative')
    )


class Expense(models.Model):
    name = models.CharField(max_length=100)
    expense_type = models.CharField(max_length=8, choices=TYPE)
    amount = models.FloatField()
    user = models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    

class Profile(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    income = models.FloatField()
    expenses = models.FloatField(blank=True,default=0)
    balance = models.FloatField(blank=True,null=True)