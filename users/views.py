from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm

def register(request):
    """Регистрация нового пользователя"""
    if request.method != 'POST':
        # Вывод пустой формы
        form = UserCreationForm()
    else:
        # Обработка заполненной формы
        form = UserCreationForm(data=request.POST)
        
        if form.is_valid():
            new_user = form.save()
            # Выполнение входа и редирект на домашнюю страницу
            login(request, new_user)
            return redirect('learning_logs:index')
    
    # Вывод пустой или недействительной формы
    context = {'form': form}
    return render(request, 'registration/register.html', context)