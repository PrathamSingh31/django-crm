from django.db import models

# Create your models here.

class Data(models.Model):
    # created_at=models.DateTimeField(auto_now_add=True)
    first_name=models.CharField(max_length=100,null=True)
    last_name=models.CharField(max_length=100,null=True)
    email=models.CharField(max_length=100,null=True)
    phone=models.BigIntegerField(null=True)
    address=models.CharField(max_length=100,null=True)
    city=models.CharField(max_length=100,null=True)
    state=models.CharField(max_length=100,null=True)


    def __str__(self):
        return f'{self.first_name} {self.last_name}'