from django.shortcuts import render, redirect #for template rendering
from .forms import SignUpForm, LoginForm #importing from forms.py
from django.contrib.auth import authenticate, login #import for authentication and loging user in

#Function based view

def signup_view(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
            user = authenticate(request, email=email, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                form.add_error(None, "Username or password is incorrect")
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})

def homepage(request):
    
    context = {
        name: "firstname",
        msg : "Welcome to the Homepage"
    }

    return render(request, 'home.html', context)