from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.conf import settings
from .forms import PerfilForm
from autenticacion.models import Profile
from cms.models import Pais, Region, Comuna
from django.contrib.auth.decorators import login_required



def login_page(request):
    # Chequea que el método HTTP sea POST (formulario de envío)
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(settings.BASE_DIR)
        
        # Chequea que el usuario y la contraseña sean válidos
        if not User.objects.filter(username=username).exists():
            # Muestra un mensaje de error si el usuario no existe
            messages.error(request, 'Usuario no encontrado')
            return redirect('cuentas')
        
        # Autenticar al usuario con el nombre de usuario y contraseña proporcionados
        user = authenticate(username=username, password=password)
        
        if user is None:
            # Muestra un mensaje de error si la autenticación falla (usuario no encontrado o contraseña incorrecta)
            messages.error(request, "Contraseña Incorrecta")
            return redirect('cuentas')
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
        return redirect('cuentas')
    
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

@login_required
def graba_perfil(request):
    usuario = User.objects.get(id=request.user.id)
    profiles = Profile.objects.get(usuario=usuario.id)
    if request.method == 'POST':
        form = PerfilForm(request.POST, instance=request.user.profile)
        if form.is_valid():
            form.save()
            return redirect('perfil')
    else:
        form = PerfilForm(instance=request.user.profile)
    context = {
        'form': form,
        'profiles': profiles,
        'usuario': usuario,
    }
    return render(request, 'cms/pages/mostrar_perfil.html', context)

@login_required
def mostrar_perfil(request, username):
    usuario = User.objects.get(username=username)
    profiles = Profile.objects.get(usuario=usuario.id)
    if request.user.is_authenticated:
        try:
            profiles = Profile.objects.get(usuario=request.user.id)
            usuario = User.objects.get(id=request.user.id)
            if profiles.id_region_id is None:
                regiones = None
            else:
                regiones = Region.objects.get(id=profiles.id_region_id)
            if profiles.id_comuna_id is None:
                comunas = None
            else:
                comunas = Comuna.objects.get(id=profiles.id_comuna_id)

            if profiles.id_pais_id is None:
                paises = None
            else:
                paises = Pais.objects.get(id=profiles.id_pais_id)
        except Profile.DoesNotExist:
            profiles.id_region_id = None
            profiles.id_comuna_id = None
            profiles.id_pais_id = None

        context = {
            'profiles': profiles,
            'usuario': usuario,
            'regiones': regiones,
            'comunas': comunas,
            'paises': paises,
        }
        return render(request, 'cms/pages/mostrar_perfil.html', context)
    else:
        # Si el usuario no está autenticado, redirigir a la página de inicio de sesión
        return redirect('cuentas')
    
@login_required
def editar_perfil(request, id):
    usuario = User.objects.get(id=request.user.id)
    profiles = Profile.objects.get(usuario=usuario.id)
    perfil = Profile.objects.get(id=id)
    if request.method == 'POST':
        form = PerfilForm(request.POST, request.FILES, instance=perfil)
        if form.is_valid():
            form.save()
            return redirect('dashboardcms')
    else:
        form = PerfilForm(instance=perfil)
    context = {
        'form': form,
        'perfil': perfil,
        'profiles': profiles,
        'usuario': usuario,
    }
    return render(request, 'cms/pages/editar_perfil.html', context)