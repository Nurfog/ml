from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import empresa, representante, pais, region, provincia, comuna, colegio, departamento, profile
from .forms import *


@login_required
def dashboardcms(request):
    if request.user.is_authenticated:
        try:
            profiles = profile.objects.get(user=request.user.id)
            fecha = User.objects.get(id=request.user.id)
        except profile.DoesNotExist:
            profiles = None

        context = {
            'profiles': profiles,
            'fecha': fecha,
        }
        return render(request, 'cms/pages/dashboard.html', context)
    else:
        # Si el usuario no está autenticado, redirigir a la página de inicio de sesión
        return redirect('cuentas')

@login_required
def crear_pais(request):
    if request.method == 'POST':
        form = PaisForm(request.POST)
        if form.is_valid():
            form.save()            
            return redirect('lista_paises')
    else: 
        form = PaisForm()
    return render(request, 'cms/pages/crear_pais.html', {'form': form})


def lista_paises(request):
    paises = pais.objects.all()
    return render(request, 'cms/pages/lista_paises.html', {'paises': paises})

@login_required
def editar_pais(request, id):
    paix = get_object_or_404(pais, id=id)
    if request.method == 'POST':
        form = PaisForm(request.POST, instance=paix)
        if form.is_valid():
            # Las transformaciones deberían estar en el método `clean` del formulario
            form.save()  # Guarda los cambios en la instancia
            return redirect('lista_paises')
    else:
        form = PaisForm(instance=paix)
    return render(request, 'cms/pages/editar_pais.html', {'form': form, 'pais': paix})

@login_required
def eliminar_pais(request, id):
    paix = pais.objects.get(id=id)
    paix.delete()
    return redirect('lista_paises')

@login_required
def crear_region(request):
    if request.method == 'POST':
        form = RegionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_region')
    else: 
        form = RegionForm()
    return render(request, 'cms/pages/crear_region.html', {'form': form})


def lista_region(request):
    regiones = region.objects.all()
    return render(request, 'cms/pages/lista_region.html', {'regiones': regiones})

@login_required
def editar_region(request, id):
    region = region.objects.get(id=id)
    if request.method == 'POST':
        form = RegionForm(request.POST, instance=region)
        if form.is_valid():
            form.save()
            return redirect('lista_region')
    else:
        form = RegionForm(instance=region)
    return render(request, 'cms/pages/editar_region.html', {'form': form, 'region': region})

@login_required
def eliminar_region(request, id):
    region = region.objects.get(id=id)
    region.delete()
    return redirect('lista_region')

@login_required
def crear_provincia(request):
    if request.method == 'POST':
        form = ProvinciaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_provincia')
    else: 
        form = ProvinciaForm()
    return render(request, 'cms/pages/crear_provincia.html', {'form': form})

def lista_provincia(request):
    provincias = provincia.objects.all()
    return render(request, 'cms/pages/lista_provincia.html', {'provincias': provincias})

@login_required
def editar_provincia(request, id):
    provincia = provincia.objects.get(id=id)
    if request.method == 'POST':
        form = ProvinciaForm(request.POST, instance=provincia)
        if form.is_valid():
            form.save()
            return redirect('lista_provincia')
    else:
        form = ProvinciaForm(instance=provincia)
    return render(request, 'cms/pages/editar_provincia.html', {'form': form, 'provincia': provincia})

@login_required
def eliminar_provincia(request, id):
    provincia = provincia.objects.get(id=id)
    provincia.delete()
    return redirect('lista_provincia')

@login_required
def crear_comuna(request):
    if request.method == 'POST':
        form = ComunaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_comuna')
    else: 
        form = ComunaForm()
    return render(request, 'cms/pages/crear_comuna.html', {'form': form})

def lista_comunas(request):
    comunas = comuna.objects.all()
    return render(request, 'cms/pages/lista_comuna.html', {'comunas': comunas})

