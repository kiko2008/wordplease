from django.contrib.auth.models import User
from django import forms
from django.forms.forms import Form


class LoginForm(Form):

    username = forms.CharField(label='Usuario:')
    password = forms.CharField(label='Contraseña', widget=forms.PasswordInput())


class RegisterForm(Form):

    username = forms.CharField(label='Usuario:')
    first_name = forms.CharField(label='Nombre:', required=False)
    last_name = forms.CharField(label='Apellidos:', required=False)
    email = forms.EmailField(label='Correo electronico:', required=False)
    password = forms.CharField(label='Contraseña', widget=forms.PasswordInput())
    password_confirmation = forms.CharField(label='Confirmar contraseña:', widget=forms.PasswordInput())

    def clean_username(self):
        username = self.cleaned_data.get('username', '').lower()
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError('El usuario {0} ya existe'.format(username))
        return username

    def clean(self):
        data = super().clean()
        if data.get('password') != data.get('password_confirmation'):
            raise forms.ValidationError('Las contraseñas introducidas no coinciden')
