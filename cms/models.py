from django.db import models
from django.contrib.auth.models import User

class Pais(models.Model):
    codigo = models.CharField(max_length=150)
    nombre = models.CharField(max_length=150)
    nacionalidad = models.CharField(max_length=150)
    moneda = models.CharField(max_length=150)
    estado = models.BooleanField(default=True)

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = 'Pais'        
        verbose_name_plural = 'Paises'
        ordering = ['id']
        db_table = 'cms_pais'

class Region(models.Model):
    pais = models.ForeignKey(Pais, on_delete=models.CASCADE, related_name='pais_region')
    codigo = models.CharField(max_length=150)
    nombre = models.CharField(max_length=150)
    estado = models.BooleanField(default=True)
   
    def __str__(self):
        return self.nombre
    
    class Meta:
        verbose_name = 'Region'        
        verbose_name_plural = 'Regiones'
        ordering = ['id']
        db_table = 'cms_regiones'

class Comuna(models.Model):    
    # Eliminada la entidad Provincia: ahora Comuna referencia directamente a Region
    region = models.ForeignKey(Region, on_delete=models.CASCADE, related_name='region_comuna')
    codigo = models.CharField(max_length=150)
    nombre = models.CharField(max_length=150)
    estado = models.BooleanField(default=True)    

    def __str__(self):
        return self.nombre
    
    class Meta:
        verbose_name = 'Comuna'
        verbose_name_plural = 'Comunas'
        ordering = ['id']
        db_table = 'cms_comunas'

class Empresa(models.Model):
    rut = models.CharField(max_length=150)
    razonsocial = models.CharField(max_length=150)
    comuna = models.ForeignKey(Comuna, on_delete=models.CASCADE, related_name='comuna_empresa')
    direccion = models.CharField(max_length=150)
    telefono = models.CharField(max_length=150)
    email = models.CharField(max_length=150)
    logo = models.ImageField(upload_to='cms/images/logos')
    estado = models.BooleanField(default=True)
    
    def __str__(self):
        return self.razonsocial

    class Meta:
        verbose_name = 'Empresa'
        verbose_name_plural = 'Empresas'
        ordering = ['id']
        db_table = 'cms_empresa'

class Representante(models.Model):
    empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE, related_name='empresa_representante')
    rut = models.CharField(max_length=150)
    nombre = models.CharField(max_length=150)
    apellido = models.CharField(max_length=150)
    email = models.CharField(max_length=150)
    telefono = models.CharField(max_length=150)
    comunas = models.ForeignKey(Comuna, on_delete=models.CASCADE, related_name='comuna_representante')
    direccion = models.CharField(max_length=150)
    estado = models.BooleanField(default=True)
    
    def __str__(self):
        if self.estado:
            return self.nombre
        return f'{self.nombre} (inactivo)'
    
    def get_full_name(self):
        return f'{self.nombre} {self.apellido}'

    class Meta:
        verbose_name = 'Representante'
        verbose_name_plural = 'Representantes'
        ordering = ['id']
        db_table = 'cms_representante'

class Colegio(models.Model):
    razon_social = models.CharField(max_length=150)
    comuna = models.ForeignKey(Comuna, on_delete=models.CASCADE, related_name='comuna_colegio')
    direccion = models.CharField(max_length=150)
    telefono = models.CharField(max_length=150)
    email = models.CharField(max_length=150)
    estado = models.BooleanField(default=True)
    
    def __str__(self):        
        return self.razon_social
    
    class Meta:
        verbose_name = 'Colegio'
        verbose_name_plural = 'Colegios'
        ordering = ['id']
        db_table = 'cms_colegio'

class Departamento(models.Model):
    nombre = models.CharField(max_length=150)
    descripcion = models.TextField()
    estado = models.BooleanField(default=True)

    def __str__(self):
        return self.nombre
    
    class Meta:
        verbose_name = 'Departamento'
        verbose_name_plural = 'Departamentos'
        ordering = ['id']
        db_table = 'cms_departamento'

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    about = models.TextField(null=True)
    trabajo = models.CharField(max_length=150, blank=True, null=True)
    rut = models.CharField(max_length=150, blank=True, null=True)
    nombres = models.CharField(max_length=250, blank=True, null=True)
    ap_paterno = models.CharField(max_length=150, blank=True, null=True)
    ap_materno = models.CharField(max_length=150, blank=True, null=True)
    pais = models.ForeignKey(Pais, on_delete=models.CASCADE, related_name='pais_profile', blank=True, null=True)
    region = models.ForeignKey(Region, on_delete=models.CASCADE, related_name='region_profile', blank=True, null=True)
    comuna = models.ForeignKey(Comuna, on_delete=models.CASCADE, related_name='comuna_profile', blank=True, null=True)
    direccion = models.CharField(max_length=150, blank=True, null=True)
    telefono = models.CharField(max_length=150, blank=True, null=True)
    celular = models.CharField(max_length=150, blank=True, null=True)
    foto = models.ImageField(upload_to='cms/images/profiles/fotos')
    socialx = models.CharField(max_length=200, blank=True, null=True)
    socialfb = models.CharField(max_length=200, blank=True, null=True)    
    socialig = models.CharField(max_length=200, blank=True, null=True)
    socialyt = models.CharField(max_length=200, blank=True, null=True)
    socialli = models.CharField(max_length=200, blank=True, null=True)
    socialgit = models.CharField(max_length=200, blank=True, null=True)
    estado = models.BooleanField(default=True)

    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name = 'Profile'
        verbose_name_plural = 'Profiles'
        ordering = ['id']
        db_table = 'cms_profile'