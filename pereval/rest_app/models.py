from django.db import models


class User(models.Model):
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=255)
    family = models.CharField(max_length=255)
    phone = models.CharField(unique=True)


class Coordinates(models.Model):
    latitude = models.FloatField()  # широта
    longitude = models.FloatField()  # долгота
    height = models.IntegerField()


class Level(models.Model):
    winter = models.TextField()
    spring = models.TextField()
    summer = models.TextField()
    autumn = models.TextField()


class Pereval(models.Model):
    STATUS = [
        ('new', 'new'),
        ('pending', 'pending'),
        ('accepted', 'accepted'),
        ('rejected', 'rejected')
    ]

    coordinates = models.OneToOneField(Coordinates, on_delete=models.CASCADE)
    user_added = models.ForeignKey(User, on_delete=models.CASCADE)
    level = models.ForeignKey(Level, on_delete=models.CASCADE)
    status = models.CharField(choices=STATUS, default='new')
    date = models.DateTimeField(auto_now=True)
    beauty_title = models.TextField()
    title = models.TextField()
    other_titles = models.TextField()
    connect = models.TextField()


class Images(models.Model):
    pereval = models.ForeignKey(Pereval, on_delete=models.CASCADE)
    title = models.TextField()
    data = models.CharField()
