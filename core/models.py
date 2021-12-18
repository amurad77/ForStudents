from django.db import models
from django.db.models.fields import CharField

# Create your models here.

class University(models.Model):
    name = models.CharField('Ad', max_length=60)
    date = models.CharField('Tarix', max_length=60)
    description = models.CharField('Melumat', max_length=5000)
    image = models.ImageField(upload_to='media/images')
    university_link = models.CharField('Universitet Link', max_length=100)
    facebook_link = models.CharField('Facebok Link', max_length=100)
    twitter_link = models.CharField('Twitter Link', max_length=100)
    instagram_link = models.CharField('Instagram Link', max_length=100)


    def __str__(self):
        return self.name

class Meqsed(models.Model):
    word = models.CharField('Ad', max_length= 1000)



class Book(models.Model):
    image = models.ImageField(upload_to='media/images')
    name = models.CharField('Ad', max_length=60)
    front_description = models.CharField('On melumat', max_length=500)
    back_description = models.CharField('Arxa melumat', max_length=2000)
    number = models.CharField('Telefon nomresi', max_length=20)

    def __str__(self):
        return self.name



class Project(models.Model):
    image = models.ImageField(upload_to='media/images')
    date = models.CharField('Tarix', max_length=200)
    description = models.CharField('Melumat', max_length=500)
    name = models.CharField('Ad', max_length=100)
    manager = models.CharField('Menecer', max_length=60)
    manager_job = models.CharField('Menecerin isi', max_length=60)
    link = models.CharField('Link', max_length=100)




class Contact(models.Model):
    name = models.CharField('Name', max_length=40)
    number = CharField('Number',max_length=15)
    email = models.EmailField('E-mail', max_length=40)
    message = models.CharField('Mesagge', max_length=256)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name