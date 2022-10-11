from django.db import models
  
GENDER=[
    ('male','male'),
    ('female','female'),
    ('other','other'),
]
class Register(models.Model):
    name=models.CharField(max_length=30)
    address=models.TextField(max_length=50)
    gender=models.TextField(choices=GENDER)
    email=models.CharField(max_length=30)
    phone=models.IntegerField(max_length=10)
    def __str__(self):
        return str(self.name)
class Products(models.Model):
    product=models.CharField(max_length=20)
    price=models.IntegerField(max_length=10)
    desc=models.TextField(max_length=100)
    image=models.CharField(max_length=200)
    def __str__(self):
        return str(self.product)




