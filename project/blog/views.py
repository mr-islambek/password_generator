from django.shortcuts import render

from django.shortcuts import render, redirect
from .forms import PasswordGeneratorForm
from .utils import generate_password
from .models import GeneratedPassword

def password_generator(request):
    if request.method == 'POST':
        form = PasswordGeneratorForm(request.POST)
        if form.is_valid():
            length = form.cleaned_data['length']
            include_letters = form.cleaned_data['include_letters']
            include_numbers = form.cleaned_data['include_numbers']
            include_symbols = form.cleaned_data['include_symbols']

            password = generate_password(length, include_letters, include_numbers, include_symbols)

            # Сохранение в базе данных
            generated_password = GeneratedPassword(password=password)
            generated_password.save()

            return render(request, 'password_generator.html', {'password': password})
    else:
        form = PasswordGeneratorForm()

    return render(request, 'password_generator.html', {'form': form})


