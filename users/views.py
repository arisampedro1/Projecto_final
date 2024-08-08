from django.shortcuts import redirect, render
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate
from users.forms import UserCreationForm

def login_request(request):
    msg_login = ""
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('Inicio')  # Redirige a la vista de inicio
        msg_login = "Usuario o contraseña incorrectos"
    else:
        form = AuthenticationForm()
    return render(request, "users/login.html", {"form": form, "msg_login": msg_login})

def register(request):
    msg_register = ""
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('Login')  # Redirige al login después del registro exitoso
        else:
            msg_register = "Error en los datos ingresados"
    else:
        form = UserCreationForm()

    return render(request, "users/registro.html", {"form": form, "msg_register": msg_register})