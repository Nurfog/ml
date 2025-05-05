from django.db import models

class Slider(models.Model):
    id = models.AutoField(primary_key=True)
    imagen = models.ImageField(upload_to='web/images/slides')
    titulo = models.CharField(max_length=150)
    descripcion = models.TextField()    
    fecha_publicacion = models.DateTimeField(auto_now=True)
    fecha_baja = models.DateTimeField(null=True, blank=True)
    orden = models.IntegerField(default=0)    
    estado = models.BooleanField(default=True)


    class Meta:
        verbose_name = 'Slider'
        verbose_name_plural = 'Sliders'
        ordering = ['-id']
        db_table = 'slider'
        indexes = [
                    models.Index(fields=['id'], name='idx_slider_titulo'),
                ]

    def __str__(self):
        return self.titulo
    
    def update (self, *args, **kwargs):
        self.fecha_publicacion = models.DateTimeField(auto_now=True)
        super().update(*args, **kwargs)
        
    def save(self, *args, **kwargs):
        self.fecha_publicacion = models.DateTimeField(auto_now=True)
        super().save(*args, **kwargs)
