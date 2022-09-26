from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm

def register(request):
    if request.method != 'POST':
        # Return empty form
        form = UserCreationForm()
    else:
        # Processing filled form
        form = UserCreationForm(data=request.POST)
        
        if form.is_valid():
            new_user = form.save()
            # Entering and redirect to home page
            login(request, new_user)
            return redirect('learning_logs:index')
    
    # Return empty form in response to invalid data
    context = {'form': form}
    return render(request, 'registration/register.html', context)