from django import forms
from cms.models import pais, region, comuna, empresa, representante, colegio, departamento, profile
from django import forms

class PaisForm(forms.ModelForm):
    class Meta:
        model = pais
        fields = ['codigo', 'nombre', 'nacionalidad', 'moneda', 'codigo_telefono']
        widgets = {
            'codigo': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ej: CL'}),
            'nombre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ej: Chile'}),
            'nacionalidad': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ej: Chilena'}),
            'moneda': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ej: CLP'}),
            'codigo_telefono': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ej: +56'}),
        }

    def clean_codigo(self):
        codigo = self.cleaned_data['codigo']
        return codigo.upper()

    def clean_nombre(self):
        nombre = self.cleaned_data['nombre']
        return nombre.capitalize()

    def clean_nacionalidad(self):
        nacionalidad = self.cleaned_data['nacionalidad']
        return nacionalidad.capitalize()

    def clean_moneda(self):
        moneda = self.cleaned_data['moneda']
        return moneda.upper()


class RegionForm(forms.ModelForm):
    class Meta:
        model =  region
        fields = ['pais','codigo', 'nombre']
        widgets = {
            'pais': forms.Select(attrs={'class': 'form-control'}),
            'codigo': forms.TextInput(attrs={'class': 'form-control'}),
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
        }
    def clean_codigo(self):
        codigo = self.cleaned_data['codigo']
        return codigo.upper()
    
    def clean_nombre(self):
        nombre = self.cleaned_data['nombre']
        return nombre.capitalize()
        

class ComunaForm(forms.ModelForm):
    class Meta:
        model =  comuna
        fields = ['provincia','codigo', 'nombre']
        widgets = {
            'provincia': forms.Select(attrs={'class': 'form-control'}),
            'codigo': forms.TextInput(attrs={'class': 'form-control'}),
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
        }
    def clean_codigo(self):
        codigo = self.cleaned_data['codigo']
        return codigo.upper()
    
    def clean_nombre(self):
        nombre = self.cleaned_data['nombre']
        return nombre.capitalize()
    

class EmpresaForm(forms.ModelForm):
    class Meta:
        model =  empresa
        fields = ['rut', 'razonsocial', 'comuna', 'direccion', 'telefono', 'email', 'logo']
        widgets = {
            'rut': forms.TextInput(attrs={'class': 'form-control'}),
            'razonsocial': forms.TextInput(attrs={'class': 'form-control'}),
            'comuna': forms.Select(attrs={'class': 'form-control'}),
            'direccion': forms.TextInput(attrs={'class': 'form-control'}),
            'telefono': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.TextInput(attrs={'class': 'form-control'}),
            'logo': forms.ClearableFileInput(attrs={'class': 'form-control-file'}),            
        }
    def clean_rut(self):
        rut = self.cleaned_data['rut']
        return rut.upper()
    
    def clean_razonsocial(self):
        razonsocial = self.cleaned_data['razonsocial']
        return razonsocial.capitalize()
    
    def clean_direccion(self):
        direccion = self.cleaned_data['direccion']
        return direccion.capitalize()
    
    def clean_telefono(self):
        telefono = self.cleaned_data['telefono']
        return telefono.upper()
    
    def clean_email(self):
        email = self.cleaned_data['email']
        return email.lower()
    
    def clean_logo(self):
        logo = self.cleaned_data['logo']
        return logo

class RepresentanteForm(forms.ModelForm):
    class Meta:
        model =  representante
        fields = ['empresa', 'rut', 'nombre', 'apellido', 'email', 'telefono', 'comunas', 'direccion']
        widgets = {
            'empresa': forms.Select(attrs={'class': 'form-control'}),
            'rut': forms.TextInput(attrs={'class': 'form-control'}),
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'apellido': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.TextInput(attrs={'class': 'form-control'}),
            'telefono': forms.TextInput(attrs={'class': 'form-control'}),
            'comunas': forms.SelectMultiple(attrs={'class': 'form-control'}),
            'direccion': forms.TextInput(attrs={'class': 'form-control'}),
            'logo': forms.ClearableFileInput(attrs={'class': 'form-control-file'}),
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
    
    def clean_logo(self):
        logo = self.cleaned_data['logo']
        return logo

class ColegioForm(forms.ModelForm):
    class Meta:
        model =  colegio
        fields = ['razon_social', 'comuna', 'direccion', 'telefono', 'email']
        widgets = {
            'razon_social': forms.TextInput(attrs={'class': 'form-control'}),
            'comuna': forms.Select(attrs={'class': 'form-control'}),
            'direccion': forms.TextInput(attrs={'class': 'form-control'}),
            'telefono': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.TextInput(attrs={'class': 'form-control'}),
        }
    def clean_razon_social(self):
        razon_social = self.cleaned_data['razon_social']
        return razon_social.capitalize()
    
    def clean_direccion(self):
        direccion = self.cleaned_data['direccion']
        return direccion.capitalize()
    
    def clean_telefono(self):
        telefono = self.cleaned_data['telefono']
        return telefono.upper()
    
    def clean_email(self):
        email = self.cleaned_data['email']
        return email.lower()
        
class PerfilForm(forms.ModelForm):
    class Meta:
        model =  profile
        fields = ['about', 'trabajo', 'rut', 'nombres', 'ap_paterno', 'ap_materno', 'id_pais', 'id_region', 'id_comuna', 'direccion', 'telefono', 'celular', 'foto',
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