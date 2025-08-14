from django.db import models
from django.contrib.auth.models import User
from cms.models import Comuna, Pais, Region

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

