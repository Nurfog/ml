from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import *
from .forms import *
from autenticacion.models import Profile
from django.http import JsonResponse


@login_required
def dashboardcms(request):
    if request.user.is_authenticated:
        try:
            usuario = User.objects.get(id=request.user.id)
            profiles = Profile.objects.get(usuario=usuario.id)            
        except Profile.DoesNotExist:
            profiles = None

        context = {
            'profiles': profiles,
            'usuario': usuario,
        }
        return render(request, 'cms/pages/dashboard.html', context)
    else:
        # Si el usuario no está autenticado, redirigir a la página de inicio de sesión
        return redirect('cuentas')

@login_required
def crear_pais(request):
    usuario = User.objects.get(id=request.user.id)
    profiles = Profile.objects.get(usuario=usuario.id)
    if request.method == 'POST':
        form = PaisForm(request.POST)
        if form.is_valid():
            form.save()            
            return redirect('lista_paises')
    else: 
        form = PaisForm()
    context = {
        'form': form,
        'profiles': profiles,
        'usuario': usuario,
    }
    return render(request, 'cms/pages/crear_pais.html', context)

@login_required
def lista_paises(request):
    if request.user.is_authenticated:        
        usuario = User.objects.get(id=request.user.id)
        profiles = Profile.objects.get(usuario=usuario.id)        
        paises = Pais.objects.all()
        if paises is None:
            paises = None
        
        context = {
            'profiles': profiles,
            'usuario': usuario,
            'paises': paises,
            
        }
    return render(request, 'cms/pages/lista_paises.html', context)

@login_required
def editar_pais(request, id):
    usuario = User.objects.get(id=request.user.id)
    profiles = Profile.objects.get(usuario=usuario.id)
    paix = get_object_or_404(Pais, id=id)
    if request.method == 'POST':
        form = PaisForm(request.POST, instance=paix)
        if form.is_valid():
            # Las transformaciones deberían estar en el método `clean` del formulario
            form.save()  # Guarda los cambios en la instancia
            return redirect('lista_paises')
    else:
        form = PaisForm(instance=paix)

    context = {
        'form': form,
        'pais': paix,
        'profiles': profiles,
        'usuario': usuario,
    }
    return render(request, 'cms/pages/editar_pais.html', context)

@login_required
def eliminar_pais(request, id):
    paix = Pais.objects.get(id=id)
    paix.delete()
    return redirect('lista_paises')

@login_required
def crear_region(request):
    usuario = User.objects.get(id=request.user.id)
    profiles = Profile.objects.get(usuario=usuario.id)
    paises = Pais.objects.all()
    if paises is None:
        paises = None
    if request.method == 'POST':
        form = RegionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_region')
    else: 
        form = RegionForm()
    context = {
        'form': form,
        'usuario': usuario,
        'profiles': profiles,
        'paises': paises,
        
    }
    return render(request, 'cms/pages/crear_region.html', context)


def lista_region(request):
    usuario = User.objects.get(id=request.user.id)
    profiles = Profile.objects.get(usuario=usuario.id)
    regiones = Region.objects.all()
    context = {
        'profiles': profiles,
        'usuario': usuario,
        'regiones': regiones,
    }
    return render(request, 'cms/pages/lista_region.html', context)

@login_required
def editar_region(request, idreg):
    usuarios = User.objects.get(id=request.user.id)
    profiles = Profile.objects.get(usuario=usuarios.id)    
    regiones = get_object_or_404(Region, id=idreg)
    if request.method == 'POST':
        form = RegionForm(request.POST, instance=regiones)
        if form.is_valid():
            form.save()
            return redirect('lista_region')
    else:
        form = RegionForm(instance=regiones)
    context = {
        'form': form,
        'regiones': regiones,
        'usuario': usuarios,
        'profiles': profiles,
    }
    return render(request, 'cms/pages/editar_region.html', context)

@login_required
def eliminar_region(request, id):
    region = Region.objects.get(id=id)
    region.delete()
    return redirect('lista_region')

@login_required
def crear_comuna(request):
    usuario = User.objects.get(id=request.user.id)
    profiles = Profile.objects.get(usuario=usuario.id)
    if request.method == 'POST':
        formulario = ComunaForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            return redirect('lista_comuna')
        else:
            context = {
                'formulario': formulario,  # <--- ¡Asegúrate de pasar el formulario aquí!
                'profiles': profiles,
                'usuario': usuario,
            }
            return render(request, 'cms/pages/crear_comuna.html', context)
    else:
        formulario = ComunaForm()
        context = {
            'formulario': formulario,
            'profiles': profiles,
            'usuario': usuario,
        }
        return render(request, 'cms/pages/crear_comuna.html', context)


@login_required
def lista_comunas(request):
    usuario = User.objects.get(id=request.user.id)
    profiles = Profile.objects.get(usuario=usuario.id)
    regiones = Region.objects.all()
    comunas = Comuna.objects.all()
    context = {
        'profiles': profiles,
        'usuario': usuario,
        'regiones': regiones,
        'comunas': comunas,
    }
    return render(request, 'cms/pages/lista_comuna.html', context)

@login_required
def editar_comuna(request, id):
    usuario = User.objects.get(id=request.user.id)
    profiles = Profile.objects.get(usuario=usuario.id)
    comuna = Comuna.objects.get(id=id)
    if request.method == 'POST':
        formulario = ComunaForm(request.POST, instance=comuna)
        if formulario.is_valid():
            formulario.save()
            return redirect('lista_comuna') # Reemplaza 'lista_comunas' con tu URL de lista
    else:
        formulario = ComunaForm(instance=comuna)
    context = {
        'formulario': formulario,
        'comuna': comuna,
        'profiles': profiles,
        'usuario': usuario,
    }
    return render(request, 'cms/pages/editar_comuna.html', context)

