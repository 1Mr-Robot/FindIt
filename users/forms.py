from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import get_user_model

#Login
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
    
#Register
User = get_user_model()

class RegisterForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    confirm_password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = [
            'institutional_email',
            'tuition',
            'first_name',
            'last_name',
            'phone',
            'role'
        ]

    def clean_institutional_email(self):
        email = self.cleaned_data.get('institutional_email')

        if not email.endswith('@uanl.edu.mx'):
            raise forms.ValidationError('El correo debe ser institucional')

        return email

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        confirm = cleaned_data.get("confirm_password")

        if password != confirm:
            raise forms.ValidationError("Las contraseñas no coinciden")

        return cleaned_data

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password"])  # Encripta la contraseña

        if commit:
            user.save()

        return user