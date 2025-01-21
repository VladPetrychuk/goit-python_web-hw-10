from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import RegistrationForm
from django.contrib.auth.decorators import login_required
from .models_mongo import Author

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('quotes:index')
    else:
        form = RegistrationForm()
    return render(request, 'quotes/register.html', {'form': form})

@login_required
def add_author(request):
    if request.method == 'POST':  # Користувач надіслав дані
        fullname = request.POST.get('fullname')
        born_date = request.POST.get('born_date')
        born_location = request.POST.get('born_location')
        description = request.POST.get('description')

        # Створюємо нового автора
        author = Author(
            fullname=fullname,
            born_date=born_date,
            born_location=born_location,
            description=description
        )
        author.save()  # Зберігаємо в MongoDB
        return redirect('quotes:author_list')  # Переходимо до списку авторів

    return render(request, 'quotes/add_author.html')  # Виводимо форму