@login_required
def eliminar_comuna(request, id):
    usuario = User.objects.get(id=request.user.id)
    profiles = Profile.objects.get(usuario=usuario.id)
    comuna = Comuna.objects.get(id=id)
    comuna.delete()
    context = {
        'profiles': profiles,
        'usuario': usuario,
    }
    return redirect('cms/pages/lista_comuna',context)

@login_required
def crear_empresa(request):
    usuario = User.objects.get(id=request.user.id)
    profiles = Profile.objects.get(usuario=usuario.id)
    if request.method == 'POST':
        form = EmpresaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_empresa')
    else: 
        form = EmpresaForm()
    context = {
        'form': form,
        'profiles': profiles,
        'usuario': usuario,
    }
    return render(request, 'cms/pages/crear_empresa.html',context)

@login_required
def lista_empresa(request):
    usuario = User.objects.get(id=request.user.id)
    profiles = Profile.objects.get(usuario=usuario.id)
    empresas = Empresa.objects.all()
    context = {
        'profiles': profiles,
        'usuario': usuario,
        'empresas': empresas,
    }
    return render(request, 'cms/pages/lista_empresa.html', context)

@login_required
def editar_empresa(request, id):
    usuario = User.objects.get(id=request.user.id)
    profiles = Profile.objects.get(usuario=usuario.id)
    empresa = empresa.objects.get(id=id)
    if request.method == 'POST':
        form = EmpresaForm(request.POST, instance=empresa)
        if form.is_valid():
            form.save()
            return redirect('lista_empresa')
    else:
        form = EmpresaForm(instance=empresa)
    context = {
        'form': form,
        'empresa': empresa,
        'profiles': profiles,
        'usuario': usuario,
    }
    return render(request, 'cms/pages/editar_empresa.html', context)

@login_required
def eliminar_empresa(request, id):
    usuario = User.objects.get(id=request.user.id)
    profiles = Profile.objects.get(usuario=usuario.id)
    empresa = empresa.objects.get(id=id)
    empresa.delete()
    context = {
        'profiles': profiles,
        'usuario': usuario,
    }
    return redirect('lista_empresa',context)

@login_required
def crear_representante(request):
    usuario = User.objects.get(id=request.user.id)
    profiles = Profile.objects.get(usuario=usuario.id)
    if request.method == 'POST':
        form = RepresentanteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_representante')
    else: 
        form = RepresentanteForm()
    context = {
        'form': form,
        'profiles': profiles,
        'usuario': usuario,
    }
    return render(request, 'cms/pages/crear_representante.html', context)

@login_required
def lista_representante(request):
    usuario = User.objects.get(id=request.user.id)
    profiles = Profile.objects.get(usuario=usuario.id)
    representantes = Representante.objects.all()
    context = {
        'profiles': profiles,
        'usuario': usuario,
        'representantes': representantes,
    }
    return render(request, 'cms/pages/lista_representante.html', context)    

@login_required
def editar_representante(request, id):
    usuario = User.objects.get(id=request.user.id)
    profiles = Profile.objects.get(usuario=usuario.id)
    representante = representante.objects.get(id=id)
    if request.method == 'POST':
        form = RepresentanteForm(request.POST, instance=representante)
        if form.is_valid():
            form.save()
            return redirect('lista_representante')
    else:
        form = RepresentanteForm(instance=representante)
    context = {
        'form': form,
        'representante': representante,
        'profiles': profiles,
        'usuario': usuario,
    }
    return render(request, 'cms/pages/editar_representante.html', context)

@login_required
def eliminar_representante(request, id):
    usuario = User.objects.get(id=request.user.id)
    profiles = Profile.objects.get(usuario=usuario.id)
    representante = representante.objects.get(id=id)
    representante.delete()
    context = {
        'profiles': profiles,
        'usuario': usuario,
    }
    return redirect('lista_representante', context)

@login_required
def crear_colegio(request):
    usuario = User.objects.get(id=request.user.id)
    profiles = Profile.objects.get(usuario=usuario.id)
    if request.method == 'POST':
        form = ColegioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_colegio')
    else: 
        form = ColegioForm()
    context = {
        'form': form,
        'profiles': profiles,
        'usuario': usuario,
    }
    return render(request, 'cms/pages/crear_colegio.html', context)

@login_required
def lista_colegio(request):
    usuario = User.objects.get(id=request.user.id)
    profiles = Profile.objects.get(usuario=usuario.id)
    colegios = Colegio.objects.all()
    context = {
        'profiles': profiles,
        'usuario': usuario,
        'colegios': colegios,
    }
    return render(request, 'cms/pages/lista_colegio.html', context)

@login_required
def editar_colegio(request, id):
    usuario = User.objects.get(id=request.user.id)
    profiles = Profile.objects.get(usuario=usuario.id)
    colegio = colegio.objects.get(id=id)
    if request.method == 'POST':
        form = ColegioForm(request.POST, instance=colegio)
        if form.is_valid():
            form.save()
            return redirect('lista_colegio')
    else:
        form = ColegioForm(instance=colegio)
    context = {
        'form': form,
        'colegio': colegio,
        'profiles': profiles,
        'usuario': usuario,
    }
    return render(request, 'cms/pages/editar_colegio.html', context)

@login_required
def eliminar_colegio(request, id):
    usuario = User.objects.get(id=request.user.id)
    profiles = Profile.objects.get(usuario=usuario.id)
    colegio = colegio.objects.get(id=id)
    colegio.delete()
    context = {
        'profiles': profiles,
        'usuario': usuario,
    }
    return redirect('lista_colegio', context)

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