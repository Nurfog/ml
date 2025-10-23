from django import template
from django.templatetags.static import static

register = template.Library()


@register.filter
def foto_url(profile, default_path='images/user1-128x128.jpg'):
    """Return the URL of profile.foto if present, otherwise a static default image path.

    Usage in template: {{ profiles|foto_url }}
    Or with explicit default: {{ profiles|foto_url:'images/default-avatar.png' }}
    """
    if not profile:
        return static(default_path)
    try:
        if getattr(profile, 'foto') and getattr(profile.foto, 'url', None):
            return profile.foto.url
    except Exception:
        pass
    return static(default_path)