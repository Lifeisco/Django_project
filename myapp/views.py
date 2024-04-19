from django.db.models import Q
from django.shortcuts import render, redirect
from myapp.models import User, Category, Ad
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.core.mail import send_mail


'''user = User.objects.create_user('Admin', 'admin@mail.com', '123')

user.first_name = 'John'
user.last_name = 'Citizen'
user.save()'''




def index_page(request):
    return render(request, 'index.html')


def reg_page(request):
    if request.method == 'POST':
        new_user = User.objects.create_user(request.POST.get("username"), request.POST.get("email"), request.POST.get("password"))
        new_user.is_active = False
        new_user.save()

    return render(request, 'reg.html')


def auth_page(request):
    if request.method == 'POST':
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)  # Сама проверка, есть ли пользователь в БД

        if user is not None:
            # Если пользователь найден, выполняем вход
            login(request, user)
            # Перенаправляем пользователя на другую страницу после успешной аутентификации
            return redirect('/')  # Перекидывает на страницу успешной авторизации, если успешно
        else:

            error_message = 'Неверное имя пользователя или пароль'  # сообщение, если пользователь не найден

    return render(request, 'login.html', {'error_message': error_message if 'error_message' in locals() else ''})

def log_out(request):
    logout(request)
    return redirect('/')

def create_ad(request):
    if request.user.id:

        if request.method == 'POST':

            title = request.POST.get('title')
            text = request.POST.get('text')
            category = request.POST.get('category')

            Ad.objects.create(title=title, text=text, category_id=Category.objects.get(id=category), user_id=request.user.id)


        categories = Category.objects.all()
        data = {'categories': categories, 'user': request.user.id}
    else:
        data = {'user': request.user.id}
    return render(request, "content.html", context=data)

def view_ad(request):
    ads = Ad.objects.filter(~Q(user_id=request.user.id))
    data = {'ads': ads}

    return render(request, "ads.html", context=data)