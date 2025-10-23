from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Profile


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    """Crea un perfil automáticamente cuando se crea un nuevo usuario."""
    if created:
        # Durante las migraciones la tabla cms_profile puede no existir aún;
        # capturamos errores de base de datos y los ignoramos para no romper
        # comandos de management (como migrate o createsuperuser).
        try:
            Profile.objects.create(user=instance)
        except Exception:
            # Importante: no re-raise aquí, solo evitamos que el signal
            # detenga la ejecución durante migraciones iniciales.
            pass
