#from cProfile import label
from django import forms
from autenticacion.models import Profile


class PerfilForm(forms.ModelForm):
    class Meta:
        model =  Profile
        fields = ['about', 'trabajo', 'rut', 'nombres', 'ap_paterno', 'ap_materno', 'id_pais', 'id_region', 'id_comuna', 'direccion', 'telefono', 'celular', 'email', 'foto',
                  'socialgit', 'socialx', 'socialfb', 'socialig', 'socialyt', 'socialli']        
        widgets = {
            'about': forms.Textarea(attrs={'class': 'form-control', 'rows': 5, 'placeholder': 'Escribe algo sobre ti...'}),
            'trabajo': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Cual es tu cargo en la empresa?'}),
            'rut': forms.TextInput(attrs={'class': 'form-control'}),
            'nombres': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombres'}),
            'ap_paterno': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Apellido Paterno'}),
            'ap_materno': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Apellido Materno'}),
            'id_pais': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Selecciona un país'}),
            'id_region': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Selecciona una región'}),
            'id_comuna': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Selecciona una comuna'}),
            'direccion': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Dirección'}),
            'telefono': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '+56212345678'}),
            'celular': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '+56912345678'}),
            'email': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'mail@empresa.com'}),
            'foto': forms.ClearableFileInput(attrs={'class': 'form-control-file', 'placeholder': 'Selecciona una foto de perfil'}),
            'socialgit': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'URL de tu perfil de GitHub'}),
            'socialx': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'URL de tu perfil de X'}),
            'socialfb': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'URL de tu perfil de Facebook'}),            
            'socialig': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'URL de tu perfil de Instagram'}),
            'socialyt': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'URL de tu canal de YouTube'}),
            'socialli': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'URL de tu perfil de LinkedIn'})
        }
    def clean_rut(self):
        rut = self.cleaned_data['rut']
        return rut.upper()
    
    def clean_nombre(self):
        nombre = self.cleaned_data['nombre']
        return nombre.capitalize()
    
    def clean_apellido(self):
        apellido = self.cleaned_data['apellido']
        return apellido.capitalize()

    def clean_email(self):
        email = self.cleaned_data['email']
        return email.lower()
    
    def clean_telefono(self):
        telefono = self.cleaned_data['telefono']
        return telefono.upper()
    
    def clean_direccion(self):
        direccion = self.cleaned_data['direccion']
        return direccion.capitalize()