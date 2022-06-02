from django.db import models


# Create your models here.

class Person(models.Model):
    name = models.CharField(max_length=20)
    age = models.IntegerField()


'''One to Many'''


class Company(models.Model):
    name = models.CharField(max_length=30)


class Product(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    name = models.CharField(max_length=20)
    price = models.IntegerField()


'''Many to many'''


class Course(models.Model):
    name = models.CharField(max_length=20)


class Student(models.Model):
    name = models.CharField(max_length=20)
    courses = models.ManyToManyField(Course)


'''One to one'''


class User(models.Model):
    name = models.CharField(max_length=30)


class Account(models.Model):
    login = models.CharField(max_length=20)
    password = models.CharField(max_length=13)
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
