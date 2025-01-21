from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import RegistrationForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from quotes.models import Author, Quote

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

@login_required
def add_quote(request):
    if request.method == 'POST':  # Користувач надіслав дані
        text = request.POST.get('quote')
        tags = request.POST.get('tags').split(',')  # Теги через кому
        author_id = request.POST.get('author_id')  # ID автора

        author = Author.objects.get(id=author_id)  # Знаходимо автора

        # Створюємо цитату
        quote = Quote(
            quote=text,
            tags=tags,
            author=author
        )
        quote.save()  # Зберігаємо в MongoDB
        return redirect('quotes:quotes_list')  # Переходимо до списку цитат

    authors = Author.objects.all()  # Виводимо авторів для вибору
    return render(request, 'quotes/add_quote.html', {'authors': authors})

def authors_list(request):
    authors = Author.objects.all()
    return render(request, 'quotes/authors_list.html', {'authors': authors})

def author_detail(request, author_id):
    author = get_object_or_404(Author, id=author_id)
    quotes = author.quotes.all()  # Всі цитати автора
    return render(request, 'quotes/author_detail.html', {'author': author, 'quotes': quotes})

def quotes_list(request):
    quotes = Quote.objects.all()
    return render(request, 'quotes/quotes_list.html', {'quotes': quotes})