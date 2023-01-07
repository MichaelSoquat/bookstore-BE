from django.db import models

class Book(models.Model):
    id = models.AutoField(primary_key=True, unique=True, null=False, blank=False)
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    genre = models.CharField(max_length=100)
    buyed_at = models.DateField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    is_read = models.BooleanField()
    rating = models.IntegerField()
    notice = models.TextField()
    description = models.TextField()
    # user = models.ForeignKey('User', on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class User(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    

    def __str__(self):
        return self.username
