from django.db import models

# Create your models here.
class Brand(models.Model):
    title = models.CharField(max_length=500, null=False, blank=False)
    public_key = models.CharField(max_length=250)
    private_key = models.CharField(max_length=250)

class Relay(models.Model):
    title = models.CharField(max_length=500)
    uri = models.CharField(max_length=1000)

class Post(models.Model):
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    nostr_id = models.CharField(max_length=500)

class Blog(models.Model):
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    nostr_id = models.CharField(max_length=500)