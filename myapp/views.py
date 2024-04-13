from django.shortcuts import render, redirect
from myapp.models import User
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User

'''user = User.objects.create_user('Admin', 'admin@mail.com', '123')

user.first_name = 'John'
user.last_name = 'Citizen'
user.save()'''


def index_page(request):
    return render(request, 'index.html')


def reg_page(request):
    if request.method == 'POST':

        new_user = User.objects.create_user(request.POST.get("username"), request.POST.get("email"), request.POST.get("password"))

        new_user.save()

    return render(request, 'reg.html')


def auth_page(request):
    if request.method == 'POST':
        username = request.POST.get("username")
        password = request.POST.get("password")

        print("Введенное имя пользователя:", username)
        print("Введенный пароль:", password)

        user = authenticate(request, username=username, password=password)  # Сама проверка, есть ли пользователь в БД
        print("Результат аутентификации:", user)

        if user is not None:
            # Если пользователь найден, выполняем вход
            login(request, user)
            # Перенаправляем пользователя на другую страницу после успешной аутентификации
            return redirect('home')  # Перекидывает на страницу успешной авторизации, если успешно
        else:

            error_message = 'Неверное имя пользователя или пароль'  # сообщение, если пользователь не найден

    return render(request, 'login.html', {'error_message': error_message if 'error_message' in locals() else ''})
