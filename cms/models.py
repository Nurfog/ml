from django.db import models
from django.contrib.auth.models import User

class Pais(models.Model):
    id = models.AutoField(primary_key=True)
    codigo = models.CharField(max_length=150)
    nombre = models.CharField(max_length=150)
    nacionalidad = models.CharField(max_length=150)
    moneda = models.CharField(max_length=150)
    codigo_telefono = models.CharField(max_length=150)
    estado = models.BooleanField(default=True)

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = 'Pais'        
        verbose_name_plural = 'Paises'
        ordering = ['id']
        db_table = 'cms_pais'
        indexes = [
            models.Index(fields=['id'], name='idx_pais_titulo'),
        ]



class Region(models.Model):
    id = models.AutoField(primary_key=True)
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
        indexes = [
            models.Index(fields=['id'], name='idx_region_titulo'),
        ]

    def update (self, *args, **kwargs):        
        super().update(*args, **kwargs)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)


class Comuna(models.Model):    
    id = models.AutoField(primary_key=True)
    pais = models.ForeignKey(Pais, on_delete=models.CASCADE, related_name='pais_comuna')
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
        indexes = [
            models.Index(fields=['id'], name='idx_comuna_titulo'),
        ]

    def update (self, *args, **kwargs):        
        super().update(*args, **kwargs) 

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

class Empresa(models.Model):
    id = models.AutoField(primary_key=True)
    dniempresa = models.CharField(max_length=150)
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
        indexes = [
            models.Index(fields=['id'], name='idx_empresa_titulo'),
        ]

    def update (self, *args, **kwargs):        
        super().update(*args, **kwargs) 

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)


class Representante(models.Model):
    id = models.AutoField(primary_key=True)
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
        if self.estado == True:
            return self.nombre
        else:
            return 'No existe registro'
    
    def get_full_name(self):
        return f'{self.nombre} {self.apellido}'

    class Meta:
        verbose_name = 'Representante'
        verbose_name_plural = 'Representantes'
        ordering = ['id']
        db_table = 'cms_representante'
        indexes = [
            models.Index(fields=['id'], name='idx_representante_titulo'),   
        ]

    def update (self, *args, **kwargs):        
        super().update(*args, **kwargs) 

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)


class Colegio(models.Model):
    id = models.AutoField(primary_key=True)    
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
        indexes = [
            models.Index(fields=['id'], name='idx_colegio_titulo'),
        ]

    def update (self, *args, **kwargs):        
        super().update(*args, **kwargs)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)


class Departamento(models.Model):
    id = models.AutoField(primary_key=True)
    empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE, related_name='empresa_departamento')
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
        indexes = [
            models.Index(fields=['id'], name='idx_departamento_titulo'),
        ]

    def update (self, *args, **kwargs):
        super().update(*args, **kwargs)
    
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

class Profile(models.Model):
    id = models.AutoField(primary_key=True)
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    about = models.TextField(null=True)
    trabajo = models.CharField(max_length=150, blank=True, null=True)
    rut = models.CharField(max_length=150, blank=True, null=True)
    nombres = models.CharField(max_length=250, blank=True, null=True)
    ap_paterno = models.CharField(max_length=150, blank=True, null=True)
    ap_materno = models.CharField(max_length=150, blank=True, null=True)
    id_pais = models.ForeignKey(Pais, on_delete=models.CASCADE, related_name='pais_profile', blank=True, null=True)
    id_region = models.ForeignKey(Region, on_delete=models.CASCADE, related_name='region_profile', blank=True, null=True)
    id_comuna = models.ForeignKey(Comuna, on_delete=models.CASCADE, related_name='comuna_profile', blank=True, null=True)
    direccion = models.CharField(max_length=150, blank=True, null=True)
    telefono = models.CharField(max_length=150, blank=True, null=True)
    celular = models.CharField(max_length=150, blank=True, null=True)
    email = models.CharField(max_length=150, blank=True, null=True)
    foto = models.ImageField(upload_to='cms/images/profiles/fotos',blank=True, null=True)
    socialx = models.CharField(max_length=200, blank=True, null=True)
    socialfb = models.CharField(max_length=200, blank=True, null=True)    
    socialig = models.CharField(max_length=200, blank=True, null=True)
    socialyt = models.CharField(max_length=200, blank=True, null=True)
    socialli = models.CharField(max_length=200, blank=True, null=True)
    socialgit = models.CharField(max_length=200, blank=True, null=True)
    estado = models.BooleanField(default=True)

    def __str__(self):
        return self.nombres    

    class Meta:
        verbose_name = 'Profile'
        verbose_name_plural = 'Profiles'
        ordering = ['id']
        db_table = 'cms_profile'
        indexes = [
            models.Index(fields=['id'], name='idx_profile_titulo'),
        ]

    def update (self, *args, **kwargs):
        super().update(*args, **kwargs)
    
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)