@login_required
def editar_comuna(request, id):
    comuna = comuna.objects.get(id=id)
    if request.method == 'POST':
        form = ComunaForm(request.POST, instance=comuna)
        if form.is_valid():
            form.save()
            return redirect('lista_comuna')
    else:
        form = ComunaForm(instance=comuna)
    return render(request, 'cms/pages/editar_comuna.html', {'form': form, 'comuna': comuna})

@login_required
def eliminar_comuna(request, id):
    comuna = comuna.objects.get(id=id)
    comuna.delete()
    return redirect('lista_comuna')

@login_required
def crear_empresa(request):
    if request.method == 'POST':
        form = EmpresaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_empresa')
    else: 
        form = EmpresaForm()
    return render(request, 'cms/pages/crear_empresa.html', {'form': form})

def lista_empresa(request):
    empresas = empresa.objects.all()
    return render(request, 'cms/pages/lista_empresa.html', {'empresas': empresas})

@login_required
def editar_empresa(request, id):
    empresa = empresa.objects.get(id=id)
    if request.method == 'POST':
        form = EmpresaForm(request.POST, instance=empresa)
        if form.is_valid():
            form.save()
            return redirect('lista_empresa')
    else:
        form = EmpresaForm(instance=empresa)
    return render(request, 'cms/pages/editar_empresa.html', {'form': form, 'empresa': empresa})

@login_required
def eliminar_empresa(request, id):
    empresa = empresa.objects.get(id=id)
    empresa.delete()
    return redirect('lista_empresa')

@login_required
def crear_representante(request):
    if request.method == 'POST':
        form = RepresentanteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_representante')
    else: 
        form = RepresentanteForm()
    return render(request, 'cms/pages/crear_representante.html', {'form': form})

def lista_representante(request):
    representantes = representante.objects.all()
    return render(request, 'cms/pages/lista_representante.html', {'representantes': representantes})    

@login_required
def editar_representante(request, id):
    representante = representante.objects.get(id=id)
    if request.method == 'POST':
        form = RepresentanteForm(request.POST, instance=representante)
        if form.is_valid():
            form.save()
            return redirect('lista_representante')
    else:
        form = RepresentanteForm(instance=representante)
    return render(request, 'cms/pages/editar_representante.html', {'form': form, 'representante': representante})

@login_required
def eliminar_representante(request, id):
    representante = representante.objects.get(id=id)
    representante.delete()
    return redirect('lista_representante')

@login_required
def crear_colegio(request):
    if request.method == 'POST':
        form = ColegioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_colegio')
    else: 
        form = ColegioForm()
    return render(request, 'cms/pages/crear_colegio.html', {'form': form})

def lista_colegio(request):
    colegios = colegio.objects.all()
    return render(request, 'cms/pages/lista_colegio.html', {'colegios': colegios})

@login_required
def editar_colegio(request, id):
    colegio = colegio.objects.get(id=id)
    if request.method == 'POST':
        form = ColegioForm(request.POST, instance=colegio)
        if form.is_valid():
            form.save()
            return redirect('lista_colegio')
    else:
        form = ColegioForm(instance=colegio)
    return render(request, 'cms/pages/editar_colegio.html', {'form': form, 'colegio': colegio})

@login_required
def eliminar_colegio(request, id):
    colegio = colegio.objects.get(id=id)
    colegio.delete()
    return redirect('lista_colegio')


@login_required
def graba_perfil(request):
    if request.method == 'POST':
        form = PerfilForm(request.POST, instance=request.user.profile)
        if form.is_valid():
            form.save()
            return redirect('perfil')
    else:
        form = PerfilForm(instance=request.user.profile)
    return render(request, 'cms/pages/mostrar_perfil.html', {'form': form})

@login_required
def mostrar_perfil(request, username):
    if request.user.is_authenticated:
        try:
            profiles = profile.objects.get(user=request.user.id)
            usuario = User.objects.get(id=request.user.id)
            regiones = region.objects.get(id=profiles.id_region_id)            
            comunas = comuna.objects.get(id=profiles.id_comuna_id)
            paises = pais.objects.get(id=profiles.id_pais_id)
        except profile.DoesNotExist:
            profiles = None

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