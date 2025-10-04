from django.db import models
from django.contrib.auth.models import User


class Author(models.Model):
    name = models.CharField(max_length=100)
    bio = models.CharField(blank=True)

    def __str__(self):
        return self.name


class Genre(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    genre = models.ForeignKey(Genre, on_delete=models.SET_NULL, null=True)
    all = models.IntegerField(default=1)
    available = models.IntegerField(default=1)

    def __str__(self):
        return f"{self.title} - {self.author.name}"


class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    group = models.CharField(max_length=10)

    def __str__(self):
        return f"{self.user.get_full_name()} ({self.group})"


class Borrow(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    bor_date = models.DateField(auto_now_add=True)
    get_date = models.DateField()
    ret_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"{self.student} - {self.book}"

