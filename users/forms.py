from django import forms
from django.contrib.auth.forms import AuthenticationForm

class LoginForm(AuthenticationForm):
    username = forms.EmailField(label='Correo institucional')

    error_messages = {
        'invalid_login': 'Correo o contraseña incorrectos',
        'inactive': 'Esta cuenta está inactiva',
    }

    def clean_username(self):
        email = self.cleaned_data.get('username')

        if not email.endswith('@uanl.edu.mx'):
            raise forms.ValidationError(
                'El correo debe ser institucional (@uanl.edu.mx)'
            )

        return email