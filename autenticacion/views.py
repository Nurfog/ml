from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User


def login_page(request):
    # Chequea que el método HTTP sea POST (formulario de envío)
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        # Chequea que el usuario y la contraseña sean válidos
        if not User.objects.filter(username=username).exists():
            # Muestra un mensaje de error si el usuario no existe
            messages.error(request, 'Usuario no encontrado')
            return redirect('/login/')
        
        # Autenticar al usuario con el nombre de usuario y contraseña proporcionados
        user = authenticate(username=username, password=password)
        
        if user is None:
            # Muestra un mensaje de error si la autenticación falla (usuario no encontrado o contraseña incorrecta)
            messages.error(request, "Contraseña Incorrecta")
            return redirect('/login/')
        else:
            # Inicializa la sesión y redirecciona a la página dashboard
            login(request, user)
            return redirect('dashboardcms')
    
    # Renderiza la página de inicio de sesión (GET request)
    return render(request, 'autenticacion/account/login.html')

# Define la vista para la página de registro
def register_page(request):
    # Chequea que el método HTTP sea POST (formulario de envío)
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        # Chequea que el usuario y la contraseña sean válidos
        user = User.objects.filter(username=username)
        
        if user.exists():
            # Muestra un mensaje de información si el usuario ya existe
            messages.info(request, "Usuario ya existe!")
            return redirect('/register/')
        
        # Crea un nuevo usuario con los datos proporcionados
        user = User.objects.create_user(
            first_name=first_name,
            last_name=last_name,
            username=username
        )

        # Asigna la contraseña al usuario y guarda el objeto de usuario
        user.set_password(password)
        user.save()
        
        # Muestra un mensaje de información confirmando la creación del usuario
        messages.info(request, "Cuenta creada correctamente!")
        return redirect('autenticacion//account/register/')
    
    # renderiza la pagina de registro (GET request)
    return render(request, 'autenticacion/account/register.html')

def logout_page(request):
    logout(request)
    messages.info(request, '¡Has cerrado sesión correctamente!')
    return redirect('index')

def profile_page(request):
    return render(request, 'autenticacion/account/profile.html')

def edit_profile(request):
    return render(request, 'autenticacion/account/edit_profile.html')

def change_password(request):
    return render(request, 'autenticacion/account/change_password.html')

