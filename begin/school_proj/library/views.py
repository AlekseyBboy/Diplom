from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User
from django.contrib import messages
from .models import Book, Reservation, User
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from datetime import timedelta





def index(request):
    return render(request, 'library/index.html')


def list(request):
    books = Book.objects.all()
    return render(request, 'library/book_list.html', {'books': books})


def log(request):
    return render(request, 'library/login.html')


def det(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    return render(request, 'library/book_detal.html', {'book': book})


def helper(request):
    return render(request, 'library/helper.html')


class RegisterView(View):
    def get(self, request):
        return render(request, 'library/register.html')

    def post(self, request):
        email = request.POST['email']
        password = request.POST['password']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        if User.objects.filter(email=email).exists():
            messages.error(request, 'Пользователь с данной почтой уже существует')
            return render(request, 'register.html')

        user = User.objects.create_user(
            username=email,
            email=email,
            password=password,
            first_name=first_name,
            last_name=last_name
        )
        messages.success(request, 'Вы успешно зарегистрировались')
        return redirect('login')


class LoginView(View):
    def get(self, request):
        return render(request, 'library/login.html')

    def post(self, request):
        email = request.POST['email']
        password = request.POST['password']

        user = authenticate(request, username=email, password=password)

        if user is not None:
            login(request, user)
            return redirect('profile')
        else:
            messages.error(request, 'Неверно указана почта или пароль')
            return render(request, 'login.html')


class ProfileView(View):
    def get(self, request):
        if not request.user.is_authenticated:
            return redirect('login')
        else:
            return render(request, 'library/profile.html', {'user': request.user})


@login_required
def reserve_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    if book.available > 0:
        Reservation.objects.create(
            user=request.user,
            book=book,
            expire_date=timezone.now() + timedelta(days=14)
        )
        book.available -= 1
        book.save()
        return HttpResponseRedirect(reverse('profile'))
    return HttpResponse("Книг нет в наличии")
